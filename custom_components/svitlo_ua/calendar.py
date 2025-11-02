"""Модуль календаря інтеграції «Світло»."""
from datetime import datetime
from homeassistant.components.calendar import CalendarEntity, CalendarEvent
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from . import const

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[const.DOMAIN][entry.entry_id]
    async_add_entities([OutagesCalendar(coordinator)])

class OutagesCalendar(CoordinatorEntity, CalendarEntity):
    """Календар з запланованими відключеннями."""
    def __init__(self, coordinator):
        super().__init__(coordinator)
        region = coordinator.region
        group = coordinator.group
        self._attr_name = f"Відключення - {region} {group}"
        self._attr_unique_id = f"{region}_{group}_outages_calendar"
        self._attr_device_info = {
            "identifiers": {(const.DOMAIN, f"{region}-{group}")},
            "name": f"Світло - {region} черга {group}",
            "manufacturer": "Світло UA",
            "model": "Outage Schedule"
        }

    @property
    def event(self):
        # Наступний або активний івент
        events = self.coordinator.data.get("events", [])
        now = datetime.utcnow()
        next_event = None
        current_event = None
        for ev in events:
            start = ev.get("start")
            end = ev.get("end")
            if start and end and start <= now < end:
                current_event = ev
                break
            if start and start >= now:
                next_event = ev
                break
        ev = current_event or next_event
        if ev:
            summary = "Відключення електрики"
            ev_type = ev.get("type", "")
            if "POSSIBLE" in ev_type:
                summary = "Можливе " + summary
            return CalendarEvent(
                start=ev.get("start"), end=ev.get("end"), summary=summary
            )
        return None

    async def async_get_events(self, hass, start_date, end_date):
        events = []
        all_events = self.coordinator.data.get("events", [])
        for ev in all_events:
            start = ev.get("start")
            end = ev.get("end")
            if not start or not end:
                continue
            # Фільтр за запитом періоду
            if start < end_date and end > start_date:
                summary = "Відключення електрики"
                ev_type = ev.get("type", "")
                if "POSSIBLE" in ev_type:
                    summary = "Можливе " + summary
                events.append(CalendarEvent(start=ev["start"], end=ev["end"], summary=summary))
        return events

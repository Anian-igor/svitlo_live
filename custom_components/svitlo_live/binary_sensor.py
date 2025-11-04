from __future__ import annotations
from typing import Any
from homeassistant.core import HomeAssistant
from homeassistant.components.binary_sensor import (
    BinarySensorEntity,
    BinarySensorDeviceClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([SvitloElectricityStatusBinary(coordinator, entry)])

class SvitloBaseEntity(CoordinatorEntity):
    def __init__(self, coordinator) -> None:
        super().__init__(coordinator)

    @property
    def device_info(self) -> dict[str, Any]:
        region = getattr(self.coordinator, "region", "region")
        queue = getattr(self.coordinator, "queue", "queue")
        return {
            "identifiers": {(DOMAIN, f"{region}_{queue}")},
            "manufacturer": "svitlo.live",
            "model": f"Queue {queue}",
            "name": f"Svitlo • {region} / {queue}",
        }

class SvitloElectricityStatusBinary(SvitloBaseEntity, BinarySensorEntity):
    _attr_name = "Electricity status"
    _attr_device_class = BinarySensorDeviceClass.POWER

    def __init__(self, coordinator, entry: ConfigEntry) -> None:
        super().__init__(coordinator)
        self._attr_unique_id = f"{entry.entry_id}_power_{coordinator.region}_{coordinator.queue}"

    @property
    def is_on(self) -> bool | None:
        # ON/OFF логіка: on/maybe -> ON; off/unknown -> OFF
        val = getattr(self.coordinator, "data", {}).get("now_status")
        if val in ("on", "maybe"):
            return True
        if val in ("off", "unknown"):
            return False
        return None

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        d = getattr(self.coordinator, "data", {})
        return {
            "next_change_at": d.get("next_change_at"),
            "queue": d.get("queue"),
        }

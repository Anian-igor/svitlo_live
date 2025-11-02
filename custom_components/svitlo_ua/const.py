"""Константи для інтеграції «Світло»."""
DOMAIN = "svitlo_ua"

# Відповідність назвою регіона та API або URL джерела
REGION_API_MAPPING = {
    # Регіони Yasno:
    "Київ": {"api": "yasno", "region_code": "kiev"},
    "Київська область": {"api": "yasno", "region_code": "kievobl"},
    "Дніпропетровська обл.": {"api": "yasno", "region_code": "dnipro"},
    # Інші регіони Energy UA:
    "Львівська обл.": {"api": "energy_ua", "region_code": "lviv"},
    "Полтавська обл.": {"api": "energy_ua", "region_code": "poltava"},
    "Харківська обл.": {"api": "energy_ua", "region_code": "kharkiv"},
    "Чернігівська обл.": {"api": "energy_ua", "region_code": "chernigiv"},
    "Запорізька обл.": {"api": "energy_ua", "region_code": "zap"},
    "Закарпатська обл.": {"api": "energy_ua", "region_code": "zakarpat"},
    "Тернопільська обл.": {"api": "energy_ua", "region_code": "ternopil"},
    "Хмельницька обл.": {"api": "energy_ua", "region_code": "khmel"},
    "Чернівецька обл.": {"api": "energy_ua", "region_code": "chernivtsi"},
    "Сумська обл.": {"api": "energy_ua", "region_code": "sumy"},
    "Рівненська обл.": {"api": "energy_ua", "region_code": "rivne"},
    "Житомирська обл.": {"api": "energy_ua", "region_code": "zhytomyr"},
    "Івано-Франківська обл.": {"api": "energy_ua", "region_code": "prykarpattya"}
}

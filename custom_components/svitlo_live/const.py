from homeassistant.const import Platform

DOMAIN = "svitlo_live"

PLATFORMS: list[Platform] = [Platform.SENSOR, Platform.BINARY_SENSOR]

DEFAULT_SCAN_INTERVAL = 900  # 15 хв

CONF_REGION = "region"
CONF_QUEUE = "queue"
CONF_SCAN_INTERVAL = "scan_interval_seconds"

# Оновлений список (Херсонська прибрана)
REGIONS = {
    "cherkaska-oblast": "Черкаська область",
    "chernigivska-oblast": "Чернігівська область",
    "chernivetska-oblast": "Чернівецька область",
    "dnipropetrovska-oblast": "Дніпропетровська область",
    "donetska-oblast": "Донецька область",
    "harkivska-oblast": "Харківська область",
    # "hersonska-oblast": "Херсонська область",  # виключена
    "hmelnitska-oblast": "Хмельницька область",
    "ivano-frankivska-oblast": "Івано-Франківська область",
    "kirovogradska-oblast": "Кіровоградська область",
    "kyiv": "Київ",
    "kiivska-oblast": "Київська область",
    "lvivska-oblast": "Львівська область",
    "mikolaivska-oblast": "Миколаївська область",
    "odeska-oblast": "Одеська область",
    "poltavska-oblast": "Полтавська область",
    "rivnenska-oblast": "Рівненська область",
    "sumska-oblast": "Сумська область",
    "ternopilska-oblast": "Тернопільська область",
    "vinnitska-oblast": "Вінницька область",
    "volinska-oblast": "Волинська область",
    "zakarpatska-oblast": "Закарпатська область",
    "zaporizka-oblast": "Запорізька область",
    "jitomirska-oblast": "Житомирська область",
}

# Мапа режимів вибору черги/групи
# - DEFAULT: звичні "Черга 4.1", "4.2" ... (наш поточний випадок з підчергами)
# - CHERGA_NUM: Вінницька — "Черга 1..6" (без підчерг)
# - GRUPA_NUM: Чернівецька (1..12), Донецька (1..6) — "Група N"
REGION_QUEUE_MODE = {
    "vinnitska-oblast": "CHERGA_NUM",
    "chernivetska-oblast": "GRUPA_NUM",
    "donetska-oblast": "GRUPA_NUM",
    # інші — "DEFAULT"
}

# Класи з HTML
CLASS_MAP = {
    "on": "on",
    "off": "off",
    "f4": "off_first",   # 00–29 off, 30–59 on
    "f5": "off_second",  # 00–29 on, 30–59 off
}

INTERVAL_LABEL_TO_SECONDS = {
    "5 хв": 300, "10 хв": 600, "15 хв": 900, "30 хв": 1800,
    "1 год": 3600, "2 год": 7200, "4 год": 14400, "6 год": 21600, "12 год": 43200,
}

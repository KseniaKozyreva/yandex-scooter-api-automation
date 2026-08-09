from datetime import datetime, timedelta

class Urls:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/"
    DZEN_URL = "dzen.ru"

class TestData:
    tomorrow = (datetime.now() + timedelta(days=1)).strftime("%d.%m.%Y")
    day_after_tomorrow = (datetime.now() + timedelta(days=2)).strftime("%d.%m.%Y")

    USER_1 = ("Иван", "Иванов", "Ленинградская", "Сокольники", "79991112233", tomorrow, "Позвоните за час")
    USER_2 = ("Пётр", "Петров", "Кащенко", "Черкизовская", "79005556677", day_after_tomorrow, "Оставьте у подъезда")

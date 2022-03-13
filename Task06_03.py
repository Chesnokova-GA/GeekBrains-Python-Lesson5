"Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),"
"income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,"
"например, {""wage"": wage, ""bonus"": bonus}. Создать класс Position (должность) на базе класса Worker."
"В классе Position реализовать методы получения полного имени сотрудника (get_full_name) "
"и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных "
"(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров)."

class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int) -> None:
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            "wage": wage,
            "bonus": bonus
        }

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


chesnokova = Position("Galina", "Chesnokova", "analyst", 120000, 30000)
print(chesnokova.get_full_name(), chesnokova.get_total_income())

zaicev = Position("Anrey", "Zaicev", "Director", 130000, 35000)
print(zaicev.get_full_name(), zaicev.get_total_income())
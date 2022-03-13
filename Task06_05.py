"Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и "
"метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), "
"Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. "
"Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить, "
"что выведет описанный метод для каждого экземпляра."

class Stationery:
    title: str

    _message = "Запуск отрисовки."

    def draw(self):
        print(self._message)

class Pen(Stationery):
    title = 'Pen'
    _message = f"{title} - ручка"


class Pencil(Stationery):
    title = 'Pencil'
    _message = f"{title} - карандаш"


class Handle(Stationery):
    title = 'Handle'
    _message = f"{title} - маркер"


items = [Pen(), Pencil(), Handle()]

for item in items:
    item.draw()
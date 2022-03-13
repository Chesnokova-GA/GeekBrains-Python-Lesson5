"Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск)."
"Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый."
"Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — "
"на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый)."
"Проверить работу примера, создав экземпляр и вызвав описанный метод."
"Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее "
"сообщение и завершать скрипт."

import itertools
import time

class Trafficlight:
    __color: str
    __timing: dict

    def __init__(self, time_red: int = 7, time_yellow: int = 2, time_green: int = 3) -> None:
        self.__timing = {
            "red": time_red,
            "yellow": time_yellow,
            "green": time_green
        }

    def running(self):
        for switch, timer in itertools.cycle(self.__timing.items()):
            self.__color = switch

            for n in range(timer):
                print(f"{self} [{n+1}]")
                time.sleep(1)

    def __repr__(self):
        return f"Текущий режим = {self.__color}"

try:
    traffic_light = Trafficlight(7,2,3)
    traffic_light.running()
except KeyboardInterrupt:
    print("Exit the program")


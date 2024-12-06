import menu
import curses

class Task():
    def __init__(self):
        self.__id = 0
        self.__ptle = "Изучить основы Тестирование"
        self.__descrippon = "Написать тесты с использованием pytest"
        self.__category = "Обучени"
        self.__due_date = "2024-07-31"
        self.__priority = "Низкий"
        self.__status = "Выполнена"



def main(screen):
    menu.print(screen)


if __name__ == "__main__":
    curses.wrapper(main)
import curses
import time
import viewTask

class menu:

    menu_items = [
        "Просмотр задач",
        "Добавление задачи",
        "Изменение задачи",
        "Удаление задачи",
        "Поиск задач"
    ]

    submenus = {
        "Просмотр задач": [
            "Просмотр всех текущих задач.",
            "Просмотр задач по категориям."
        ],
        "Изменение задачи": [
            "Редактирование существующей задачи.",
            "Отметка задачи как выполненной."
        ],
        "Удаление задачи": [
            "Удаление задачи по идентификатору.",
            "Удаление задачи по категории."
        ],
        "Поиск задач": [
            "Поиск по категории",
            "Поиск по статусу выполения",
            "Поиск по ключевым словам"
        ]
    }
 

    current_index = 4
    current_sub_index = 2
    submenu_active = True

def callfunction(canvas):
    menu.functions[menu.current_index][menu.current_sub_index]
    canvas.refresh()


def printMainMenu(canvas):

    # Печать основного меню
    for i, item in enumerate(menu.menu_items):
        if i == menu.current_index:
            canvas.addstr(i, 0, item, curses.A_UNDERLINE)
        else:
            canvas.addstr(i, 0, item)

    canvas.addstr(len(menu.menu_items), 0, "Нажмите 'q' для выхода.")
    canvas.refresh()

def printSubMenu(canvas):
    canvas.clear()

    menu.submenu_active = True

    current_submenu = list(menu.submenus[menu.menu_items[menu.current_index]])
    # Печать подсменю
    for j, sub_item in enumerate(current_submenu):
        if j == menu.current_sub_index:
            canvas.addstr(len(menu.menu_items) + j + 1, 0, sub_item, curses.A_UNDERLINE)
        else:
            canvas.addstr(len(menu.menu_items) + j + 1, 0, sub_item)

    canvas.addstr(2, 0, " Нажмите 'Esc' для выхода назад.")
    canvas.addstr(1, 0, " \n")
    canvas.refresh()

def selectMainMenu(canvas, key):

    if key == 27:
            return 1  # Завершить выполнение программы
    elif key == 259:
        if(menu.current_index == 0):
            menu.current_index = 5
        menu.current_index -= 1
        canvas.refresh()
    elif key == 258:
        if(menu.current_index == 4):
            menu.current_index = -1
        menu.current_index += 1
        canvas.refresh()
    elif key == 10 or key in [10, 13]:  # Enter key
        if menu.menu_items[menu.current_index] in menu.submenus:
            menu.submenu_active = True
            menu.current_sub_index = 0
        else:
            temp(canvas)
            

    return 0


def selectSubMenu(canvas, key):
    if key == 259:
        if(menu.current_sub_index == 0):
            menu.current_sub_index = len(menu.submenus[menu.menu_items[menu.current_index]])
        menu.current_sub_index -= 1
        canvas.refresh()
    elif key == 258:
        if(menu.current_sub_index == len(menu.submenus[menu.menu_items[menu.current_index]]) - 1):
            menu.current_sub_index = -1
        menu.current_sub_index += 1
        canvas.refresh()
    elif key == 27:
        menu.submenu_active = False  
        canvas.refresh()
    
  
    if menu.submenu_active and key == (10 or 13):
        temp(canvas)
        canvas.refresh()
        canvas.getch()  # Ждем нажатия клавиши для продолжени 

    return 0
    

def temp(canvas):
    canvas.clear()
    if menu.current_index == 0:
        if menu.current_sub_index == 0:
           viewTask.printAll(1, canvas)
        else:
            searchByCategory(canvas)
        canvas.refresh()
    if menu.current_index == 1:
        add(canvas)
    if menu.current_index == 2:
        if menu.current_sub_index == 0:
            changeTask(canvas)
        else:
            changeStatus(canvas)
    if menu.current_index == 3:
        if menu.current_sub_index == 0:
            deleteTaskById(canvas)
        else:
            deleteTaskByCategory(canvas)
    if menu.current_index == 4:
        if menu.current_sub_index == 0:
            searchByCategory(canvas)
        elif menu.current_sub_index == 1:
            searchByStatus(canvas)
        else:
            searchByKeyWord(canvas)

def searchByKeyWord(canvas):
    canvas.addstr(0, 0, "Введите ключевое слово для поиска (ищет в ptle и desdescrippon)")
    keyWord = canv_input(1, canvas)
    keyWord = "Work"
    if keyWord == '':
        return
    else:
        viewTask.printByKeyWord(canvas, keyWord, 1)


def searchByStatus(canvas):
    canvas.addstr(0, 0, "Введите Статус для поиска")
    status = canv_input(1, canvas)
    if status == '':
        return
    else:
        viewTask.printByStatus(canvas, status, 1)


def searchByCategory(canvas):
    canvas.addstr(0, 0, "Введите Категорию для поиска")
    category = canv_input(1, canvas)
    if category == '':
        return
    else:
        viewTask.printByCategory(canvas, category, 1)
    

def deleteTaskById(canvas):
    viewTask.printAll(3, canvas)
    canvas.addstr(0, 0, "Введите id задачи которой хотите удалить")
    id = canv_input(1, canvas)
    if id == '':
        return
    else:
        viewTask.delete_task_by_id(canvas, int(id))
        canvas.clear()
        canvas.addstr(1, 0, "Delete id: " + id)
        viewTask.printAll(3, canvas)
        canvas.refresh()

def deleteTaskByCategory(canvas):
    viewTask.printAll(3, canvas)
    canvas.addstr(0, 0, "Введите category задачи которой хотите удалить")
    key = canv_input(1, canvas)
    if key == '':
        return
    else:
        viewTask.delete_task_by_category(canvas, key)
        canvas.clear()
        canvas.addstr(1, 0, "Delete category: " + key)
        viewTask.printAll(3, canvas)
        canvas.refresh()



def changeStatus(canvas):
    viewTask.printAll(3, canvas)
    canvas.addstr(0, 0, "Введите id задачи которой хотите отметить выполненой")
    id = canv_input(1, canvas)
    if id == '':
        return
    else:
        canvas.refresh()
        viewTask.change(canvas, int(id), "status",  "Выполнена")
        viewTask.printAll(3, canvas)

def changeTask(canvas):
    canvas.addstr(0, 0, "Введите id задачи")
    id = canv_input(1, canvas)
    if id == '':
        return
    else:
        viewTask.printByID(4, canvas, int(id))
        canvas.addstr(5+7, 0, "Введите что хотите изменить")
        key = canv_input(13, canvas)
        if key == '':
            return
        else:
            canvas.addstr(14, 0, "Введите Новое значение")
            new_str = canv_input(15, canvas)
            if new_str == '':
                return
            else:
                viewTask.change(canvas, int(id), key,  new_str)
                viewTask.printByID(17, canvas, int(id))
                canvas.refresh()



def add(canvas):
    canvas.clear()
    data = []
    canvas.addstr(2, 0, "Введите название задачи")
    data.append(canv_input(3, canvas))
    if data[0] == '': return
    canvas.addstr(4, 0, "Введите полный текст задачи")
    data.append(canv_input(5, canvas))
    if data[1] == '': return
    canvas.addstr(6, 0, "Введите категорию")
    data.append(canv_input(7, canvas))
    if data[2] == '': return
    canvas.addstr(8, 0, "Введите дату конца дедлайна")
    data.append(str(canv_input(9, canvas)))
    if data[3] == '': return
    canvas.addstr(10, 0, "Введите приоритет")
    data.append(str(canv_input(11, canvas)))
    if data[3] == '': return
    canvas.addstr(12, 0, "Введите статус")
    data.append(canv_input(13, canvas))
    if data[5] == '': return
    canvas.refresh()
    viewTask.addTask(canvas, data)

    #Реализовать выбор категории и статуса
# def canv_select_input(arrSelect):
#     canvas.addstr

def canv_input(pos, canvas):
    category = ""
    while True:
        char = canvas.getch() 
        

        if char == 10:  # Код клавиши Enter
            break
        elif char == 27: #Код escape
            break
        elif char == 127 or char == 8:  # Код для Backspace
            category = category[:-1]  
        else:
            category += chr(char)  

        canvas.addstr(pos, 0, " " * (curses.COLS - 1))  # Очищаем строку ввода
        canvas.addstr(pos, 0, category)  # Отображаем текущее значение
        canvas.refresh()  # Обновляем экран
    return category




def print(canvas):
    
    curses.curs_set(0)

    while True:
        canvas.clear()
        

        if menu.submenu_active:
            printSubMenu(canvas);
        else:
            printMainMenu(canvas);
        
        key = canvas.getch()

        if key == '10':
            break
        
        if(menu.submenu_active):
            selectSubMenu(canvas, key)
        elif(selectMainMenu(canvas, key) == 1) :
            break

        










import json
from tabulate import tabulate
import shutil
import os
import curses
import time
import search

file_path = r"..\data\taskList.json"

def printAll(pos, canvas):
    tasks = search.Searh.pushByTable(canvas)
    tableTask(canvas, tasks, pos)

def printByCategory(canvas, category, pos):
    task = search.Searh.sortBy(canvas, "category", category)
    tableTask(canvas, task, pos)

def printByKeyWord(canvas, KeyWord, pos):
    task = search.Searh.sortByKeyWord(canvas, KeyWord)
    tableTask(canvas, task, pos)

def printByStatus(canvas, status, pos):
    tasks = search.Searh.pushByTable(canvas)
    task = search.Searh.sortBy(canvas, "status", status)
    tableTask(canvas, task, pos)

def printByID(pos, canvas, id):
    tasks = search.Searh.pushByTable(canvas)
    task = search.Searh.sortBy(canvas, "id", id)
    tableTask(canvas, task, pos)
    return task


def tableTask(canvas, tasks, pos):
    headers = ["ID", "ptle", "descrippon", "category", "due_date", "priority", "status"]

    terminal_width, _ = shutil.get_terminal_size()
    max_col_widths = [terminal_width // len(headers)] * len(headers)

    if len(tasks) > 0:
    # Преобразование словаря в формат для tabulate
        formatted_table = [[task["id"], task["ptle"], task["descrippon"], task["category"],
                        task["due_date"], task["priority"], task["status"]] 
                        for task in tasks]
    
        canvas.addstr(pos, 0, tabulate(formatted_table, headers, tablefmt='double_grid', maxcolwidths=max_col_widths, stralign='center'))
    else:
        canvas.addstr(pos, 0, "В данной категории записей нет")


def addTask(canvas, info):

    if search.Searh.check_file(canvas) == 0:
        with open(file_path, 'r', encoding='utf-8') as f:
            templates = json.load(f)

    # Генерация нового id
    new_id = templates[-1]['id'] + 1 if templates else 1  # Начинаем с 1, если нет существующих

    # Создание нового задания
    data = {
        "id": new_id,
        "ptle": info[0],
        "descrippon": info[1],
        "category": info[2],
        "due_date": info[3],
        "priority": info[4],
        "status": info[5]
    }

    templates.append(data)  # Добавление нового задания в существующий список задач

    # Запись обновленных данных обратно в файл
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(templates, f, ensure_ascii=False, indent=4)

    canvas.addstr(1, 0, f"Задача с ID {new_id} успешно добавлена.")
    
def normalizathionid(canvas):
    if(search.Searh.check_file(canvas) == 0):
        with open(file_path, 'r', encoding='utf-8') as f:
            tasks = json.load(f)

        j = 1
        for obj in tasks:
            obj["id"] = j
            j += 1    

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, ensure_ascii=False, indent=4)

def change(canvas, task_id, key, new_str):

    if(search.Searh.check_file(canvas) == 0):
        with open(file_path, 'r', encoding='utf-8') as f:
            tasks = json.load(f)

        tasks[task_id-1][key] = new_str
        
        # Запись обновленных данных обратно в файл
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, ensure_ascii=False, indent=4)
        


       

def delete_task_by_id(canvas, task_id):

    if(search.Searh.check_file(canvas) == 0):
        with open(file_path, 'r', encoding='utf-8') as f:
            tasks = json.load(f)

    
    if(id != 0):
        updated_tasks = [task for task in tasks if task["id"] != task_id]

        if len(updated_tasks) < len(tasks):
            canvas.addstr(2, 0, f"Задача с ID {task_id} Удалена")
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(updated_tasks, f, ensure_ascii=False, indent=4)
            normalizathionid(canvas)
        else:
            canvas.addstr(2, 0, f"Задача с ID {task_id} не найдена.")



def delete_task_by_category(canvas, category):
    if(search.Searh.check_file(canvas) == 0):
        with open(file_path, 'r', encoding='utf-8') as f:
            tasks = json.load(f)

    if(category != ""):
        updated_tasks = [task for task in tasks if task["category"] != category]

        if len(updated_tasks) < len(tasks):
            canvas.addstr(2, 0, f"Задача с category {category} Удалена")

            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(updated_tasks, f, ensure_ascii=False, indent=4)

            normalizathionid(canvas)
            
        else:
            canvas.addstr(2, 0, f"Задача с category {category} не найдена.")
    
    canvas.refresh()


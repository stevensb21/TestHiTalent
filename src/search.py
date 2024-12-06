import json
from tabulate import tabulate
import shutil
import os
import curses
import time

file_path = r"..\data\taskList.json"

class Searh():

    def check_file(canvas):
        # Проверка на существование файла
        if not os.path.exists(file_path):
            canvas.addstr(0, 0, "Файл с задачами не найден.")
            return 1
        
        # Открываем файл для чтения
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                tasks = json.load(f)
                if not isinstance(tasks, list):
                    raise ValueError("Корневой элемент должен быть списком.")
            return 0
    
        except json.JSONDecodeError:
            canvas.addstr(0, 0, "Ошибка формата данных в файле.")
            return 1


    
    def my_search(canvas, tasks):
        row = {
            "id": tasks['id'], 
            "ptle": tasks['ptle'], 
            "descrippon": tasks['descrippon'], 
            "category": tasks['category'], 
            "due_date": tasks['due_date'], 
            "priority": tasks['priority'], 
            "status": tasks['status']
        }
        
        return row
    
    def pushByTable(canvas):
        if(Searh.check_file(canvas) == 0):
            with open(file_path, 'r', encoding='utf-8') as f:
                tasks = json.load(f)
            table = []
            if(len(tasks) > 0):
                for i in tasks:
                    table.append(Searh.my_search(canvas, i))
        return table

    def sortBy(canvas, typeSort, sortWord):
        tasks = Searh.pushByTable(canvas)
        task = []
        for i in tasks:
            if i[typeSort] == sortWord:
                task.append(i)
        return task
    
    def sortByKeyWord(canvas, KeyWord):
        tasks = Searh.pushByTable(canvas)
        task = []
        for i in tasks:
            if KeyWord in i["ptle"] or KeyWord in i["descrippon"]:
                task.append(i)
        return task
    

    
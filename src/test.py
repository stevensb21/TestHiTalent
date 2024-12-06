import json
import search
import curses
import time

file_path = r"..\data\taskList.json"



with open(file_path, 'r', encoding='utf-8') as f:
    tasks = json.load(f)

j = 1
for obj in tasks:
    obj["id"] = j
    j += 1  

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(tasks, f, ensure_ascii=False, indent=4)
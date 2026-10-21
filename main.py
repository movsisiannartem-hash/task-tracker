import sys
import json
from pathlib import Path
from datetime import datetime


args = sys.argv

#Функции
def load_json():
    path = Path("tasks.json")

    if not path.exists():
        with open(path, "w", encoding="utf-8") as f:
            json.dump([], f)

    with open(path, "r", encoding="utf-8") as f:
        tasks = json.load(f)


    return tasks

def save_json(tasks):
    with open(Path("tasks.json"), "w") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)


def add_task(description):
    tasks = load_json()
    now = datetime.now().isoformat()

    if not tasks:
        task_id = 1
    else:
        task_id = max(task["id"] for task in tasks) + 1

    task_dict = {"id": task_id, "description": description, "status": "todo", "createdAt": now, "updatedAt": now}
    tasks.append(task_dict)

    save_json(tasks)



def list_tasks(status=None):
    tasks = load_json()

    if not tasks:

        print("Задач пока нет")
        return


    for task in tasks:
        if status is None or task["status"] == status:
            print(f"{task['id']}: {task['description']} | {task['status']}")





def update_task(task_id, new_description):
   tasks = load_json()

   for task in tasks:
       if task["id"] == task_id:
           task["description"] = new_description
           task["updatedAt"] = datetime.now().isoformat()
           break
   else:
       print("Задача с таким ID не найдена")

   save_json(tasks)


def delete_task(task_id):
    tasks = load_json()
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_json(tasks)
            break
    else:
        print("Задача с таким ID не найдена")



def mark_in_progress(task_id):
    tasks = load_json()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            task["updatedAt"] = datetime.now().isoformat()
            save_json(tasks)
            break
    else:
        print("Задача с таким ID не найдена")


def mark_done(task_id):
    tasks = load_json()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            task["updatedAt"] = datetime.now().isoformat()
            save_json(tasks)
            break
    else:
        print("Задача с таким ID не найдена")


#Обработка CLI
if len(args) == 1:
    print("Используйте какую-нибудь команду")
elif args[1] == "add":
    if len(args) > 2:
        add_task(args[2])
    else:
        print("Использование: python main.py add 'Описание задачи'")

elif args[1] == "list":
    if len(args) > 2:
        if args[2] not in ["todo", "in-progress", "done"]:
            print("Неизвестный статус")
        else:
            list_tasks(args[2])

    else:
        list_tasks()

elif args[1] == "update":
    if len(args) > 3:
        try:
            update_task(int(args[2]), args[3])
        except ValueError:
            print("ID должен быть числом")
    else:
        print("Использование: python main.py update 'ID' 'description'")

elif args[1] == "delete":
    if len(args) > 2:
        try:
            delete_task(int(args[2]))
        except ValueError:
            print("ID должен быть числом")

    else:
        print("Использование: python main.py delete 'ID'")

elif args[1] == "mark-in-progress":
    if len(args) > 2:
        try:
            mark_in_progress(int(args[2]))
        except ValueError:
            print("ID должен быть числом")
    else:
        print("Использование: python main.py mark-in-progress 'ID'")

elif args[1] == "mark-done":
    if len(args) > 2:
        try:
            mark_done(int(args[2]))
        except ValueError:
            print("ID должен быть числом")
    else:
        print("Использование: python main.py mark-done 'ID'")

else:
    print("Такой команды нет")
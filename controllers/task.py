from flask import request
from models.task import Task

def add_task_function():
    if request.method == "POST":
        taskname = request.form["taskname"]
        url = request.form["url"]
        task = Task(
            taskname = taskname,
            url = url
        )

        task.save()
        data = {
            'id':task.id,
            'taskname':task.taskname,
            'url':task.url
        }
        return data
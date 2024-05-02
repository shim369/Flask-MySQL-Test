from flask import request
from models.task import Task
from extensions import db

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
    
def edit_task_function(data):
    if request.method == "POST":
        data.taskname = request.form["taskname"]
        data.url = request.form["url"]
        db.session.commit()
        return data
    
def delete_task_function(task):
    db.session.delete(task)
    db.session.commit()


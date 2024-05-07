from flask import Blueprint,render_template,redirect, request,url_for
from controllers.task import add_task_function,edit_task_function,delete_task_function
import sys
from models.task import Task

main = Blueprint('main',__name__)

@main.route("/", methods=["GET"])
def index():
    data = Task.get_all()
    return render_template("index.html", data=data)

@main.route("/addtask", methods=["GET","POST"])
def add_task():
    data = add_task_function()
    print(data,file=sys.stderr)
    return render_template("addtask.html", data=data)

@main.route("/edittask/<int:id>", methods=["GET","POST"])
def edit_task(id):
    task = Task.get_by_id(id)
    if request.method == "POST":
        edit_task_function(task)
        return redirect(url_for('main.index'))
    return render_template('edittask.html', task=task)

@main.route("/deletetask/<int:id>", methods=["POST"])
def delete_task(id):
    task = Task.get_by_id(id)
    print(task,file=sys.stderr)
    delete_task_function(task)
    return redirect(url_for('main.index'))

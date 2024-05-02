from flask import Blueprint,render_template
from controllers.task import add_task_function
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
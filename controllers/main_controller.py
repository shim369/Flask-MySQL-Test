from flask import Blueprint,render_template,request,redirect,session
from controllers.task import add_task_function
import sys

main = Blueprint('main',__name__)

@main.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@main.route("/addtask", methods=["GET","POST"])
def add_task():
    data = add_task_function()
    print(data,file=sys.stderr)
    return render_template("addtask.html",data=data)
from flask import Blueprint,render_template,request,redirect,session
main = Blueprint('main',__name__)

@main.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@main.route("/addtask", methods=["GET","POST"])
def add_task():
    return render_template("addtask.html")
    return render_template("complete.html")
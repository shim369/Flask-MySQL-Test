from flask import Blueprint,render_template,request,redirect,session
main = Blueprint('main',__name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/about")
def profile():
    myname = "Shim"
    hobbies = ["Sleep","Movie","Run"]
    return render_template("profile.html", myname = myname, hobbies = hobbies)

@main.route("/form", methods=["GET","POST"])
def form():
    if request.method == "GET":
        return render_template("form.html")
    else:     
        myname = request.form.get("myname")
        token = request.form.get("token")
        session["myname"] = myname
        return redirect("/confirm")

@main.route("/confirm", methods=["GET","POST"])
def confirm():
    if request.method == "GET":
        myname = session["myname"]
        return render_template("confirm.html", myname = myname)
    else:
        session.clear()
        return redirect("/complete")
    
@main.route("/complete")
def complete():
    return render_template("complete.html")
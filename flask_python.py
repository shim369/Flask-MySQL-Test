from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def profile():
    myname = "Shim"
    hobbies = ["Sleep","Movie","Run"]
    return render_template("profile.html", myname = myname, hobbies = hobbies)

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/result")
def result():
    req = request.args
    myname = req.get("myname")
    return myname

if __name__ == "__main__":
    #debug=False
    app.run(debug=True)
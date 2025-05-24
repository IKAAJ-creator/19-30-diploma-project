from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dogs")
def dogs():
    return render_template("dogs.html", title="dogs")

@app.route("/cats")
def cats():
    return render_template("cats.html", title="cats")

@app.route("/parrot")
def parrot():
    return render_template("parrot.html", title="parrots")

@app.route("/rrabit")
def rrabit():
    return render_template("rrabit.html", title="rabbits")

@app.route("/Features")
def Features():
    return render_template("Features.html", title="pluses")


@app.route("/About")
def About():
    return render_template("About.html", title="registration")

@app.route("/mem")
def mem():
    return render_template("mem.html", title="joke1")

@app.route("/Andr")
def Andr():
    return render_template("Andr.html", title="joke2")

@app.route("/NNM")
def NNM():
    return render_template("NNM.html", title="joke4")

@app.route("/spanio")
def spanio():
    return render_template("spanio.html", title="joke5")



app.run(debug=True)
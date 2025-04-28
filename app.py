from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dogs")
def dogs():
    return render_template("dogs.html", title="Информация о собаках")


@app.route("/Features")
def Features():
    return render_template("Features.html", title="Плюсы")


@app.route("/About")
def About():
    return render_template("About.html", title="Регестрация")





app.run(debug=True)
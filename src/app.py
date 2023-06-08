from flask import Flask, render_template

app = Flask("__name__")

@app.route("/")
def index():
      return render_template("home.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/hobbies")
def hobbies():
    return render_template("hobbies.html")
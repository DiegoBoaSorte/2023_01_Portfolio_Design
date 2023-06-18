from flask import Flask, render_template

app = Flask("__name__", template_folder="./src/templates", static_folder="./src/static")

@app.route("/")
def home():
      return render_template("home.html")


@app.route("/portfolio")
def portfolio():
    projetos = [
        "Projeto de Design Digital - Portfólio",
        "Projeto de Desenvolvimento Web - UNES",
        "Projeto API Projeto Integrado - DATA SARS"
    ]
    return render_template("portfolio.html", projetos=projetos)


@app.route("/hobbies")
def hobbies():
    return render_template("hobbies.html")


if __name__ == '__main__':
     app.run(debug=True)
     
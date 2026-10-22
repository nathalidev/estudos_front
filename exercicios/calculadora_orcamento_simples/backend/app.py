from flask import Flask, render_template, request

app = Flask(__name__, template_folder="frontend")


@app.route("/", methods=["GET", "POST"])
def calcular_orcamento():
    resultado = None
    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", resultado=None, erro=None)


def calcular_valor_bruto(horas_trabalhadas, valor_hora):
    if horas_trabalhadas < 0 or valor_hora < 0:
        raise ValueError("Horas trabalhadas e valor por hora devem ser não negativos.")
    return horas_trabalhadas * valor_hora

def aplicar_desconto(valor_bruto, desconto):
    return valor_bruto * (1 - desconto / 100)
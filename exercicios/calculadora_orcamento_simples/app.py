from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    if request.method == "POST":
        try:
            horas_trabalhadas = float(request.form["horas_trabalhadas"])
            valor_hora = float(request.form["valor_hora"])
            desconto = float(request.form["desconto"])
            
            valor_do_desconto = calcular_desconto(calcular_valor_bruto(horas_trabalhadas, valor_hora), desconto)

            valor_bruto = calcular_valor_bruto(horas_trabalhadas, valor_hora)
            valor_liquido = valor_final(valor_bruto, valor_do_desconto)

            return render_template(
                "index.html",
                valor_bruto=valor_bruto,
                valor_do_desconto=valor_do_desconto,
                valor_liquido=valor_liquido,
                horas_trabalhadas=horas_trabalhadas,
                valor_hora=valor_hora,
                desconto=desconto
            )
        except ValueError as e:
            return render_template(
                "index.html",
                erro=str(e)
            )


def calcular_valor_bruto(horas_trabalhadas, valor_hora):
    if horas_trabalhadas < 0 or valor_hora < 0:
        raise ValueError("Horas trabalhadas e valor por hora devem ser não negativos.")
    return horas_trabalhadas * valor_hora

def calcular_desconto(valor_bruto, perc_desconto):
    return valor_bruto * (perc_desconto / 100)

def valor_final(valor_bruto, desconto):
    return valor_bruto - desconto
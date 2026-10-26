from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calcular", methods=["POST"])
def calcular():
    if request.method == "POST":
        try:
            horas = int(request.form["horas_trabalhadas"])
            minutos = int(request.form["minutos_trabalhados"])
            valor_hora = float(request.form["valor_hora"])
            desconto = float(request.form["desconto"])

            if horas < 0:
                raise ValueError("As horas trabalhadas devem ser não negativas.")
            if minutos < 0 or minutos > 59:
                raise ValueError("Os minutos trabalhados devem estar entre 0 e 59.")

            horas_trabalhadas = horas + (minutos / 60)
            horas_trabalhadas_formatadas = f"{horas}h {minutos:02d}min"

            valor_do_desconto = str(calcular_desconto(calcular_valor_bruto(horas_trabalhadas, valor_hora), desconto)).replace(".", ",")

            valor_bruto = str(calcular_valor_bruto(horas_trabalhadas, valor_hora)).replace(".", ",")
            valor_liquido = str(valor_final(
                float(valor_bruto.replace(",", ".")), 
                float(valor_do_desconto.replace(",", "."))
            )).replace(".", ",")


            return render_template(
                "index.html",
                valor_bruto=valor_bruto,
                valor_do_desconto=valor_do_desconto,
                valor_liquido=valor_liquido,
                horas_trabalhadas_formatadas=horas_trabalhadas_formatadas,
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
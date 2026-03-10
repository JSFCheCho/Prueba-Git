#Buzon de prueba

from flask import Flask, render_template, request

app = Flask(__name__)


def comprobar_texto(texto):
    texto = texto.strip()
    if texto == "":
        return None
    return texto


def comprobar_entero(valor):
    valor = valor.strip()
    if not valor.isdigit():
        return None
    return int(valor)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/procesar", methods=["POST"])
def procesar():
    nombre = comprobar_texto(request.form.get("nombre", ""))
    programa = comprobar_texto(request.form.get("programa", ""))
    correo = comprobar_texto(request.form.get("correo", ""))
    edad = comprobar_entero(request.form.get("edad", ""))
    mensaje = comprobar_texto(request.form.get("mensaje", ""))

    errores = []

    if nombre is None:
        errores.append("Nombre inválido")
    if programa is None:
        errores.append("Programa académico inválido")
    if correo is None:
        errores.append("Correo inválido")
    if edad is None:
        errores.append("Edad inválida")
    if mensaje is None:
        errores.append("Mensaje inválido")

    if errores:
        return render_template("resultado.html", errores=errores, datos=None)

    datos = {
        "nombre": nombre,
        "programa": programa,
        "correo": correo,
        "edad": edad,
        "mensaje": mensaje
    }

    return render_template("resultado.html", errores=None, datos=datos)


if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask, render_template, abort, request
import os
import json
app = Flask(__name__)

with open('MSX.json') as fichero:
    datos=json.load(fichero)

@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("inicio.html")

@app.route('/juegos', methods=["GET","POST"])
def juegos():
    if request.method == "GET":
        categorias=[]
        for juego in datos:
            categorias.append(juego["categoria"])
        return render_template('juegos.html', categorias=set(categorias))
    else:
        nombre_juego=request.form.get("nombre")
        categoria=request.form.get("categorias")
        nombres=[]
        desarrolladores=[]
        identificadores=[]
        categorias=[]
        for juego in datos:
            categorias.append(juego["categoria"])
            if nombre_juego == "" and str(juego["categoria"]) == categoria:
                desarrolladores.append(juego["desarrollador"])
                nombres.append(juego["nombre"])
                identificadores.append(juego["id"])
            elif str(juego["nombre"]).startswith(nombre_juego) and str(juego["categoria"]) == categoria:
                desarrolladores.append(juego["desarrollador"])
                nombres.append(juego["nombre"])
                identificadores.append(juego["id"])
        return render_template("juegos.html", nom_juego=nombre_juego, l_nombres=nombres, l_desarrolladores=desarrolladores, l_identificadores=identificadores, l_categorias=set(categorias))

@app.route('/juego/<int:identificador>')
def juegos_detalles(identificador):
    for juegos in datos:
        if juegos["id"] == identificador:
            return render_template('detallejuegos.html', juego=juegos)
        
    return abort(404)

app.run('0.0.0.0',5000, debug=True)

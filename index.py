from webui import WebUI
from flask import Flask, render_template
#from flask_debugtoolbar import DebugToolbarExtension
from flask import request
import metodos, random

# acierto = 0
# fallo= 0
# posiciones = "vacio"
# c = []

app = Flask(__name__)
ui = WebUI(app, debug=True)
app.debug = True

#app.config['SECRET_KEY'] = '123'

#toolbar = DebugToolbarExtension(app)

# @app.route('/')
# def home():
#     return render_template('home.html')
palabra=""
@app.route('/')
def home():
    return render_template('inicio.html')

@app.route('/main')
def main():
    palabra = metodos.elegirPalabra()
    print(palabra)
    c=metodos.dividirPalabra(palabra)
    tamaño=metodos.obtenerTamaño(palabra)
    return render_template('main.html', tamaño=tamaño)

@app.route('/about')

def about():
    return render_template('about.html')

@app.route('/agregarPalabra', methods = ['POST', 'GET'])
def agregarPalabra():
    tamaño = 0
    if request.method == 'POST':
        palabra = request.form['palabra']
        metodos.agregarDiccionario(palabra)
        print(metodos.diccionario)
        tamaño = metodos.obtenerTamaño(palabra)
        print(tamaño)
    return render_template('agregarPalabra.html', tamaño=tamaño)

@app.route('/recibir', methods = ['POST','GET'])
def recibir():
    if request.method == 'GET':
        print("entro")
        letra = request.args.get('letra')
        print(letra)
        #acierto=0
        #fallo=0
        #posiciones="vacio"
        c=metodos.dividirPalabra(palabra)
        print(c)
        p,metodos.a,metodos.f = metodos.analizarRespuesta(c,letra,metodos.a,metodos.f,metodos.p)
        print(metodos.a)
        print(metodos.f)
    else:
        print("no entro")
    return "hola 2"
if __name__ == '__main__':
    app.run()
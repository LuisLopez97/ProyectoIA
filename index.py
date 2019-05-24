from webui import WebUI
from flask import Flask, render_template
#from flask_debugtoolbar import DebugToolbarExtension
from flask import request
from flask import jsonify
import metodos, random

# acierto = 0
# fallo= 0
# posiciones = "vacio"
#metodos.c = []

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
    metodos.c=[]
    palabra = metodos.elegirPalabra()
    print(palabra)
    metodos.c=metodos.dividirPalabra(palabra)
    #print("prueba c ",metodos.c)
    tamaño=metodos.obtenerTamaño(palabra)
    return render_template('main.html', tamaño=tamaño)

@app.route('/about')

def about():
    return render_template('about.html')

@app.route('/agregarPalabra', methods = ['POST', 'GET'])
def agregarPalabra():
    tamaño = 0
    if request.method == 'POST':
        metodos.c=[]
        palabra = request.form['palabra']
        metodos.agregarDiccionario(palabra)
        print(metodos.diccionario)
        tamaño = metodos.obtenerTamaño(palabra)
        metodos.c=metodos.dividirPalabra(palabra)
        print(tamaño)
        return render_template('main.html', tamaño=tamaño)
    else:
        return render_template('agregarPalabra.html')
   

@app.route('/recibir', methods = ['POST','GET'])
def recibir():
    if request.method == 'GET':
        letra = request.args.get('letra')
        #c = metodos.dividirPalabra(palabra)
        
        #print(metodos.c)
        metodos.p, metodos.a, metodos.f = metodos.analizarRespuesta(metodos.c, letra, metodos.a, metodos.f, metodos.p)
        
        # parametros = {'letra': letra, 'posicion' = str(metodos.p)}
    return jsonify({'letra': letra, 'posicion': metodos.p})

if __name__ == '__main__':
    app.run()
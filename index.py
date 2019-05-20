from webui import WebUI
from flask import Flask, render_template    
#from flask_debugtoolbar import DebugToolbarExtension
from flask import request
import metodos

app = Flask(__name__)
ui = WebUI(app, debug=True)
#app.debug = True

#app.config['SECRET_KEY'] = '123'

#toolbar = DebugToolbarExtension(app)

# @app.route('/')
# def home():
#     return render_template('home.html')

@app.route('/')
def home():
    return render_template('inicio.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/about')

def about():
    return render_template('about.html')

@app.route('/agregarPalabra', methods = ['POST', 'GET'])   
def agregarPalabra():
    if request.method == 'POST':
        palabra = request.form['palabra']
        metodos.agregarDiccionario(palabra)
        print(metodos.diccionario)
    return render_template('agregarPalabra.html')

if __name__ == '__main__':
    ui.run()
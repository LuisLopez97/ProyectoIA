from webui import WebUI
from flask import Flask, render_template

app = Flask(__name__)
ui = WebUI(app, debug=True)

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
    
@app.route('/agregarPalabra')
def agregarPalabra():
    return render_template('agregarPalabra.html')

if __name__ == '__main__':
    ui.run()
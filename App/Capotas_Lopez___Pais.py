from flask import Flask, render_template, request
import geocoder
import json

#FUNCIONES
def get_IP():
    return request.remote_addr

def pais_por_IP(ip):
    data = geocoder.ip(ip)
    return data.country

def return_pais_csv(code):
    data = {}

    with open('App/paises.json', 'r') as file:
        data = json.load(file)

    #Try and except si no encuentra poner undefined
    return data[code]

#INICIO DE FLASK
app = Flask(__name__)

@app.route('/')

# ---------------- PROGRAMA PRINCIPAL --------------
def index():
    #Variables de uso global
    IP = get_IP()
    
    #FOR TESTING
    IP = "200.114.151.167"

    PAIS = return_pais_csv(pais_por_IP(IP))

    data_html={
        'ip': IP,
        'pais': PAIS,
    }

    return render_template('index.html', data=data_html)

if __name__ == '__main__':
    app.run()
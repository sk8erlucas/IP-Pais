from flask import Flask, render_template, request
import geocoder
import gspread
from flask_cors import CORS



#FUNCIONES
def get_IP():
    return request.remote_addr

def pais_por_IP(ip):
    data = geocoder.ip(ip)
    return data.country

def BuscarPaisenSheet(code):
    sa = gspread.service_account(filename='App/capotas-lopez-35faa4b11037.json')
    sh = sa.open('Copia de Domicilios')

    wks = sh.worksheet('Hoja 1')

    data = wks.get_all_records()

    for i in data:

        if i['Code'] == code:
            return i['Idioma/pais']

    return 'undefined'



#INICIO DE FLASK
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')



# ---------------- PROGRAMA PRINCIPAL --------------
def index():
    #Variables de uso global
    IP = get_IP()
    
    #FOR TESTING
    IP = "200.114.151.167"

    PAIS = BuscarPaisenSheet(pais_por_IP(IP))

    data_html={
        'ip': IP,
        'pais': PAIS,
    }

    return render_template('index.html', data=data_html)

if __name__ == '__main__':
    app.run()
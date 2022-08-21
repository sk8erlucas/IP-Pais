from flask import Flask, render_template, request
import geocoder

#FUNCIONES
def get_IP():
    return request.remote_addr

def pais_por_IP(ip):
    data = geocoder.ip(ip)
    return data.country

#INICIO DE FLASK
app = Flask(__name__)

@app.route('/')

# ---------------- PROGRAMA PRINCIPAL --------------
def index():
    #Variables de uso global
    IP = get_IP()
    
    #FOR TESTING
    IP = "200.114.151.167"

    PAIS = pais_por_IP(IP)

    data_html={
        'ip':IP,
        'pais': PAIS,
    }

    return render_template('index.html', data=data_html)

if __name__ == '__main__':
    app.run()
import base64
import requests

class Qr():
    def __init__(self, path):
        self.path = path

    def decode(self, flag):
        pwd = base64.b64decode(flag).decode('utf-8')
        return pwd
    
    def read_qr(self):
        url_api = "http://api.qrserver.com/v1/read-qr-code/"

        with open(self.path, 'rb') as archivo:
            archivos = {'file': archivo}
            respuesta = requests.post(url_api, files=archivos)

            if respuesta.status_code == 200:
                contenido_codigo_qr = respuesta.json()[0]['symbol'][0]['data']
                return contenido_codigo_qr
            else:
                print(f"Error al escanear el código QR: {respuesta.status_code}")
                return None
    





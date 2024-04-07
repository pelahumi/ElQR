import requests

def escanear_codigo_qr(archivo_imagen):
    # URL de la API para escanear códigos QR
    url_api = "http://api.qrserver.com/v1/read-qr-code/"

    # Abrir y leer el archivo de imagen en modo binario
    with open(archivo_imagen, 'rb') as archivo:
        # Crear un diccionario de archivos para enviar en la solicitud POST
        archivos = {'file': archivo}
        
        # Enviar la solicitud POST a la API con el archivo de imagen
        respuesta = requests.post(url_api, files=archivos)
        
        # Verificar si la solicitud fue exitosa (código de estado 200)
        if respuesta.status_code == 200:
            # Decodificar la respuesta JSON para obtener el contenido del código QR
            contenido_codigo_qr = respuesta.json()[0]['symbol'][0]['data']
            return contenido_codigo_qr
        else:
            # Si hay un error en la solicitud, mostrar un mensaje de error
            print(f"Error al escanear el código QR: {respuesta.status_code}")
            return None

# Ejemplo de uso
archivo_imagen = "img/flag.png"  # Reemplazar con la ruta de tu imagen QR
contenido_codigo_qr = escanear_codigo_qr(archivo_imagen)
if contenido_codigo_qr:
    print(f"Contenido del código QR: {contenido_codigo_qr}")
else:
    print("No se pudo escanear el código QR.")







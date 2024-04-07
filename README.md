# El-QR

## Lectura de códigos QR

Para la lectura del código qr, en un inicio intenté utilizar ```pyzbar``` y ```opencv```. Sin embargo, debido a problemas en la instalación de ```pyzbar```, decidí buscar nuevas alternativas.

Así que para conseguir leerlos me conecté a una API llamada QR code API, con la que se puede crear y leer tus propios códigos QR. Para establecer la conexión a la API a través del enlace: ```http://api.qrserver.com/v1/read-qr-code/```, y mandamos el código QR utilizando el método POST.

## Descifrar el mensaje

Como sabemos que el mensaje está encriptado en base 64, lo podemos descifrar sin problemas. Sin embargo, al decodificarlo una vez, rápidamente nos damos cuenta que el mensaje sigue encriptado. Por lo que para descifrarlo por completo, haremos un bucle que lo descifre tantas veces como sea necesario para obtener el mensaje.

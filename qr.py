from pyzbar.pyzbar import ZBarSymbol, decode
from PIL import Image

qr = decode(Image.open('img/flag.png'), symbols=[ZBarSymbol.QRCODE])
print(qr)



from argparse import ArgumentParser
import pyzbar
import cv2

argument_parser = ArgumentParser()
argument_parser.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(argument_parser.parse_args())

image = cv2.imread(args["image"])

barcodes = pyzbar.decode(image)

for i, barcode in enumerate(barcodes, start=1):
    x, y, w, h = barcode.rect
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    barcode_data = barcode.data.decode("utf-8")
    barcode_type = barcode.type

    print(f'Información del código de barras #{i}: {barcode_data}')
    print(f'Tipo del codigo de barras: {barcode_type}')

    text = f"Data: {barcode_data}, Type: {barcode_type}"
    cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

cv2.imwrite("output.png", image)

  
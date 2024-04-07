from ElQR import Qr

def launcher():
    path = 'img/flag.png'

    qr = Qr(path)

    flag_encoded = qr.read_qr()

    print(f'Flag encoded: {flag_encoded}')

    print('Decoding flag...')

    while True:
        try:
            flag_encoded = qr.decode(flag_encoded)
            print(flag_encoded, '\n')
        except:
            print('Mensaje descifrado:', flag_encoded)
            break
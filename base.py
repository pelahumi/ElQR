import base64


def encode(pswd):
    code = base64.b64encode(pswd.encode('utf-8'))
    return code

def decode(data):
    pswd = base64.b64decode(data)
    return pswd

print(encode("Hola"))    
    
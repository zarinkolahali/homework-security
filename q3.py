import base64
from des import DesKey

plaintext='Break me'
ciphertext="OsQFp1sqAEo="

def decodedes(plaintext,ciphertext):
    cipher = ciphertext.encode('ascii')
    cipher = base64.b64decode(cipher) 
    for i in range(0,100000000):
        creatkey=str(i).zfill(8)
        key = DesKey(str.encode(creatkey))
        text=key.decrypt(cipher)
        if text==str.encode(plaintext):
            print('key= ',creatkey)
            break

def encodedes(plaintext,password):
    key= DesKey((str.encode(password)))
    return key.encrypt((str.encode(plaintext)),padding=True)

decodedes('Break me',"OsQFp1sqAEo=")    #key=  02062440
cipher=encodedes('971531040','02062440')
cipher64=base64.b64encode(cipher).decode('ascii')
print(cipher64)
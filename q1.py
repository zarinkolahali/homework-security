import base64
base64_message = 'bHd0Y2x4YWFsdHZncHNqcGl0'
#############################################
def shift(message,shift):
    result = ""
    for i in range(len(message)):
        char = message[i]
        if (char.isupper()):
            result += chr((ord(char) + shift-65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result
##############################################
base64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message_decode = message_bytes.decode('ascii')
#############################################
for i in range(0,25):
    print(shift(message_decode,i))

#########################################
name='zarinkolah'
cipher=shift(name,11)
base64_bytes = name.encode('ascii')
message_bytes = base64.b64encode(base64_bytes)
cipher_name = message_bytes.decode('ascii')
print(f"cipher_name: \"{cipher_name}\" name: \"{name}\"")
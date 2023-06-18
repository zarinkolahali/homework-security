from textwrap import wrap

def sxor(s1,s2):    
    return ''.join(str(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

def cipher_to_plain():
    cipher="59 6b 66 6b 67 24 2a 4b 6d 6b 78 2a 7e 7f 64 6f 79 7e 63 2a 63 64 2a 67 6b 7e 64 2a 78 6b 2a 68 6f 79 62 61 6b 64 63 2a 73 6b 64 63 2a 67 65 7c 6b 6c 6b 6d 62 2a 79 62 65 6e 63"
    c=cipher.replace(" ","")
    scale = 16
    res = bin(int(c, scale)).zfill(8)

    res=res.replace("b","")
    cipher_binary = wrap(res,8)


    for i in range(0,256):
        i=bin(i).zfill(10)
        i = i.replace("0b","")
        flag = 0
        str_text = ""
        for x in cipher_binary:
            if (((int(sxor(i,x),2) > 64) and (int(sxor(i,x),2) < 91)) or ((int(sxor(i,x),2) > 96) and (int(sxor(i,x),2) < 123)) or int(sxor(i,x),2)==32 ):
                flag +=1
                str_text += str(chr(int(sxor(i,x),2)))
        if ((len(c) // 2) == (flag+1)):
            print(f"str_text {str_text}")
            print(f"key {i}")

###################################################
def plain_to_cipher():
    plain_txt = "971531040"
    cipher_txt = ""

    binary_plain_txt =""
    for i in plain_txt:
        binary_plain_txt +=bin(ord(i)).zfill(10)

    binary_plain_txt = binary_plain_txt.replace("0b","")
    binary_plain_txt= wrap(binary_plain_txt,8)

    key = "00001010"
    for i in binary_plain_txt:
        cipher_txt+=sxor(i,key)
    txt =""
    cipher_txt = wrap(cipher_txt,8)
    for i in cipher_txt:
        txt+=str(hex(int(i,2)))
    txt=txt.replace("0x","")
    txt = wrap(txt,2)
    print(f"cipher_txt {txt} plainText {plain_txt}")


cipher_to_plain()
plain_to_cipher()
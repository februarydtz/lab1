from Crypto.Cipher import AES
import time
import sys

def read_file(filename):
    with open(filename) as f:
        data =  f.read()

    data = data.encode('utf-8')
    length = 16 - (len(data) % 16)
    data += bytes([length])*length
    return data

def enc(cbc_key, iv, text):
    aes = AES.new(cbc_key, AES.MODE_CBC, iv)
    cipher_text = aes.encrypt(text)
    return cipher_text

def dec(cbc_key, iv, text):
    aes = AES.new(cbc_key, AES.MODE_CBC, iv)
    msg=aes.decrypt(text)
    return msg

def run(iv, key, inputfile, outputfile):
    file = read_file(inputfile)
    cbc_key = key.encode('utf-8')
    iv = iv.encode('utf-8')

    start1 = time.time()
    cipher_text = enc(cbc_key, iv, file)
    enc_time = time.time() - start1

    with open(outputfile, 'wb') as output:
        output.write(cipher_text)

    start2 = time.time()
    msg = dec(cbc_key, iv, cipher_text)
    dec_time = time.time() - start2
 
    return enc_time, dec_time, file, cipher_text, msg

if __name__ == '__main__':
    iv, key, inputfile, outputfile = sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
    enc_time, dec_time, file, cipher_text, msg = run(iv,key,inputfile,outputfile)
    print('Input file: ',inputfile)
    print('encryption time : ',enc_time)
    print('decryption time : ',dec_time)
    f = open('AES_time.txt', 'a+')
    f.write(str(enc_time))
    f.write(' ')
    f.write(str(dec_time))
    f.write('\n')
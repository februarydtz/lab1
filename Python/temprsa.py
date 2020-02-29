import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import ast
import sys
import time

def read_file(filename):
    with open(filename) as f:
        data =  f.read()
    data = data.encode('utf-8')
    f.close()
    return data

def read_key(key_file):
    key_read = open(key_file, 'r')
    key = RSA.import_key(key_read.read())
    key_read.close()
    return(key)

def run(keyfile, publickey_file,inputfile,outputfile):
    key = read_key(keyfile)
    publickey = read_key(publickey_file)
    
    start1 = time.time()
    encryptor = PKCS1_OAEP.new(publickey)
    encrypted = encryptor.encrypt(file)
    enc_time = time.time() - start1

    with open(outputfile, 'wb') as output:
        output.write(encrypted)

    start2 = time.time()
    decryptor = PKCS1_OAEP.new(key)
    decrypted = decryptor.decrypt(ast.literal_eval(str(encrypted)))
    dec_time = time.time() - start2
    return enc_time, dec_time, file, encrypted, decrypted

def long_run(keyfile, publickey_file,file,outputfile):
    key = read_key(keyfile)
    publickey = read_key(publickey_file)
    length = len(file)
    step = length // 64

    start1 = time.time()
    encryptor = PKCS1_OAEP.new(publickey)
    count = 0
    encrypted = []
    output = open(outputfile, 'wb+')
    for i in range(step):
        encrypted.append(encryptor.encrypt(file[count:count+64]))
        count += 64
    if length % 64 != 0:
        encrypted.append(encryptor.encrypt(file[count:]))
    enc_time = time.time() - start1

    count = 0
    start2 = time.time()
    decryptor = PKCS1_OAEP.new(key)
    decrypted = b''
    for e in encrypted:
        decrypted += decryptor.decrypt(ast.literal_eval(str(e)))
        output.write(e)
    dec_time = time.time() - start2
    return enc_time, dec_time, file, encrypted, decrypted

if __name__ == '__main__':
    inputfile, outputfile = sys.argv[1], sys.argv[2]
    file = read_file(inputfile)
    public_key_file = r'master_bot_public_key.pem'
    private_key_file = r'master_bot_private_key.pem'
    if len(file) > 64:
        enc_time, dec_time, file, encrypted, decrypted = long_run(private_key_file,public_key_file,file,outputfile)
    else:
        enc_time, dec_time, file, encrypted, decrypted = run(private_key_file,public_key_file,file,outputfile)
    print('Input file: ',inputfile)
    print('encryption time : ',enc_time)
    print('decryption time : ',dec_time)
    f = open('RSA_time.txt', 'a+')
    f.write(str(enc_time))
    f.write(' ')
    f.write(str(dec_time))
    f.write('\n')
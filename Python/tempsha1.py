import hashlib
import sys
import time

def read_file(filename):
    with open(filename) as f:
        data =  f.read()

    data = data.encode('utf-8')
    length = 16 - (len(data) % 16)
    data += bytes([length])*length
    return data

if __name__ == '__main__':
    inputfile, outputfile = sys.argv[1], sys.argv[2]
    file = read_file(inputfile)
    start = time.time()
    result = hashlib.sha1(file)
    enc_time = time.time() - start
    with open(outputfile,'w') as f:
        f.write(result.hexdigest())
    print('Input file: ',inputfile)
    print('encryption time : ',enc_time)
    f = open('SHA1_time.txt', 'a+')
    f.write(str(enc_time))
    f.write('\n')
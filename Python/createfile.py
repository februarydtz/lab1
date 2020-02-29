import random
import sys

def genFile(file,size):
    filename = file + '_' + size + '.txt'
    f = open(filename,"wb+")
    f.close()
    f=open(filename,"ab+")
    for i in range(int(size)):
        c=chr(random.randint(0,127)).encode('utf-8')
        content=b""
        content=content+c
        f.write(content)
    f.close()
    print('Generate text file:', filename)
 
for i in range(2, len(sys.argv)):
    genFile(sys.argv[1],sys.argv[i])
import hmac
import hashlib
import sys
import time


inputfile, outputfile = sys.argv[1], sys.argv[2]
digest_maker = hmac.new(b'40fedf386da13d57',b'',hashlib.md5,)
f = open(inputfile, 'rb')
try:
    while True:
        block = f.read(1024)
        if not block:
            break
        digest_maker.update(block)
finally:
    f.close()

start = time.time()
digest = digest_maker.hexdigest()
enc_time = time.time() - start

with open(outputfile,'w') as f:
    f.write(digest)
print('Input file: ',inputfile)
print('encryption time : ',enc_time)
f = open('HMAC_time.txt', 'a+')
f.write(str(enc_time))
f.write('\n')


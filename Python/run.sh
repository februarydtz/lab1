python3 createfile.py DES 8 64 512 4096 32768 262144 2047152
python3 createfile.py AES 8 64 512 4096 32768 262144 2047152
python3 createfile.py HMAC 8 64 512 4096 32768 262144 2047152
python3 createfile.py SHA1 8 64 512 4096 32768 262144 2047152
python3 createfile.py RSA 2 4 8 16 32 64 128

rm -rf *.des *.aes *.hmac *.sha *.rsa
rm -rf DES_time.txt AES_time.txt HMAC_time.txt SHA1_time.txt RSA_time.txt
rm -rf *.png

python3 tempdes.py fedcba9876543210 40fedf386da13d57 DES_8.txt DES_8.des
python3 tempdes.py fedcba9876543210 40fedf386da13d57 DES_64.txt DES_64.des
python3 tempdes.py fedcba9876543210 40fedf386da13d57 DES_512.txt DES_512.des
python3 tempdes.py fedcba9876543210 40fedf386da13d57 DES_4096.txt DES_4096.des
python3 tempdes.py fedcba9876543210 40fedf386da13d57 DES_32768.txt DES_32768.des
python3 tempdes.py fedcba9876543210 40fedf386da13d57 DES_262144.txt DES_262144.des
python3 tempdes.py fedcba9876543210 40fedf386da13d57 DES_2047152.txt DES_2047152.des

python3 tempaes.py fedcba9876543210 40fedf386da13d57 AES_8.txt AES_8.aes
python3 tempaes.py fedcba9876543210 40fedf386da13d57 AES_64.txt AES_64.aes
python3 tempaes.py fedcba9876543210 40fedf386da13d57 AES_512.txt AES_512.aes
python3 tempaes.py fedcba9876543210 40fedf386da13d57 AES_4096.txt AES_4096.aes
python3 tempaes.py fedcba9876543210 40fedf386da13d57 AES_32768.txt AES_32768.aes
python3 tempaes.py fedcba9876543210 40fedf386da13d57 AES_262144.txt AES_262144.aes
python3 tempaes.py fedcba9876543210 40fedf386da13d57 AES_2047152.txt AES_2047152.aes

python3 temprsa.py RSA_2.txt RSA_2.rsa
python3 temprsa.py RSA_4.txt RSA_4.rsa
python3 temprsa.py RSA_8.txt RSA_8.rsa
python3 temprsa.py RSA_16.txt RSA_16.rsa
python3 temprsa.py RSA_32.txt RSA_32.rsa
python3 temprsa.py RSA_64.txt RSA_64.rsa
python3 temprsa.py RSA_128.txt RSA_128.rsa

python3 tempsha1.py SHA1_8.txt SHA1_8.sha
python3 tempsha1.py SHA1_64.txt SHA1_64.sha
python3 tempsha1.py SHA1_512.txt SHA1_512.sha
python3 tempsha1.py SHA1_4096.txt SHA1_4096.sha
python3 tempsha1.py SHA1_32768.txt SHA1_32768.sha
python3 tempsha1.py SHA1_262144.txt SHA1_262144.sha
python3 tempsha1.py SHA1_2047152.txt SHA1_2047152.sha

python3 tempHMAC.py HMAC_8.txt HMAC_8.hmac
python3 tempHMAC.py HMAC_64.txt HMAC_64.hmac
python3 tempHMAC.py HMAC_512.txt HMAC_512.hmac
python3 tempHMAC.py HMAC_4096.txt HMAC_4096.hmac
python3 tempHMAC.py HMAC_32768.txt HMAC_32768.hmac
python3 tempHMAC.py HMAC_262144.txt HMAC_262144.hmac
python3 tempHMAC.py HMAC_2047152.txt HMAC_2047152.hmac

python3 creategraph.py DES_time.txt AES_time.txt HMAC_time.txt SHA1_time.txt RSA_time.txt

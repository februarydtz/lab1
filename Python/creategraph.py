import matplotlib.pyplot as plt
import sys

for i in range(1,len(sys.argv)):
    inputfile = sys.argv[i]
    enc_time = []
    dec_time = []
    f = open(inputfile,'r')
    for line in f.readlines():
        if len(line.split(' ')) == 2:
            dec_time.append(float(line.split()[1]))
        enc_time.append(float(line.split()[0]))
    plt.bar(range(len(enc_time)), enc_time, color = 'rgb')
    plt.title(inputfile.split('.')[0] + ' - Encrypt')
    plt.ylabel('Encrypt time')
    plt.xlabel('File size')
    outputfile = inputfile.split('.')[0] + '_enc.png'
    plt.savefig(outputfile)
    print('Generate graph: ', outputfile)      
    if dec_time:
        plt.bar(range(len(dec_time)), dec_time, color = 'rgb')
        plt.title(inputfile.split('.')[0] + ' - Decrypt')
        plt.ylabel('Decrypt time')
        plt.xlabel('File size')
        outputfile = inputfile.split('.')[0] + '_dec.png'
        plt.savefig(outputfile)
        print('Generate graph: ', outputfile)

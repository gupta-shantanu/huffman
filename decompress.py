from HUFFMAN.components import *
import struct
import sys

input_file = sys.argv[1]
try:
    output_file = sys.argv[2]
except:
    output_file = "undef"


def decompress():
    i = open(input_file, 'rb')
    tmp = ""
    dump = ""
    while True:
        tm = i.read(1)
        if len(tm) != 1:
            break
        t = bin(struct.unpack('B', tm)[0])[2:]
        t = ("0" * (8 - len(t))).__add__(t)
        dump = dump + t
    treesize = int(int(dump[0:17], 2) / 2)
    codedtree = dump[16:treesize + 17]
    dump = dump[16 + treesize:]
    dictionary = {0: 0}
    dt[0] = 0
    k = decodetree(codedtree, 16)
    revhuffmantree(k, dictionary, "")
    offset = 0
    for ch in dump[::-1]:
        if ch == '1':
            break
        else:
            offset += 1
    dump = dump[0:len(dump) - offset]
    decomp = open(output_file, "wb")
    print("writing file")
    chunk = ""
    print("second " + dump)
    # just some debug data
    for ch in dump:
        chunk += ch
        if hash(chunk) in dictionary:
            decomp.write(struct.pack('B', dictionary[hash(chunk)]))
            chunk = ""
decompress()
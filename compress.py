from HUFFMAN.components import *
import struct
import sys

input_file = sys.argv[1]
try:
    output_file = sys.argv[2]
except IndexError:
    output_file = "compressed.huff"
file = open(input_file, 'rb')
inp = file.read()
original_size = len(inp)
arr = [huffnode(i, 0) for i in range(0, 256)]

for ch in inp:
    arr[ch].freq += 1

arr.sort(key=lambda x: x.freq)
link = lists(arr[0])

for a in arr[:0:-1]:
    if a.freq != 0:
        new = lists(a)
        new.next = link
        link = new
    else:
        break
tree = 0
while True:
    a = link.top()
    link = link.next
    b = link.top()
    link = link.next
    n = huffnode(257, a.freq + b.freq)
    n.right = a if a.freq > b.freq else b
    n.left = b if a.freq > b.freq else a
    new = lists(n)
    if link != 0:
        link = link.insert(new)
    else:
        tree = n
        break
comp = open(output_file, 'wb')


def combine(st):
    d = ""
    for ch in st:
        d += ch
    return d


def generateaddress(tree):
    """
    Generates address of character corresponding to huffman's tree
    :rtype : None

    """
    dictionary = {0: 0}
    huffmantree(tree, dictionary, "")
    encodehufftree(tree, 16)
    codedtree = combine(pt)
    size = len(codedtree)
    comp.write(struct.pack('B', int(size / 256)))
    comp.write(struct.pack('B', size % 256))
    chunk = ""
    for ch in codedtree:
        chunk = chunk + ch
        if len(chunk) > 8:
            comp.write(struct.pack('B', int(chunk[0:8], 2)))
            chunk = chunk[8:]
    df = ""
    for ch in inp:
        chunk += dictionary[ch]
        df += dictionary[ch]
        if len(chunk) > 8:
            comp.write(struct.pack('B', int(chunk[0:8], 2)))
            chunk = chunk[8:]

    chunk += "1"
    while len(chunk) % 8 == 0:
        chunk.__add__("0")
    while chunk != "":
        comp.write(struct.pack('B', int("0b" + chunk[0:8], 2)))
        chunk = chunk[8:]
    comp.flush()


try:
    generateaddress(tree)
    print("Job completed!")
except:
    print("An error occured!")
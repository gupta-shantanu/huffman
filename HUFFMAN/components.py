class huffnode:
    """
    Node of huffman tree
    huffnode.char
    huffnode.freq
    huffnode.right
    huffnode.left
    """

    def __init__(self, d, f):
        self.char = d
        self.freq = f
        self.right = 0
        self.left = 0

    def __repr__(self):
        """
Prints Single node
For debugging purpose
"""
        print(str(self.freq), str(chr(self.char)))


def printtree(root):
    if root != 0:
        printtree(root.left)
        print(str(root.char) + "  " + str(root.freq) + "||")
        printtree(root.right)


def huffmantree(root, a, bina):
    if root != 0:
        huffmantree(root.left, a, bina + "0")
        if root.char < 256:
            a[root.char] = bina

        huffmantree(root.right, a, bina + "1")


def revhuffmantree(root, a, bina):
    if root != 0:
        revhuffmantree(root.left, a, bina + "0")
        if root.char < 256:
            a[hash(bina)] = root.char
        revhuffmantree(root.right, a, bina + "1")


pt = list()


def encode(root, N):
    """
encodes data into huffman's tree
"""
    encodehufftree(root, N)
    return pt


def encodehufftree(root, N):
    if root.right == 0 and root.left == 0:
        tu = bin(root.char)[2:]
        pt.append("1" + "0" * (N - len(tu)) + tu)
    else:
        pt.append("0")
        encodehufftree(root.left, N)
        encodehufftree(root.right, N)


dt = [0]
pt = list()


def encode(root, N):
    """
decodes data from huffman's tree
"""
    encodehufftree(root, N)
    return dt


def decodetree(st, N):
    if len(st) <= dt[0]:
        return 0
    if st[dt[0]] == '1':
        dt[0] = dt[0] + N + 1
        if st[dt[0] - N: dt[0]] == '':
            return 0
        return huffnode(int(st[dt[0] - N: dt[0]], 2), 0)
    else:
        dt[0] += 1
        l = decodetree(st, N)
        r = decodetree(st, N)
        k = huffnode(257, 0)
        k.left = l
        k.right = r
        return k


kg = []


class lists:
    """
Utility Structure: lists
linked list class
"""

    def __init__(self, a):
        self.huffnd = a
        self.next = 0

    def insert(self, node):
        if node.huffnd.freq < self.huffnd.freq:
            node.next = self
            return node
        prev = self
        ptr = self.next
        while ptr != 0:
            if node.huffnd.freq > ptr.huffnd.freq:
                prev = ptr
                ptr = ptr.next
            else:
                break
        node.next = prev.next
        prev.next = node
        return self

    def top(self):
        if self != 0:
            return self.huffnd
        else:
            return 0

    def printlist(self):
        ptr = self
        while ptr != 0:
            print(str(ptr.huffnd.freq) + " " + str(chr(ptr.huffnd.char)))
            ptr = ptr.next

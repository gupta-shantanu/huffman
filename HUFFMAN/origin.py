file=open("test.txt",'rb')
class huffnode:
    def __init__(self,d,f):
        self.char=d
        self.freq=f
        self.right=0
        self.left=0
    def printhuff(self):
        print(str(self.freq)+" "+str(chr(self.char)))
def printtree(root):
    if root!=0:
        printtree(root.left)
        print(str(root.char)+"  "+str(root.freq)+"||")
        printtree(root.right)
def huffmantree(root,a,bina):
    if root!=0:
        huffmantree(root.left,a,bina+"0")
        if root.char<256:
            a[root.char]=bina

        huffmantree(root.right,a,bina+"1")
def revhuffmantree(root,a,bina):
    if root!=0:
        revhuffmantree(root.left,a,bina+"0")
        if root.char<256:
            a[hash(bina)]=root.char
        revhuffmantree(root.right,a,bina+"1")
pt=[]
def encodehufftree(root,N):
    if root.right==0 and root.left==0:
        tu=bin(root.char)[2:]
        pt.append("1"+"0"*(N-len(tu))+tu)
    else:
        pt.append("0")
        encodehufftree(root.left,N)
        encodehufftree(root.right,N)
dt=[0]
def decodetree(st,N):
    if len(st)<=dt[0]:
        return 0
    if st[dt[0]]=='1':
        dt[0]=dt[0]+N+1
        if st[dt[0]-N : dt[0]]=='':
            return 0        
        return huffnode(int(st[dt[0]-N : dt[0]],2),0)
    else:
        dt[0]=dt[0]+1
        l=decodetree(st,N)
        r=decodetree(st,N)
        k=huffnode(257,0)
        k.left=l
        k.right=r
        return k
        

#class node:
    
kg=[]    
class lists:
    def __init__(self,a):
        self.huffnd=a
        self.next=0
        
    def insert(self,node):
        if node.huffnd.freq<self.huffnd.freq:
            node.next=self
            return node
        prev=self
        ptr=self.next
        while ptr!=0:
                if node.huffnd.freq>ptr.huffnd.freq:
                    prev=ptr
                    ptr=ptr.next
                else:
                    break
        node.next=prev.next
        prev.next=node
        return self
    def top(self):
        if self!=0:
            return self.huffnd
        else :
            return 0
    def printlist(self):
        ptr=self
        while ptr!=0:
            print(str(ptr.huffnd.freq)+" "+str(chr(ptr.huffnd.char)))
            ptr=ptr.next
        
       
    
        
        
    


inp=file.read();
arr=[ huffnode(i,0) for i in range(0,256)]
d=0
for ch in inp:
    d=d+1
    arr[ch].freq=arr[ch].freq+1
print(d)


arr.sort(key=lambda x: x.freq)
link=lists(arr[0])
for a in arr[:0:-1]:
    if a.freq!=0:
        new=lists(a)
        new.next=link
        link=new
    else:
        break
tree=0
while True:
    a= link.top()
    link=link.next
    b= link.top()
    link=link.next
    n=huffnode(257,a.freq+b.freq)
    n.right= a if a.freq>b.freq else b
    n.left=b if a.freq>b.freq else a
    new=lists(n)
    if link!=0:
        link=link.insert(new)
    else:
        tree=n
        break
comp=open("compress.scf",'wb')
import struct
def combine(st):
    d=""
    for ch in st:
        d=d+ch
    return d
    
def generateaddress(n):   
    a={0:0}
    huffmantree(n,a,"")
    encodehufftree(n,16)
    codedtree=combine(pt)
    s=len(codedtree)
    comp.write(struct.pack('B',int(s/256)))
    comp.write(struct.pack('B',s%256))
    chunk=""
    for ch in codedtree:
        chunk=chunk+ch
        if len(chunk)>8:
            comp.write(struct.pack('B',int(chunk[0:8],2)))
            chunk=chunk[8:]
    df=""      
    for ch in inp:
        chunk=chunk+a[ch]
        df=df+a[ch]
        if len(chunk)>8:
            comp.write(struct.pack('B',int(chunk[0:8],2)))
            chunk=chunk[8:]
    print("first data "+df[:50])
            
 
            
    chunk=chunk+"1"
    while len(chunk)%8==0:
        chunk.__add__("0")
    while chunk!="":
        comp.write(struct.pack('B',int("0b"+chunk[0:8],2)))
        chunk=chunk[8:]
    comp.flush()
    
    
def decompresstest(n):
    i=open("compress.scf",'rb')
   
    tmp=""
    dump=""
    while True:
        tm=i.read(1)
        if len(tm)!=1:
            break
        t=bin(struct.unpack('B',tm)[0])[2:]
        t=("0"*(8-len(t))).__add__(t)
        dump=dump+t
    treesize=int(int(dump[0:17],2)/2)
    codedtree=dump[16:treesize+17]
    dump=dump[16+treesize:]
    x={0:0}
    dt[0]=0
    k=decodetree(codedtree,16)
    revhuffmantree(k,x,"")
    offset=0
    for ch in dump[::-1]:
        if ch=='1':
            break
        else:
            offset=offset+1
    dump=dump[0:len(dump)-offset]
    decomp=open("decom.txt","wb")
    print("writing file")
    chunk=""
    print("second "+dump)
    for ch in dump:
        chunk=chunk+ch
        if x.__contains__(hash(chunk)):
            decomp.write(struct.pack('B',x[hash(chunk)]))
            chunk=""



generateaddress(tree)    
decompresstest(tree)


    
    
    
    









    

            
            
               
           

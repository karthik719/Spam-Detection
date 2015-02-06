import pickle
import math
from types import *
import sys

arg1 = sys.argv[1]
arg2 = sys.argv[2]
#ft = open('outputc.txt' , 'w')
with open(arg1 , 'rb') as fk:
    kk = pickle.load(fk)
#print(kk)
b = kk['classes'] 
bl = list(b.keys())
#print(bl)
k = len(bl)
p = 0

for i in range(k):
    p += b[bl[i]]

pb = {}
pw = {}
lw = {}
tw = {}
for x in range(k):
    pb[bl[x]] = math.log(b[bl[x]]/p)
#print(pb)

for x in range(k):
    kx = kk[bl[x]] 
    kxl = list(kx.values())
    length = len(kxl)
    t = 0
    for b in range(length):
        t = t + kxl[b]
    tw[bl[x]] = t
#print(tw)

z = 0  
for x in range(k):
    kx1 = kk[bl[x]]
    kxl1 = list(kx1.keys())
    z += len(kxl1)

with open(arg2 , 'r') as ff: 
    for line in ff:
        b = 0 
        for b in range(k):
            nw = 1
            for word in line.split(): 
                kx = kk[bl[b]] 
                if word in kx:
                    nw += math.log((kx[word]+1)/(tw[bl[b]] + z))
                else: 
                    nw += math.log(1/(tw[bl[b]] + z))
            lw[bl[b]] = nw 
        #print(lw)
        d = 0 
        e = 0 
        for d in range(k):
            e += lw[bl[d]]
        #print(e)  
        f = 0
        r = float("-inf")
        g = {}
        for f in range(k):
            g = (pb[bl[f]] + lw[bl[f]])
            #print(g) 
            if g > r:
                r = g
                u = bl[f]
        print(u)
        #ft.write(u)
        #ft.write('\n')



  
             

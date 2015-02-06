import re
import pickle
from collections import Counter
from string import punctuation
import sys
import string

arg1 = sys.argv[1]
arg2 = sys.argv[2]
Quizlist=[]
tr=[]
counterb = Counter()
counter = Counter()
with open(arg1, 'r') as f:
#with open('/home/karthik719/Desktop/test.py') as f:
    for line in f:
        #linep = line.lower()
        Quizlist.append(line.split(None,1)[0])
    counter.update(word.strip(punctuation) for word in Quizlist)
    classes = dict(counter)
    #print(classes)

    ke = list(classes.keys())
k=len(classes)
index = 0 

kp = {}
kt = [{} for k in range(k)]

with open(arg1 ,'r') as f:
#with open('/home/karthik719/Desktop/test.py') as f:
    for line in f:
        #linen = line.lower()
        #line = re.sub(r'[^\w\s]','',line)
        #line = re.sub('[^a-z,^0-9,^A-Z\ \']+', " ", line)
        for word in line.split():
            #tr.append(word.strip(punctuation))
            tr.append(word)
        #print(tr)
        lt = len(tr)
        for index in range(0,k):
            if tr[0] == ke[index]:
                for i in range(1,lt):
                    if tr[i] in kt[index]:
                        kt[index][tr[i]] += 1
                    else: 
                        kt[index][tr[i]] = 1
                    i += 1
            index += 1
        tr = []

#print(kt)

x = 0 
kp['classes'] = classes 
for x in range(k):
    kp[ke[x]] = kt[x]
    x +=1

#print(kp)

with open(arg2, 'wb') as ft:
    pickle.dump(kp,ft)

#with open('model.txt' , 'rb') as fk:
    #kk = pickle.load(fk)

#print(kk)





                
    



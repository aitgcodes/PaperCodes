import itertools
import numpy as np


f = open('Region_A.dat','r')
k = open('Region_B.dat','r')
m = open('AB_weights.dat','w',newline='')
multi = []
bulti = []
for i in f:
    multi.append(i)
print(len(multi))
for j in k:    
    bulti.append(j)
print(len(bulti))
a=np.array(multi,dtype="float64")[:187]
b=np.array(bulti,dtype="float64")[187:]
print('a',len(a))
print('b',len(b))
c=[]
for i in range(len(a)):
   for j in range(len(b)):
     c.append(a[i]*b[j])


for i in range(len(c)):
    m.write(str(c[i]))
    m.write("\n")
f.close()
k.close()
m.close()

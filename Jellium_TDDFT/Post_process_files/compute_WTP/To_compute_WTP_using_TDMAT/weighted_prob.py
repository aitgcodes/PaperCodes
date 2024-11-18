import itertools
import numpy as np


f = open('AB_weights.dat','r')
k = open('dmat.dat','r')
x=[]
y=[]
z=[]
for i in f:
    x.append(i)
for j in k:
    y.append(np.array(j.rsplit(),dtype="float64")[1:])
    z.append(np.array(j.rsplit(),dtype="float64"))
f.close()
k.close()
a=np.array(x,dtype="float64")
print(len(a))
b=np.array(y[3:])
ttime=np.array(z[3:])
time = ttime[:,0:1]
time=np.array(time,dtype="float64")
#print(time)

print(b.shape,len(b[0]))
c=np.einsum("i,ji->ji",a,b)
for i in range(len(c)):
    m = open("weighted_probab_{}.dat".format(i+1),"w")
    for v in c[i]: 
       m.write(str(v)+"\n")
    m.close()

ff = open('time.dat','w')
for i in range(len(time)):
   ff.write(str(np.asarray(time[i][0]))+"  "+"\n")
ff.close()

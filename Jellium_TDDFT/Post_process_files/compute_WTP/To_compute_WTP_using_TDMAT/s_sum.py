import sys



i = sys.argv[1]
add_sum = 0.0000000 
w = open("probabilty_sum","w")
for s in range(int(i)):
    m= open("weighted_probab_{}.dat".format(s+1),"r")
    add_sum = sum([float(k) for k in m])
    w.write(str(add_sum)+'\n')
w.close()

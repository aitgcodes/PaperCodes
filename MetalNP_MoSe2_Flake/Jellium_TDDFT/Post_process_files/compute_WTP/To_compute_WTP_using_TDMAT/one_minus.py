import csv
import numpy

f = open("Flake_weight_23_11.5.dat","r") 
lines = f.readlines()
data = open("Jellium_weight_23_11.5.dat","w")
for line in lines:
    nums = 1.0000
    my_row = []
    my_dummy = []
    one_myrow = []
    for s in line.strip().split()[1:2]:
       k = float(round(1.000000-float(s),7))
    data.write(str(k)+"\n")

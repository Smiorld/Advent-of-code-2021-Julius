import os
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))
filename=Path(script_dir,'d7-input.txt')
f = open(filename, "r")
data1=f.read()
data2=data1.split(',')
data3=[]
for i in data2:
    data3.append(int(i))

min=data3[0]
max=data3[0]
for i in data3:
    if i>max:
        max=i
    if i<min:
        min=i

cmin=9999999999999
for i in range(min,max+1):
    counter=0
    for j in data3:
        counter+=(abs(j-i)+1)*abs(j-i)/2
    if cmin>counter:
        cmin=counter
print(cmin)

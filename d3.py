# import os
# import unittest
# from pathlib import Path
# script_dir = os.path.dirname(os.path.abspath(__file__))
# filename=Path(script_dir,'d3-input.txt')
# f = open(filename, "r")
# data1=f.read()
# data2=data1.split('\n')
# print(data2)
# c0=[0,0,0,0,0,0,0,0,0,0,0,0]
# c1=[0,0,0,0,0,0,0,0,0,0,0,0]
# gamma=''
# epsilon=''
# for ind1,v1 in enumerate(data2):
#     for ind2,v2 in enumerate(v1):
#         if int(v2)==0:
#             c0[ind2]+=1
#         else:
#             c1[ind2]+=1
# for i,v in enumerate(c0):
#     if v>c1[i]:
#         gamma+='0'
#         epsilon+='1'
#     else:
#         gamma+='1'
#         epsilon+='0'
# print(gamma)
# print(epsilon)
# print(int(gamma,2)*int(epsilon,2))

import os
import unittest
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))
filename=Path(script_dir,'d3-input.txt')
f = open(filename, "r")
data1=f.read()
data2=data1.split('\n')
print(data2)



oxyrate=''
co2rate=''
index=0
while len(data2)>1 and index<len(data2[0]) :
    c0=0
    c1=0
    for i in data2:
        if int(i[index])==0:
            c0+=1
        else:
            c1+=1
    if c1>=c0:
        oxyrate+='1'
        data2=list(filter((lambda x: x[index] == '1'),data2))

    else:
        oxyrate+='0'
        data2=list(filter((lambda x: x[index] == '0'),data2))

    index+=1

while len(data2)==1 and index<len(data2[0]) :
    oxyrate+=data2[0][index]
    index+=1
print(oxyrate)

f = open(filename, "r")
data1=f.read()
data2=data1.split('\n')

index=0

while len(data2)>1 and index<len(data2[0]) :
    c0=0
    c1=0
    for i in data2:
        if int(i[index])==0:
            c0+=1
        else:
            c1+=1
    if c1>=c0:
        co2rate+='0'
        data2=list(filter((lambda x: x[index] == '0'),data2))

    else:
        co2rate+='1'
        data2=list(filter((lambda x: x[index] == '1'),data2))

    index+=1

while len(data2)==1 and index<len(data2[0]) :
    co2rate+=data2[0][index]
    index+=1
print(co2rate)
print(int(oxyrate,2)*int(co2rate,2))
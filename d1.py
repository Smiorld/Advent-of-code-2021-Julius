# import os
# import unittest
# from pathlib import Path
# script_dir = os.path.dirname(os.path.abspath(__file__))
# filename=Path(script_dir,'d1-input.txt')
# f = open(filename, "r")
# data1=f.read()
# data2=data1.split('\n')
# print(data2)
# res=0
# pre=0
# for i,v in enumerate(data2):
#     if i==0:
#         pre=int(v)
#         continue
#     if int(v)>pre:
#         res+=1
#     pre=int(v)
# print(res)

import os
import unittest
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))
filename=Path(script_dir,'d1-input.txt')
f = open(filename, "r")
data1=f.read()
data2=data1.split('\n')
res=0
a=0
b=0
c=0
for i,v in enumerate(data2):
    if i==0:
        a+=int(v)
        continue
    if i==1:
        a+=int(v)
        b+=int(v)
        continue
    if i==2:
        a+=int(v)
        b+=int(v)
        c+=int(v)
        continue
    b+=int(v)
    c+=int(v)
    if(b>a):
        res+=1
    a=b
    b=c
    c=int(v)
print(res)
    

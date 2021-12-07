import os
import unittest
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))
filename=Path(script_dir,'d2-input.txt')
f = open(filename, "r")
data1=f.read()
data2=data1.split('\n')
print(data2)

aim=0
x=0
d=0
def oprand(s,aim):
    # break s down to a oprand and a number  like 'forward','3'
    a=s.split(' ')
    if(a[0]=='forward'):
        return [int(a[1]),0,aim*int(a[1])]
    if(a[0]=='up'):
        return [0,0-int(a[1]),0]
    if(a[0]=='down'):
        return [0,int(a[1]),0]
for i,v in enumerate(data2):
    x+=oprand(v,aim)[0]
    aim+=oprand(v,aim)[1]
    d+=oprand(v,aim)[2]
print(x*d)
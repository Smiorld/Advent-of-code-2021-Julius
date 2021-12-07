import os
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))
filename=Path(script_dir,'d6-input.txt')
f = open(filename, "r")
data1=f.read()
data2=data1.split(',')
print(data2)
d0=data2.count('0')
d1=data2.count('1')
d2=data2.count('2')
d3=data2.count('3')
d4=data2.count('4')
d5=data2.count('5')
d6=data2.count('6')
d7=0
d8=0
new=0

days=0
while days<256:
    new=d0
    d0=d1
    d1=d2
    d2=d3
    d3=d4
    d4=d5
    d5=d6
    d6=d7
    d7=d8
    d6+=new
    d8=new
    days+=1
print(d0+d1+d2+d3+d4+d5+d6+d7+d8)
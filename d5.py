import os
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))
filename=Path(script_dir,'d5-input1.txt')
f = open(filename, "r")
data1=f.read()
data2=data1.split('\n')
data3=[]
for a in data2:
    b=a.split(' -> ')
    c=b[0].split(',')
    d=b[1].split(',')
    data3.append([c,d])

print(data3)
table=[ [0 for i in range(1000)]for j in range(1000)]



for l in data3:
    print(l)
    # only deal with horizontal and vetical lines
    if l[0][0]==l[1][0]:
        #a->b, a<=b
        if int(l[0][1])>=int(l[1][1]):
            a=l[1][1]
            b=l[0][1]
        else:
            a=l[0][1]
            b=l[1][1]
        for i in range(int(a),int(b)+1):
            table[i][int(l[0][0])]+=1
    elif l[0][1]==l[1][1]:
        if int(l[0][0])>=int(l[1][0]):
            a=l[1][0]
            b=l[0][0]
        else:
            a=l[0][0]
            b=l[1][0]
        for i in range(int(a),int(b)+1):
            table[int(l[0][1])][i]+=1
    else:# diagonal
        if int(l[0][0])<=int(l[1][0]) and int(l[0][1])<=int(l[1][1]):
            for i in range(int(l[1][0])-int(l[0][0])+1):
                table[int(l[0][1])+i][int(l[0][0])+i]+=1
        elif int(l[0][0])<=int(l[1][0]) and int(l[0][1])>int(l[1][1]):
            for i in range(int(l[1][0])-int(l[0][0])+1):
                table[int(l[0][1])-i][int(l[0][0])+i]+=1
        elif int(l[0][0])>int(l[1][0]) and int(l[0][1])<=int(l[1][1]):
            for i in range(int(l[0][0])-int(l[1][0])+1):
                table[int(l[0][1])+i][int(l[0][0])-i]+=1
        elif int(l[0][0])>int(l[1][0]) and int(l[0][1])>int(l[1][1]):
            for i in range(int(l[0][0])-int(l[1][0])+1):
                table[int(l[0][1])-i][int(l[0][0])-i]+=1
counter=0
for i in table:
    for j in i:
        if j>=2:
            counter+=1
print(counter)
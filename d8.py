import os
import re
from pathlib import Path
script_dir = os.path.dirname(os.path.abspath(__file__))
filename=Path(script_dir,'d8-input.txt')
f = open(filename, "r")
data1=f.read()
data2=re.split('\n| \| ', data1)

old2new_matching={
    'a':'z',
    'b':'z',
    'c':'z',
    'd':'z',
    'e':'z',
    'f':'z',
    'g':'z'
}
new2old_matching={
    'a':'z',
    'b':'z',
    'c':'z',
    'd':'z',
    'e':'z',
    'f':'z',
    'g':'z'
}
    

def decode(a,old2new_matching,new2old_matching):#decode the ten patterns, change the matching dictionary
    b=a.split(' ')
    n=[-1]*10
    #find 1,4,7,8, then find a 
    for i,v in enumerate(b):
        if len(v)==2:
            n[1]=v
        elif len(v)==4:
            n[4]=v
        elif len(v)==3:
            n[7]=v
        elif len(v)==7:
            n[8]=v
    for i in n[7]:
        if i not in n[1]:
            old2new_matching['a']=i
            new2old_matching[i]='a'
    
    counter={
        'a':0,
        'b':0,
        'c':0,
        'd':0,
        'e':0,
        'f':0,
        'g':0,
    }

    for i in b:
        for j in i:
            counter[j]+=1
        
    key = [key for key, value in counter.items() if value == 4] # find e
    old2new_matching['e']=key[0]
    new2old_matching[key[0]]='e'
    key = [key for key, value in counter.items() if value == 6] # find b
    old2new_matching['b']=key[0]
    new2old_matching[key[0]]='b'
    key = [key for key, value in counter.items() if value == 8] # find c, but need to except a
    for i in key:
        if i != old2new_matching['a']:
            old2new_matching['c']=i
            new2old_matching[i]='c'
    key = [key for key, value in counter.items() if value == 9] # find f
    old2new_matching['f']=key[0]
    new2old_matching[key[0]]='f'

    key = [key for key, value in counter.items() if value == 7] # find d,g . 4 contains d    1 contains neither d or g
    for i in key:
        if i in n[4] and i not in n[1]:
            old2new_matching['d']=i
            new2old_matching[i]='d'
        else:
            old2new_matching['g']=i
            new2old_matching[i]='g'

def find1478(a,counter):
    b=a.split(' ')
    for i in b:
        if len(i)==2 or len(i)==4 or len(i)==3 or len(i)==7:
            counter+=1
    return counter

def solve(a,new2old_matching):
    num={
    'abcefg':0,
    'cf':1,
    'acdeg':2,
    'acdfg':3,
    'bcdf':4,
    'abdfg':5,
    'abdefg':6,
    'acf':7,
    'abcdefg':8,
    'abcdfg':9
    }
    b=''
    for i in a:
        if i!=' ':
            b+=new2old_matching[i]
        else:
            b+=' '
    b=b.split(' ')
    counter=0
    for i in b:
        counter=counter*10+num[''.join(sorted(i))]
    return counter




counter=0
for i,v in enumerate(data2):
    if i%2==0:
        decode(v,old2new_matching,new2old_matching)
    else:
        # counter=find1478(v,counter)
        counter+=solve(v,new2old_matching)
print(counter)
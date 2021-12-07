import os
from pathlib import Path

def list_split(listA): # split data2 to a list of list
    for x in range(0, len(listA), 6):
        # every_chunk = listA[x+1: 6+x]
        every_chunk=[]
        for y in range(1,6):
            tmp=listA[x+y].split(' ')
            every_chunk.append(list(filter(lambda z: z!='',tmp )) )
        
        
        yield every_chunk

def make_marker(a,bingo,marker,marker_counter):#change marker and counter
    for i1,t in enumerate(bingo):
        for i2,y in enumerate(t):
            for i3,x in enumerate(y):
                if int(x)==a:
                    marker[i1][i2][i3]=1
                    marker_counter[i1][0][i2]+=1
                    marker_counter[i1][1][i3]+=1

def check_bingo(marker_counter): #check whether winner exist, return winner statement, and winner table index
    #check the table
    for i1,t in enumerate(marker_counter):
        if t[0].count(5):
            return (True,i1)
        if t[1].count(5):
            return (True,i1)
    return (False,-1)





script_dir = os.path.dirname(os.path.abspath(__file__))
filename=Path(script_dir,'d4-input2.txt')
f = open(filename, "r")
data1=f.read()
data2=data1.split('\n')

filename=Path(script_dir,'d4-input1.txt')
f = open(filename, "r")
data3=f.read()
data4=data3.split(',')


bingo=list(list_split(data2))
print(bingo)
# bingo[1][2][3]   1 is table, 2 is y, 3 is x
marker=[]
# same amount of elements as bingo, with all value 0
marker_counter=[]
# counter for every table in marker.
for x in range(len(bingo)):
    marker_1=[]
    marker_counter.append([ [0 for m in range(5)],[0 for m in range(5)] ])
    for y in range(len(bingo[0])):
        marker_2=[0 for z in range(len(bingo[0][0]))]
        marker_1.append(marker_2)
    marker.append(marker_1)



win_num=0
for a in data4:
    make_marker(int(a),bingo,marker,marker_counter)
    winner_state=check_bingo(marker_counter)
    if winner_state[0]:
        win_num=int(a)
        break

counter=0
for i1,y in enumerate(marker[winner_state[1]]):
    for i2,x in enumerate(y):
        if x==0:
            counter+=int(bingo[winner_state[1]][i1][i2])

print(counter*win_num)





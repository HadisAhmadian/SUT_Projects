import numpy as np
from operator import itemgetter
global node_num
global height
global edges
global D
global clusters



f = open("a.txt", "r")
t=f.readline()
t=t.replace("\n", "")
n=int(t)
a=[]

while t!="":
    t=f.readline()
    c=t.split()
    if t=="":
        break
    c=[int(element) for element in c]
    a.append(c)
    height.append(0)


node_num=[i for i in range(n)]
height=[0 for i in range(n)]
edges=[]
D=[list(x) for x in a]
clusters={0:[0]}
for i in range(n):
    clusters[i] = [i]



#----------------------------------------------------------------------------------------
def choose_node(a):
    min_all=a[0][1]
    I=0
    J=1
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j]<min_all and a[i][j]!=0:
                min_all =a[i][j]
                I=i
                J=j
    return (min_all,I,J)

def distance_cal(i,num):
    s=0
    for x in clusters[i]:
        for y in clusters[num]:
            s+=D[x][y]
            
    return(s/(len(clusters[i])*len(clusters[num])))
    


def add_new_cluster(I,J,num):
    clusters[num] = clusters[I]+clusters[J]
    
    
def new_cluster(info,a,i):
    I=info[1]
    J=info[2]
    tmp=[]
    h=info[0]/2
    height.append(h)
    #print(height)
    node_num.append(n+i)
    edges.append((n+i,node_num[I],h-height[node_num[I]]))
    edges.append((n+i,node_num[J],h-height[node_num[J]]))
    
    add_new_cluster(node_num[I],node_num[J],n+i)
    #print(clusters)
    node_num.pop(max(I,J))
    node_num.pop(min(I,J))
    
    
    for k in range(len(node_num)-1):
        tmp.append(distance_cal(node_num[k],n+i))
        
    tmp.append(0)
    
    #make new matrix
    a.pop(max(I,J))
    a.pop(min(I,J))
    for x in a:
        x.pop(max(I,J))
        x.pop(min(I,J))
        
    for i in range(len(a)):
        a[i].append(tmp[i])
    
    a.append(tmp)
    
    
def print_by_format():
    
    for x in edges:
        print(str(x[0])+"->"+str(x[1])+str(":")+str('%.3f'%x[2]))
    
#------------------------------------------------------------------------
i=0

while(len(a)>1):
    new_cluster(choose_node(a),a,i)
    i+=1
tmp=[]
for x in edges:
    tmp.append((x[1],x[0],x[2]))
edges=edges+tmp
edges=sorted(edges,key=itemgetter(0))  
print_by_format()
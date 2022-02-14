global node_num

from operator import itemgetter
f = open("a.txt", "r")
t=f.readline()
t=t.replace("\n", "")
n=int(t)
a=[]
node_num=[i for i in range(n)]
while t!="":
    t=f.readline()
    c=t.split()
    if t=="":
        break
    c=[int(element) for element in c]
    a.append(c)

def Dtotal(D,i,n):
    s=0
    for j in range(n):
        s+=D[i][j]
    return s

def NJ_matrix(D,n):
    Dt=[Dtotal(D,i,n) for i in range(n)]
    NJm=[[0]*n for _ in range(n)]
    m=9999999
    I=J=0
    for i in range(n):
        for j in range(n):
            NJm[i][j]=(n-2)*(D[i][j])-Dt[i]-Dt[j]
            if i!=j and m>NJm[i][j]:
                m=NJm[i][j]
                I=i
                J=j
    return NJm,Dt,I,J

def add_new(D,n,I,J):
    tmp=[]
    for k in range(n):
        if k!=I and k!=J:
            tmp.append((D[k][I]+D[k][J]-D[I][J])/2)
    D.pop(max(I,J))
    D.pop(min(I,J))
    for x in D:
        x.pop(max(I,J))
        x.pop(min(I,J))
    for k in range(len(D)):
        D[k].append(tmp[k])
    tmp.append(0)
    D.append(tmp)


def NeighborJoining(D,n,node_num):
   
    if n==2:
        x=node_num[0]
        y=node_num[1]
        T={x:{y:D[0][1]},y:{x:D[1][0]}}
        return T
    
    NJm,Dt,I,J=NJ_matrix(D,n)
    delta=(Dt[I]-Dt[J])/(n-2)
    Li=(D[I][J]+delta)/2
    Lj=(D[I][J]-delta)/2
    
    add_new(D,n,I,J)
    IJ=[node_num[I],node_num[J]]
    
    v=node_num[len(node_num)-1]+1
    node_num.pop(max(I,J))
    node_num.pop(min(I,J))
    
    node_num.append(v)
    T=NeighborJoining(D,n-1,node_num[:])

    k=[key for key in T]
    
    
    if v not in T:
        T[v]={IJ[0]:Li , IJ[1]:Lj}
    else:
        T[v][IJ[0]]=Li
        T[v][IJ[1]]=Lj
    
    if IJ[0] not in T:
        T[IJ[0]]={v:Li}
    else:
        T[IJ[0]][v]=Li
        
    if IJ[1] not in T:
        T[IJ[1]]={v:Lj}
    else:
        T[IJ[1]][v]=Lj
   
    
    return T


def print_(T,k,tmp):
    for key in T:
        tmp.append((k,key,T[key]))

def print_by_res(T):
    tmp=[]
    for key in T:
        print_(T[key],key,tmp)
    return tmp


def print_by_format(edges):
    for x in edges:
        print(str(x[0])+"->"+str(x[1])+str(":")+str('%.3f'%x[2]))


edges=(print_by_res(NeighborJoining(a,n,node_num)))
edges=sorted(edges,key=itemgetter(0))  
print_by_format(edges)
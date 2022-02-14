from operator import itemgetter
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

def limb(a,n):
    y=99999999
    J=K=0
    i=n
    n+=1
    for j in range(n):
        for k in range(n):
            if j==k or i==k or j==i:
                continue
            x=a[i][k]+a[i][j]-a[j][k]
            x=x/2
            if x<y:
                y=x
                J=j
                K=k
                
    return y

def find_nodes(D,n):
    for i in range(n-1):
        for k in range(n-1):
            if D[i][k]==D[i][n-1]+D[n-1][k]:
                return (i,k)
        
def path_ret(i,k,T,visited,path,p):
    visited[i]=True
    path.append(i)
    if i == k:
        p.append(path[:])        
        
    else:
        for key in T[i]:
            if visited[key]== False:
                path_ret(key, k,T, visited, path,p)
    path.pop()
    visited[i]=False
    




    

def find_place(x,i,k,T,C):
    path=[]
    path_ret(i,k,T,[False for i in range(C[0])],[],path)
    path=path[0]
    s=0
    for j in range(len(path)-1):
        s+=T[path[j]][path[j+1]]
        if s == x:
            v=path[j+1]
            return T,v
        elif s>x:
            v=C[0]
            C[0]+=1
            Len=T[path[j]][path[j+1]]
            x=s-x
            y=Len-x
            T[path[j]].pop(path[j+1])
            T[path[j+1]].pop(path[j])
            T[path[j]][v]=y
            T[path[j+1]][v]=x
            T[v]= {path[j]:y , path[j+1]:x}
            return T,v
        
    
    
    
    
    


def addative_ph(D,n):
    
    if n==2:
        T={0:{1:D[0][1]},1:{0:D[1][0]}}
        return T
        
    
    l=limb(D,n-1)
    for i in range(n-1):
        D[i][n-1]-=l
        D[n-1][i]=D[i][n-1]
    (i,k)=find_nodes(D,n)
    x=D[i][n-1]
    T=addative_ph(D,n-1)
    T,v=find_place(x,i,k,T,C)
    T[v][n-1]=l
    T[n-1]={v:l}
    return T


def print_(T,k,tmp):
    for key in T:
        tmp.append((k,key,int(T[key])))

def print_by_res(T):
    tmp=[]
    for key in T:
        print_(T[key],key,tmp)
    return tmp


def print_by_format(edges):
    for x in edges:
        print(str(x[0])+"->"+str(x[1])+str(":")+str(x[2]))


global C
C=[n]

edges=print_by_res(addative_ph(a,n))
edges=sorted(edges,key=itemgetter(0))  
print_by_format(edges)
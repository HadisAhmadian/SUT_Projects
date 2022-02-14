from math import log
def convert(s):
    s=reversed(s)
    new = ""
    for x in s:
        new += x 
    return new


f = open("a.txt", "r")
t=f.readline()
emision=t.replace("\n", "")
emision=list(emision)
n=len(emision)
#print(emision)
t=f.readline()

t=f.readline()
alph=t.split()
A=len(alph)
#print(alph)
t=f.readline()

t=f.readline()
states=t.split()
Q=len(states)
#print(states)

T=[]
t=f.readline()
t=f.readline()
for i in range(Q):
    t=f.readline()
    t=t.split()
    t=t[1:]
    t=[float(x) for x in t]
    T.append(t)
    

E=[]
t=f.readline()
t=f.readline()
for i in range(Q):
    t=f.readline()
    t=t.split()
    t=t[1:]
    t=[float(x) for x in t]
    d={}
    for j in range(A):
        d[alph[j]]=t[j]
    E.append(d)


viterbi=[[0]*n for i in range(Q)]
res=[[0]*n for i in range(Q)]

for i in range(n):
    for j in range(Q):
        m=-9999
        Km=0
        if i==0:
            viterbi[j][i]=log(E[j][emision[i]])
            continue
        for k in range(Q):
            x=log(T[k][j])+viterbi[k][i-1]
            if x>m:
                Km=k
                m=x
        
        viterbi[j][i]=m+log(E[j][emision[i]])
        res[j][i]=Km
p=[]
i=n-1
tmp=[viterbi[j][i] for j in range(Q)]
f=tmp.index(max(tmp))
p.append(states[f])
while i!=0:
    f=res[f][i]
    p.append(states[f])
    i-=1
    
print(convert(p))
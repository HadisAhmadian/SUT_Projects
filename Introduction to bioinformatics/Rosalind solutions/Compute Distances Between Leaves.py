MAX=9999999
f = open("a.txt", "r")
t=f.readline()
t=t.replace("\n", "")
N=int(t)
n=2*N-1
X=[[MAX]*n for _ in range(n)]
while t!="":
    t=f.readline()
    t=t.replace("\n", "")
    i=0
    a=""
    if t=="":
        break
    while t[i]!="-":
        a+=t[i]
        i+=1
    fr=int(a) #from
    i+=2
    a=""
    while t[i]!=":":
        a+=t[i]
        i+=1
    i+=1
    to=int(a) #from
    a=t[i:]
    w=int(a)#weight
    
    
    X[fr][to]=w
    X[to][fr]=w

#---------------------------------

for k in range(n):
        for i in range(n):
            for j in range(n):
                if i==j:
                    X[i][j]=0
                    continue
                X[i][j] = min(X[i][j],X[i][k] + X[k][j])
                
for i in range(N):
    s=""
    for j in X[i][:N]:
        s+=str(j)
        s+=" "
    print(s)
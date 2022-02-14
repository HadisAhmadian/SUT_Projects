f = open("a.txt", "r")
t=f.readline()
t=t.replace("\n", "")
n=int(t)
t=f.readline()
t=t.replace("\n", "")
J=int(t)
a=[]
while t!="":
    t=f.readline()
    c=t.split()
    if t=="":
        break
    c=[int(element) for element in c]
    a.append(c)

y=99999999
i=J
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


            
print(int(y))
f = open("a.txt", "r")
t=f.readline()
t=t.replace("\n", "")
k=int(t)
dna_all=[]

while t!="":
    t=f.readline()
    t=t.replace("\n", "")
    t=t.replace(" ", "")
    if t=="":
        break
    dna_all.append(t)

units=['A','T','C','G']

def nth_string(units,n,k):
    s=""
    for i in range(k):
        s+='A'
    i=k-1
    while n>0:
        r=n%4
        s = s[:i] + units[r] + s[i+1:]
        n=n/4
        n=int(n)
        i-=1
    return s

def make_all_strings(strings,units,k):
    
    for n in range(4**k):
        strings.append(nth_string(units,n,k))
        
def hamming(a,b):
    A=list(a)
    B=list(b)
    c=0
    for i in range(len(A)):
        if A[i]!=B[i]:
            c+=1
    return c

def d(p,dna):
    k=len(p)
    n=len(dna)
    I=n-k+1
    s=9999
    for i in range(I):
        new=hamming(p,dna[i:i+k])
        if new<s:
            s=new
    return s

strings=[]
make_all_strings(strings,units,k)

d_value=[]
for S in strings:
    d_tmp=0
    for D in dna_all:
        d_tmp+=d(S,D)
    d_value.append(d_tmp)


i=d_value.index(min(d_value))
print(strings[i])
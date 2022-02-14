dna=[]
f = open("a.txt", "r")
l=f.readline()
l=l.split(" ")
k=int(l[0])
t=int(l[1])
for _ in range(t):
    l=f.readline()
    l=l.replace("\n","")
    dna.append(l)


index={
    "A":0,
    "C":1,
    "T":2,
    "G":3
}

    

def score(profile):
    sum_all=0
    sum_max=0
    all_max=[0]*len(profile[0])
    for x in profile:
        for i in range(len(x)):
            sum_all+=x[i]
            if x[i]>all_max[i]:
                all_max[i]=x[i]
        
    for m in all_max:
        sum_max+=m
            
    #print(profile,sum_all,sum_max)
    return sum_all-sum_max


def make_profile(motifs,k):
    t=len(motifs)
    #print(motifs)
    
    prof=[[0]*k for _ in range(4)]
    for i in range(t):
        j=0
        for nuc in motifs[i]:
            prof[index[nuc]][j]+=1
            j+=1
    return prof


def find_best(prof_p,s):
    n=len(s)
    k=len(prof_p[0])
    sc=0
    motif=s[0:k]
    for i in range(n-k+1): 
        m=list(s[i:i+k])
        tmp=1
        for j in range(k):
            tmp*=prof_p[index[m[j]]][j]
        if tmp>sc:
            sc=tmp
            motif=s[i:i+k]
    #print(motif)
    return motif
            
        


n=len(dna[0])
best_motifs =[x[0:k] for x in dna]
best_score=score(make_profile(best_motifs,k))
#print(motifs)

for i in range(n-k+1):
    #print(dna[0][i:i+k])
    motifs=[]
    motifs.append(dna[0][i:i+k])
    for j in range(1,t):
        prof=make_profile(motifs,k)
        prof_p=[]
        for x in prof:
            tp=[(y+1)/(j+4) for y in x]
            prof_p.append(tp)
        motifs.append(find_best(prof_p,dna[j]))
        
    prof=make_profile(motifs,k)
    ts=score(prof)
    if ts<best_score:
        best_score=ts
        best_motifs=motifs
 
for x in best_motifs:   
    print(x)
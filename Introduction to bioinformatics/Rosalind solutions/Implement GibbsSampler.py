from random import randrange,choices
dna=[]
f = open("a.txt", "r")
l=f.readline()
l=l.split(" ")
k=int(l[0])
t=int(l[1])
N=int(l[2])
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


def randomize_motifs(dna,k,t):
    n=len(dna[0])
    num=n-k+1
    motifs=[]
    for i in range(t):
        j=(randrange(num))
        motifs.append(dna[i][j:j+k])
    return motifs
    
    
def index_i(p,s,k):
    prob=[]
    for i in range(len(s)-k+1):
        tmp=1
        ss=list(s[i:i+k])
        j=0
        for nuc in ss:
            tmp*=p[index[nuc]][j]
            j+=1
        prob.append(tmp)
    #print((list(range(0, len(s) - k + 1)), prob))
    return choices(list(range(len(s)-k+1)), prob)

    
    
    
    
def gibbs(dna,k,t,N):
    n=len(dna[0])
    best_motifs=randomize_motifs(dna,k,t)
    prof=make_profile(best_motifs,k)
    min_score=score(prof)
    motifs=best_motifs[:]
    for _ in range(N):
        
        i=(randrange(t))
        motifs.pop(i)
        #print(i)
        #print(motifs)
        p_first=make_profile(motifs,k)
        p=[]
        for x in p_first:
            tp=[(y+1)/(t-1+4) for y in x]
            p.append(tp)
        
        i_kmer=index_i(p,dna[i],k)[0]
        motifs.insert(i,dna[i][i_kmer:i_kmer+k])
        #print(motifs)
        prof=make_profile(motifs,k)
        s=score(prof)
        if s<min_score:
            min_score=s
            best_motifs=motifs[:]
       
        
    return best_motifs
        

best_motifs=gibbs(dna,k,t,N)
prof=make_profile(best_motifs,k)
min_score=score(prof)
for _ in range(19):
    motifs=gibbs(dna,k,t,N)
    prof=make_profile(motifs,k)
    s=score(prof)
    if s<min_score:
        best_motifs=motifs[:]
        min_score=s

for x in best_motifs:   
    print(x)
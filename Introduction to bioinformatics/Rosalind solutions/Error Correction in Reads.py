# add a ">" at the end of input file to test this code
reverse_nucleotide= {
        'A': 'T',
        'G': 'C',
        'T': 'A',
        'C': 'G'
    }

def rev(a):
    b=a[::-1]
    c=""
    for i in range(len(b)):
        c+=reverse_nucleotide[b[i]]
    return c


def ham(a,b):
    c=0
    for i in range(len(a)):
        if a[i]!=b[i]:
            c+=1
    return c

f = open("a.txt", "r")
all_input=[]
counts=[]
tmp=""
t=" "
c=0
while len(t)>0:
    t=f.readline()
    if c==0:
        c=1
        continue
    if len(t)>0 and t[0]==">":
        tmp=tmp.replace("\n", "")
        if all_input.count(tmp)!=0 :
            counts[all_input.index(tmp)]+=1
        elif all_input.count(rev(tmp))!=0:
            counts[all_input.index(rev(tmp))]+=1
        else :
            all_input.append(tmp)
            counts.append(1)
        tmp=""
        
    else:
        tmp+=t
        


for i in range(len(counts)):
    if counts[i]==1:
        for j in range(len(counts)):
            if counts[j]!=1:
                a=ham(all_input[i],all_input[j])
                if a==1:
                    print(all_input[i]+"->"+all_input[j])
                    break;
                b=ham(all_input[i],rev(all_input[j]))
                if b==1:
                    print(all_input[i]+"->"+rev(all_input[j]))
                    break;
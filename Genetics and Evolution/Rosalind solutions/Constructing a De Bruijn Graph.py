set_of_nodes=set()
set_of_edges=set()
reverse_nucleotide= {
        'A': 'T',
        'G': 'C',
        'T': 'A',
        'C': 'G'
    }


f = open("a.txt", "r")
t=f.readline()
t=t.replace("\n", "")
while t!="":
    set_of_nodes.add((t.strip(" ")))
    t_r=""
    for i in range(len(t)):
        t_r+=reverse_nucleotide[t[i]]
    set_of_nodes.add((t_r[::-1].strip(" ")))
    t=f.readline()
    t=t.replace("\n", "")



    
for x in set_of_nodes:
    k=len(x)
    set_of_edges.add("("+x[:k-1]+", "+x[1:]+")")

for x in set_of_edges:
    print(x)
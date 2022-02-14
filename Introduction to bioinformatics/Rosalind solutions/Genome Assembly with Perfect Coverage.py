set_of_edges=set()

f = open("a.txt", "r")
t=f.readline()
t=t.replace("\n", "")


k=len(t)

while t!="":
    set_of_edges.add((t[:k-1], t[1:]))
    t=f.readline()
    t=t.replace("\n", "")
res=""
set_of_edges=list(set_of_edges)
new_edge=set_of_edges[0]
del(set_of_edges[0])

res+=new_edge[0]
res+=new_edge[1][-1]


while len(set_of_edges)>k-1:
    for i in range(len(set_of_edges)):
        if set_of_edges[i][0]==new_edge[1]:
            new_edge=set_of_edges[i]
            del(set_of_edges[i])
            res+=new_edge[1][-1]
            break
        

    
print(res)
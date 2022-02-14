def convert(s):
  
    s=reversed(s)
    new = ""
    for x in s:
        new += x 
    return new

f = open("a.txt", "r")
t=" "
c=0
while t!="":
    t=f.readline()
    if t!="" and t[0]==">" and c==0:
        a=""
        c+=1
        continue
        
    if t!="" and t[0]==">" and c==1:
        b=""
        c+=1
        continue
        
    if c==1:
        a+=t
        
    if c==2:
        b+=t
        
a=a.replace("\n", "")
b=b.replace("\n", "")     



al=len(a)
bl=len(b)


list_a = list(a.strip(" "))
list_b = list(b.strip(" "))


value=[]
tmp=[]
flag=[]


for i in range(bl+1):
    tmp.append(0)
value.append(tmp)
tmp=[0]

for i in range(al+1):
    tmp=[]
    for j in range(bl+1):
        
        if i==0 or j==0:
            tmp.append(0)
            continue

        if list_a[i-1] == list_b[j-1]:
            m=(value[i-1][j-1]+1)
        else:
            m=(max(value[i-1][j], tmp[j-1], value[i-1][j-1])-1)
            
        tmp.append(m)
        

    if(i>0):
        value.append(tmp)
        
        
score=-999999
for i in range(al):
    if value[i][bl]>score:
        score=value[i][bl]
        i1=i
    
    
print(score)
    
#-------------------------------------------------------------------------------------------------------   
    

i=i1
j=bl
aa=[]
bb=[]

while i > 0 and j > 0:

        if list_a[i-1] == list_b[j-1]:
            aa.append(list_a[i-1])
            bb.append(list_b[j-1])
            i=i-1
            j=j-1
            continue

        m=(max(value[i-1][j] , value[i][j-1], value[i-1][j-1]))
        
        if value[i-1][j-1] ==m:
            aa.append(list_a[i-1])
            bb.append(list_b[j-1])
            i=i-1
            j=j-1
        

        elif value[i][j-1] ==m:
            bb.append(list_b[j-1])
            aa.append("-")
            j=j-1    
            
        elif value[i-1][j]==m:
            aa.append(list_a[i-1])
            bb.append("-")
            i=i-1    
        


print(convert(aa))
print(convert(bb))
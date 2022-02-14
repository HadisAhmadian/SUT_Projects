f = open("a.txt", "r")
t=f.readline()
t=t.replace("\n", "")
a=[]
sum_all=0
while t!="":
    x=len(t)
    a.append(x)
    sum_all+=x
    t=f.readline()
    t=t.replace("\n", "")
a.sort()


#---------------------------------
def N50(a,sum_all):
    x=sum_all*(0.5)
    my_sum=0
    c=0
    for num in a:
        my_sum+=num
        c+=1
        if my_sum>x:
            return (a[c-1])
        
#---------------------------------
def N75(a,sum_all):
    x=sum_all*(0.75)
    my_sum=0
    c=0
    for num in a:
        my_sum+=num
        c+=1
        if my_sum>x:
            return (a[c-1])
        
print(str(N50(a[::-1],sum_all))+" "+str(N75(a[::-1],sum_all)))
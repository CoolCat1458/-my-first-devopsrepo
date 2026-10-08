x=[0,1,2,3,4,5,6,7,8,9]
l1=[]
l2=[]
lir3=[]
for i in x[0:len(x)-1:2]:
    l1.append(x[i])
l1.reverse()
for k in x[1:len(x):2]:
    l2.append(x[k])
for s in range(0,len(l1)):
    lir3.append(l1[s])
    lir3.append(l2[s])
print(lir3)
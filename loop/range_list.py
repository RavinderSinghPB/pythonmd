l=[1,2,3,3,3]


idx = [0,1,2,3,4]
for i in idx:
    l[i]=1

print(l)

#######################################################
l=[1,2,3,3,3]
print(l)

# idx = [0,1,2,3,4] ==> range(5) ==> range(len(l))
for i in range(len(l)):
    l[i]=1
    
print(l)
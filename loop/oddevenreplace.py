l = [12,24,36,4,5,67,8,96]
print(l)

for idx in range(len(l)):
    if l[idx]%2==0:
        l[idx]='e'
    else:
        l[idx]="o"

print(l)
    
    
inp = input("use space bw no : ")
nl = inp.split(" ")

print(nl)

# nl[0]=int(nl[0])
# nl[1] = int(nl[1])

for idx in range(len(nl)):
    nl[idx]=int(nl[idx])

sm =sum(nl)

print(sm)


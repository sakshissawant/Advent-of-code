file = open("input.txt", "r")

add = 0
count=0
i=0

for n in file:
    if n=='\n':
        if add > count:
            count = add
   
        i+=1
        add=0
        continue

    add += int(n)
    
print(count)
print(i)

file = open('3/input','r')
strings = file.readlines() #strings is a list

#print(strings)
both=[]

for i in range(len(strings)):
    half = int((len(strings[i])-1)/2)
    count=0
    for j in range(half):
        for k in range(half):
            if strings[i][j] == strings[i][k+half]:
                count+=1
                if count==1:
                    #print(strings[i][j])
                    both.append(strings[i][j])
                
#print(both)

values = {}

for n in range(26):
    char = chr(ord('a')+n)
    Number =ord('a')+n - 96
    #print(char + " " + str(Number))
    new = {char : Number}
    values.update(new)

for N in range(26):
    chars = chr(ord('A')+N)
    Numbers =ord('A')+N -38
    #print(chars + " " + str(Numbers))
    new = {chars : Numbers}
    values.update(new)

addition=0
for add in both:
    addition += values[add]
    
print(addition)
    

file = open("2",'r')

values = {
    "A X\n" : 4,
    "A Y\n" : 8,
    "A Z\n" : 3,
    "B X\n" : 1,
    "B Y\n" : 5,
    "B Z\n" : 9,
    "C X\n" : 7,
    "C Y\n" : 2,
    "C Z\n" : 6
}

addition = 0
for N in file:
    if N == "\n":
        continue
    addition += values[N]

print(addition)

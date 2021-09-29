# Bubble sorting
# Compare j and j+1

numArray = [4,5,6,3,2,1]

for i in range(1, len(numArray)):
    for j in range(0, len(numArray) - i):
        if numArray[j] > numArray[j+1]:
            temp=numArray[j]
            numArray[j]=numArray[j+1]
            numArray[j+1] = temp

print(numArray)


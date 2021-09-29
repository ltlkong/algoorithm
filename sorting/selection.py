# Selection sort

numArray = [4,5,6,3,2,1]

for i in range(0, len(numArray)):
    min = i
    for j in range(i+1, len(numArray)):
        if numArray[min] > numArray[j]:
            min = j

    temp = numArray[i]
    numArray[i]=numArray[min]
    numArray[min]=temp

print(numArray)

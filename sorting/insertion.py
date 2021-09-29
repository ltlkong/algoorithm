# Insertion sort

numArray = [4, 5, 6, 3, 2, 1]

for i in range(1, len(numArray)):
    tmp = numArray[i]
    j = i-1
    while j >= 0 and numArray[j] > tmp:
        numArray[j+1] = numArray[j]
        j -= 1
    numArray[j+1] = tmp


print(numArray)

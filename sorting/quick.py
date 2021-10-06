# Quick sort
numarray = [8, 23, 10,  1,  9, 25,  3, 19,  5,  4]

numArray2 = [4, 5, 6, 3, 2, 1]


def partition(data, left, right):
    tmp = data[left]
    isRight = True
    mid = 0

    while left < right:
        if isRight:
            if data[right] < tmp:
                swp = data[right]
                data[right] = data[left]
                data[right] = swp
                isRight = False
                left += 1
            else:
                right -= 1
        else:
            if data[left] < tmp:
                swp = data[left]
                data[left] = data[right]
                data[right] = swp
                isRight = True
                right -= 1
            else:
                left += 1
        mid = left-1

    return mid


print(partition(numArray2, 0, 5))

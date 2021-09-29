numArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def search(array, num):
    start = 0
    end = len(numArray)

    while start < end:
        mid = (start+end)//2
        if array[mid] == num:
            return mid
        if array[mid] > num:
            end = mid-1
        if array[mid] < num:
            start = mid+1


print(search(numArray, 10))

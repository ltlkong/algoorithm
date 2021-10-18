# 4. Median Of Two Sorted Array

17 Oct

## My tries:

**(Wrong)** My solution (Incorrect time complexty):

Merge two arrays:

    mid = (len(nums1) + len(nums2)) // 2
    isOdd = (len(nums1) + len(nums2)) % 2 > 0
    merge = []
    p1 = p2 = 0

    while p1 + p2 <= mid and p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] < nums2[p2]:
        merge.append(nums1[p1])
        p1 += 1
        else:
        merge.append(nums2[p2])
        p2 += 1

    while p1 + p2 <= mid and p1 < len(nums1):
        merge.append(nums1[p1])
        p1 += 1

    while p1 + p2 <= mid and p2 < len(nums2):
        merge.append(nums2[p2])
        p2 += 1

    if isOdd:
        return merge[-1]
    else:
        return round((merge[-1] + merge[-2]) / 2, 1)
    
Time complexity O((m + n) / 2)

Steps:

1. Calculate middle of the two arrays
2. Merge two arrays until reach the middle
3. if two arrays length sum is odd return the middle, otherwise return (middle + middle - 1) /2

## Viewed answere:

Using partions:

    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1


    l, r = 0, len(nums1) - 1
    half = (len(nums1) + len(nums2)) // 2


    while True:
        mid =  (l + r) // 2
        midB = half - mid - 2

        aL = nums1[mid] if mid >= 0 else float("-infinity")
        aR = nums1[mid + 1] if mid + 1 < len(nums1) else float("infinity")
        bL = nums2[midB] if midB >= 0 else float("-infinity")
        bR = nums2[midB + 1] if midB + 1 < len(nums2) else float("infinity")

        if aL <= bR and bL <= aR:
            if (len(nums1) + len(nums2)) % 2:
                return min(aR, bR)
            else:
                return round((max(aL, bL) + min(bR, aR)) / 2,1)
        elif aL > bR:
            r = mid - 1
        else:
            l = mid + 1
            
Time complexity Olog(m+n)

Steps:

1. Calculate middle of the two arrays
2. Separate the two arrays from middle using binary search
3 Return 

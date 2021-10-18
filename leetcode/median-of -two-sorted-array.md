# 4. Median Of Two Sorted Array

17 Oct

## My tries:
**(Wrong)** My solution (Incorrect time complexty):
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
2. Declare a merged array, merge two array until reach middle
3. if two arrays length sum is odd return the middle, otherwise return (middle + middle - 1) /2

## Viewed answere:
Using Stack

     maxArea = 0
            stack = [-1]
            heights.append(-2)
        
            for i in range(len(heights)):
                while heights[i] < heights[stack[-1]] and stack[-1] > -1:
                    numI = stack.pop()
                    area = (i - stack[-1] - 1) * heights[numI]
                    maxArea = max(area, maxArea)
                stack.append(i)
                   
            return maxArea
            
Time complexity On

Steps:
1. Defind a stack
2. Loop the list
3. Append the stack when the index numbergreater than the top stack, pop stack when the index number smaller.


# 84. Largest Rectangle In Histogram

10 Oct

## My tries:
**(Failed)** My solution (Time Limit Exceeded):
   
        cur = 0
        maxArea = 0
        
        while cur < len(heights):
            left = right = cur
            while left > 0 and heights[left-1] >= heights[cur]:
                left -= 1
            while right < len(heights)-1 and heights[right+1] >= heights[cur]:
                right += 1
                
            area = heights[cur]* (right - left + 1)
            if area > maxArea:
                maxArea = area
            cur += 1
        
        return maxArea
        
Time complexity On^2

Steps:
1. Set a pointer point to the current number
2. Set two pointers move to the left and the right of current number,  stop the left right pointer until they reach a number smaller than the current.
3. Calculate the area and compare to the maxArea.
4. Repeat 1-3 steps unitil current number reach to the end.

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



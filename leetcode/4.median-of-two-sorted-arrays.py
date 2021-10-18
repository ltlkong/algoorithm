#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
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
                

        
# @lc code=end


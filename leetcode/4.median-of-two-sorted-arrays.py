#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
      mid = (len(nums1) + len(nums2)) // 2
      isOdd = (len(nums1) + len(nums2)) % 2 > 0
      merge = []
      p1 = p2 = 0

      # Merge two lists to mid
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
            
# @lc code=end


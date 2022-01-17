#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#
# https://leetcode-cn.com/problems/4sum-ii/description/
#
# algorithms
# Medium (60.68%)
# Likes:    462
# Dislikes: 0
# Total Accepted:    87.1K
# Total Submissions: 143.3K
# Testcase Example:  '[1,2]\n[-2,-1]\n[-1,2]\n[0,2]'
#
# 给你四个整数数组 nums1、nums2、nums3 和 nums4 ，数组长度都是 n ，请你计算有多少个元组 (i, j, k, l)
# 能满足：
# 
# 
# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
# 输出：2
# 解释：
# 两个元组如下：
# 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) +
# (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) +
# (-1) + 0 = 0
# 
# 
# 示例 2：
# 
# 
# 输入：nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# n == nums1.length
# n == nums2.length
# n == nums3.length
# n == nums4.length
# 1 <= n <= 200
# -2^28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^28
# 
# 
#

# @lc code=start
from collections import Counter


class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        counter = Counter()
        result = 0

        for n3 in nums3:
            for n4 in nums4:
                counter[n3 + n4] += 1

        for n1 in nums1:
            for n2 in nums2:
                t = -n1 - n2
                if t in counter:
                    result += counter[t]

        return result
# @lc code=end

s = Solution()
print(s.fourSumCount(nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]))
print(s.fourSumCount(nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]))
print(s.fourSumCount([0,1,-1], [-1,1,0], [0,0,1], [-1,1,1])) # 17

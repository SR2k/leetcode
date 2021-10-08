#
# @lc app=leetcode.cn id=1726 lang=python3
#
# [1726] 同积元组
#
# https://leetcode-cn.com/problems/tuple-with-same-product/description/
#
# algorithms
# Medium (47.72%)
# Likes:    13
# Dislikes: 0
# Total Accepted:    5.5K
# Total Submissions: 11.5K
# Testcase Example:  '[2,3,4,6]'
#
# 给你一个由 不同 正整数组成的数组 nums ，请你返回满足 a * b = c * d 的元组 (a, b, c, d) 的数量。其中 a、b、c 和
# d 都是 nums 中的元素，且 a != b != c != d 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [2,3,4,6]
# 输出：8
# 解释：存在 8 个满足题意的元组：
# (2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
# (3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,4,5,10]
# 输出：16
# 解释：存在 16 个满足题意的元组：
# (1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
# (2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
# (2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,4,5)
# (4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [2,3,4,6,8,12]
# 输出：40
# 
# 
# 示例 4：
# 
# 
# 输入：nums = [2,3,5,7]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# nums 中的所有元素 互不相同
# 
# 
#

# @lc code=start
from collections import defaultdict
from math import comb


class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        product = defaultdict(int)
        m = set()

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                p = nums[i] * nums[j]
                product[p] += 1
                if product[p] > 1:
                    m.add(p)

        result = 0
        for p in m:
            result += comb(product[p], 2) * 8

        return result
# @lc code=end

print(Solution().tupleSameProduct([1,2,4,5,10]))
print(Solution().tupleSameProduct([2,3,4,6,8,12]))
print(Solution().tupleSameProduct([2,3,5,7]))

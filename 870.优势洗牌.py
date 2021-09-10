#
# @lc app=leetcode.cn id=870 lang=python3
#
# [870] 优势洗牌
#
# https://leetcode-cn.com/problems/advantage-shuffle/description/
#
# algorithms
# Medium (42.50%)
# Likes:    144
# Dislikes: 0
# Total Accepted:    14.2K
# Total Submissions: 33.4K
# Testcase Example:  '[2,7,11,15]\n[1,10,4,11]'
#
# 给定两个大小相等的数组 A 和 B，A 相对于 B 的优势可以用满足 A[i] > B[i] 的索引 i 的数目来描述。
# 
# 返回 A 的任意排列，使其相对于 B 的优势最大化。
# 
# 
# 
# 示例 1：
# 
# 输入：A = [2,7,11,15], B = [1,10,4,11]
# 输出：[2,11,7,15]
# 
# 
# 示例 2：
# 
# 输入：A = [12,24,8,32], B = [13,25,32,11]
# 输出：[24,32,8,12]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length = B.length <= 10000
# 0 <= A[i] <= 10^9
# 0 <= B[i] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def advantageCount(self, nums_1: list[int], nums_2: list[int]) -> list[int]:
        orders_2 = [i for i in range(len(nums_2))]
        orders_2.sort(key=lambda x: nums_2[x])
        nums_1.sort(key=lambda x: -x)

        temp = []
        result = [-1 for i in range(len(nums_1))]

        for i_2 in orders_2:
            num = nums_2[i_2]

            while nums_1 and nums_1[-1] <= num:
                temp.append(nums_1.pop())

            if not nums_1:
                break

            num_1 = nums_1.pop()
            result[i_2] = num_1

        for i, n in enumerate(result):
            if n == -1:
                result[i] = temp.pop()

        return result
# @lc code=end


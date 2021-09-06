#
# @lc app=leetcode.cn id=1043 lang=python3
#
# [1043] 分隔数组以得到最大和
#
# https://leetcode-cn.com/problems/partition-array-for-maximum-sum/description/
#
# algorithms
# Medium (68.74%)
# Likes:    109
# Dislikes: 0
# Total Accepted:    7.1K
# Total Submissions: 10.4K
# Testcase Example:  '[1,15,7,9,2,5,10]\n3'
#
# 给你一个整数数组 arr，请你将该数组分隔为长度最多为 k 的一些（连续）子数组。分隔完成后，每个子数组的中的所有值都会变为该子数组中的最大值。
# 
# 返回将数组分隔变换后能够得到的元素最大和。
# 
# 
# 
# 注意，原数组和分隔后的数组对应顺序应当一致，也就是说，你只能选择分隔数组的位置而不能调整数组中的顺序。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：arr = [1,15,7,9,2,5,10], k = 3
# 输出：84
# 解释：
# 因为 k=3 可以分隔成 [1,15,7] [9] [2,5,10]，结果为 [15,15,15,9,10,10,10]，和为
# 84，是该数组所有分隔变换后元素总和最大的。
# 若是分隔成 [1] [15,7,9] [2,5,10]，结果就是 [1, 15, 15, 15, 10, 10, 10]
# 但这种分隔方式的元素总和（76）小于上一种。 
# 
# 示例 2：
# 
# 
# 输入：arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
# 输出：83
# 
# 
# 示例 3：
# 
# 
# 输入：arr = [1], k = 1
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 1 
# 
# 
#

# @lc code=start
from collections import deque


class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        len_arr = len(arr)
        if len_arr <= k:
            return max(arr) * len_arr

        dp = deque()
        for i in range(len(arr)):
            if i < k:
                dp.append(max(arr[:i + 1]) * (i + 1))
            else:
                curr = 0
                for j in range(1, k + 1):
                    curr = max(dp[-j] + max(arr[i - j + 1:i + 1]) * j, curr)
                dp.popleft()
                dp.append(curr)

        return dp[-1]
# @lc code=end

print(Solution().maxSumAfterPartitioning([7,2], 1))

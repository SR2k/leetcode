#
# @lc app=leetcode.cn id=1013 lang=python3
#
# [1013] 将数组分成和相等的三个部分
#
# https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum/description/
#
# algorithms
# Easy (40.00%)
# Likes:    146
# Dislikes: 0
# Total Accepted:    44.8K
# Total Submissions: 111.9K
# Testcase Example:  '[0,2,1,-6,6,-7,9,1,2,0,1]'
#
# 给你一个整数数组 arr，只有可以将其划分为三个和相等的 非空 部分时才返回 true，否则返回 false。
# 
# 形式上，如果可以找出索引 i + 1 < j 且满足 (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] +
# arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length -
# 1]) 就可以将数组三等分。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：arr = [0,2,1,-6,6,-7,9,1,2,0,1]
# 输出：true
# 解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
# 
# 
# 示例 2：
# 
# 
# 输入：arr = [0,2,1,-6,6,7,9,-1,2,0,1]
# 输出：false
# 
# 
# 示例 3：
# 
# 
# 输入：arr = [3,3,6,5,-2,2,5,1,-9,4]
# 输出：true
# 解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
# 
# 
# 
# 
# 提示：
# 
# 
# 3 
# -10^4 
# 
# 
#

# @lc code=start
class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        arr_sum = sum(arr)
        if arr_sum % 3 != 0:
            return False
        target_group = arr_sum // 3

        prefix_sum = 0
        e1 = -1
        for i, n in enumerate(arr):
            prefix_sum += n
            if prefix_sum == target_group and e1 < 0:
                e1 = i
            if prefix_sum == 2 * target_group and 0 <= e1 < i < len(arr) - 1:
                return True

        return False
# @lc code=end


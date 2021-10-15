#
# @lc app=leetcode.cn id=1343 lang=python3
#
# [1343] 大小为 K 且平均值大于等于阈值的子数组数目
#
# https://leetcode-cn.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/
#
# algorithms
# Medium (54.45%)
# Likes:    33
# Dislikes: 0
# Total Accepted:    12.8K
# Total Submissions: 23.5K
# Testcase Example:  '[2,2,2,2,5,5,5,8]\n3\n4'
#
# 给你一个整数数组 arr 和两个整数 k 和 threshold 。
# 
# 请你返回长度为 k 且平均值大于等于 threshold 的子数组数目。
# 
# 
# 
# 示例 1：
# 
# 输入：arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
# 输出：3
# 解释：子数组 [2,5,5],[5,5,5] 和 [5,5,8] 的平均值分别为 4，5 和 6 。其他长度为 3 的子数组的平均值都小于 4
# （threshold 的值)。
# 
# 
# 示例 2：
# 
# 输入：arr = [1,1,1,1,1], k = 1, threshold = 0
# 输出：5
# 
# 
# 示例 3：
# 
# 输入：arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
# 输出：6
# 解释：前 6 个长度为 3 的子数组平均值都大于 5 。注意平均值不是整数。
# 
# 
# 示例 4：
# 
# 输入：arr = [7,7,7,7,7,7,7], k = 7, threshold = 7
# 输出：1
# 
# 
# 示例 5：
# 
# 输入：arr = [4,4,4,4], k = 4, threshold = 1
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= arr.length <= 10^5
# 1 <= arr[i] <= 10^4
# 1 <= k <= arr.length
# 0 <= threshold <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        threshold *= k
        right, sum = 0, 0

        while right <= k - 1:
            sum += arr[right]
            right += 1
        result = 1 if sum >= threshold else 0

        while right < len(arr):
            sum += arr[right]
            sum -= arr[right - k]
            if sum >= threshold:
                result += 1
            right += 1

        return result
# @lc code=end

s = Solution()
print(s.numOfSubarrays(arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4))
print(s.numOfSubarrays(arr = [1,1,1,1,1], k = 1, threshold = 0))
print(s.numOfSubarrays(arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5))
print(s.numOfSubarrays(arr = [7,7,7,7,7,7,7], k = 7, threshold = 7))
print(s.numOfSubarrays(arr = [4,4,4,4], k = 4, threshold = 1))

#
# @lc app=leetcode.cn id=1200 lang=python3
#
# [1200] 最小绝对差
#
# https://leetcode-cn.com/problems/minimum-absolute-difference/description/
#
# algorithms
# Easy (68.43%)
# Likes:    46
# Dislikes: 0
# Total Accepted:    16.9K
# Total Submissions: 24.6K
# Testcase Example:  '[4,2,1,3]'
#
# 给你个整数数组 arr，其中每个元素都 不相同。
# 
# 请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。
# 
# 
# 
# 示例 1：
# 
# 输入：arr = [4,2,1,3]
# 输出：[[1,2],[2,3],[3,4]]
# 
# 
# 示例 2：
# 
# 输入：arr = [1,3,6,10,15]
# 输出：[[1,3]]
# 
# 
# 示例 3：
# 
# 输入：arr = [3,8,-10,23,19,-4,-14,27]
# 输出：[[-14,-10],[19,23],[23,27]]
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= arr.length <= 10^5
# -10^6 <= arr[i] <= 10^6
# 
# 
#

# @lc code=start
class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        ret, curr_delta = [], float('inf')

        for i in range(1, len(arr)):
            a, b = arr[i], arr[i - 1]
            delta = a - b

            if curr_delta > delta:
                curr_delta = delta
                ret = [[b, a]]
            elif curr_delta == delta:
                ret.append([b, a])

        return ret
# @lc code=end


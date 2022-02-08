#
# @lc app=leetcode.cn id=845 lang=python3
#
# [845] 数组中的最长山脉
#
# https://leetcode-cn.com/problems/longest-mountain-in-array/description/
#
# algorithms
# Medium (41.95%)
# Likes:    192
# Dislikes: 0
# Total Accepted:    35.9K
# Total Submissions: 85.5K
# Testcase Example:  '[2,1,4,7,3,2,5]'
#
# 我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”：
# 
# 
# B.length >= 3
# 存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... >
# B[B.length - 1]
# 
# 
# （注意：B 可以是 A 的任意子数组，包括整个数组 A。）
# 
# 给出一个整数数组 A，返回最长 “山脉” 的长度。
# 
# 如果不含有 “山脉” 则返回 0。
# 
# 
# 
# 示例 1：
# 
# 输入：[2,1,4,7,3,2,5]
# 输出：5
# 解释：最长的 “山脉” 是 [1,4,7,3,2]，长度为 5。
# 
# 
# 示例 2：
# 
# 输入：[2,2,2]
# 输出：0
# 解释：不含 “山脉”。
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000
# 
# 
#

# @lc code=start
class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        if len(arr) < 3:
            return 0

        l = [0]
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                l.append(l[-1] + 1)
            else:
                l.append(0)

        r, ret = 0, 0
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                r = r + 1
            else:
                r = 0

            if l[i] > 0 and r > 0:
                ret = max(l[i] + r + 1, ret)

        return ret
# @lc code=end


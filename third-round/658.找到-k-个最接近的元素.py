#
# @lc app=leetcode.cn id=658 lang=python3
#
# [658] 找到 K 个最接近的元素
#
# https://leetcode-cn.com/problems/find-k-closest-elements/description/
#
# algorithms
# Medium (45.63%)
# Likes:    302
# Dislikes: 0
# Total Accepted:    33.3K
# Total Submissions: 72.9K
# Testcase Example:  '[1,2,3,4,5]\n4\n3'
#
# 给定一个 排序好 的数组 arr ，两个整数 k 和 x ，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。
# 
# 整数 a 比整数 b 更接近 x 需要满足：
# 
# 
# |a - x| < |b - x| 或者
# |a - x| == |b - x| 且 a < b
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：arr = [1,2,3,4,5], k = 4, x = 3
# 输出：[1,2,3,4]
# 
# 
# 示例 2：
# 
# 
# 输入：arr = [1,2,3,4,5], k = 4, x = -1
# 输出：[1,2,3,4]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= k <= arr.length
# 1 <= arr.length <= 10^4
# arr 按 升序 排列
# -10^4 <= arr[i], x <= 10^4
# 
# 
#

# @lc code=start
from collections import deque


class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        i = self.b_find(arr, x)
        j = i + 1

        result = deque()
        while len(result) < k:
            diff_i = abs(arr[i] - x) if i >= 0 else float('inf')
            diff_j = abs(arr[j] - x) if j < len(arr) else float('inf')

            if diff_i <= diff_j:
                result.appendleft(arr[i])
                i -= 1
            else:
                result.append(arr[j])
                j += 1

        return list(result)


    def b_find(self, arr: list[int], x: int):
        if arr[0] > x:
            return 0
        if arr[-1] < x:
            return len(arr) - 1

        left, right = 0, len(arr) - 1

        while left + 1 < right:
            middle = (right + left) >> 1
            num_middle = arr[middle]

            if num_middle >= x:
                right = middle
            else:
                left = middle

        if arr[right] <= x:
            return right
        return left
# @lc code=end

s = Solution()
# print(s.findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3))
# print(s.findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3))
# print(s.findClosestElements(arr = [1,2,3,4,5], k = 4, x = 99))
# print(s.findClosestElements(arr = [1,2,3,4,5], k = 5, x = -1))
print(s.findClosestElements([1,1,1,10,10,10], 1, 9))

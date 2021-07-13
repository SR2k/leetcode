#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#
# https://leetcode-cn.com/problems/relative-sort-array/description/
#
# algorithms
# Easy (70.69%)
# Likes:    180
# Dislikes: 0
# Total Accepted:    61.7K
# Total Submissions: 87.3K
# Testcase Example:  '[2,3,1,3,2,4,6,7,9,2,19]\n[2,1,4,3,9,6]'
#
# 给你两个数组，arr1 和 arr2，
# 
# 
# arr2 中的元素各不相同
# arr2 中的每个元素都出现在 arr1 中
# 
# 
# 对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1
# 的末尾。
# 
# 
# 
# 示例：
# 
# 
# 输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# 输出：[2,2,2,1,4,3,3,9,6,7,19]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# arr2 中的元素 arr2[i] 各不相同
# arr2 中的每个元素 arr2[i] 都出现在 arr1 中
# 
# 
#

# @lc code=start
from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        c1 = Counter(arr1)
        ret = []

        for n in arr2:
            for _ in range(c1[n]):
                ret.append(n)
            c1.pop(n)

        keys = list(c1.keys())
        keys.sort()
        for n in keys:
            for _ in range(c1[n]):
                ret.append(n)

        return ret
# @lc code=end

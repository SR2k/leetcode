#
# @lc app=leetcode.cn id=1930 lang=python3
#
# [1930] 长度为 3 的不同回文子序列
#
# https://leetcode-cn.com/problems/unique-length-3-palindromic-subsequences/description/
#
# algorithms
# Medium (45.89%)
# Likes:    8
# Dislikes: 0
# Total Accepted:    4.7K
# Total Submissions: 10.1K
# Testcase Example:  '"aabca"'
#
# 给你一个字符串 s ，返回 s 中 长度为 3 的不同回文子序列 的个数。
# 
# 即便存在多种方法来构建相同的子序列，但相同的子序列只计数一次。
# 
# 回文 是正着读和反着读一样的字符串。
# 
# 子序列 是由原字符串删除其中部分字符（也可以不删除）且不改变剩余字符之间相对顺序形成的一个新字符串。
# 
# 
# 例如，"ace" 是 "abcde" 的一个子序列。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "aabca"
# 输出：3
# 解释：长度为 3 的 3 个回文子序列分别是：
# - "aba" ("aabca" 的子序列)
# - "aaa" ("aabca" 的子序列)
# - "aca" ("aabca" 的子序列)
# 
# 
# 示例 2：
# 
# 
# 输入：s = "adc"
# 输出：0
# 解释："adc" 不存在长度为 3 的回文子序列。
# 
# 
# 示例 3：
# 
# 
# 输入：s = "bbcbaba"
# 输出：4
# 解释：长度为 3 的 4 个回文子序列分别是：
# - "bbb" ("bbcbaba" 的子序列)
# - "bcb" ("bbcbaba" 的子序列)
# - "bab" ("bbcbaba" 的子序列)
# - "aba" ("bbcbaba" 的子序列)
# 
# 
# 
# 
# 提示：
# 
# 
# 3 
# s 仅由小写英文字母组成
# 
# 
#

# @lc code=start
from collections import defaultdict


def check(nums: list[int], begin: int, end: int) -> bool:
    """
    Check if any number greater than left and less than right
    """
    if not nums:
        return False

    left, right = 0, len(nums) - 1
    while left + 1 < right:
        middle = (left  + right) // 2
        if nums[middle] > begin:
            right = middle
        else:
            left = middle
    min = -1
    if nums[left] > begin:
        min = left
    elif nums[right] > begin:
        min = right
    if min < 0:
        return False

    return nums[min] < end


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        appeared: defaultdict[str, list[int]] = defaultdict(list)
        for i, char in enumerate(s):
            appeared[char].append(i)

        r = range(ord('a'), ord('z') + 1)
        ret = 0

        for i in r:
            edge_appeared = appeared[chr(i)]
            if len(edge_appeared) < 2:
                continue
            left, right = edge_appeared[0], edge_appeared[-1]
            if right == left + 1:
                continue

            for j in r:
                center_char = chr(j)
                if check(appeared[center_char], left, right):
                    ret += 1

        return ret
# @lc code=end

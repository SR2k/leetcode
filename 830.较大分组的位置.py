#
# @lc app=leetcode.cn id=830 lang=python3
#
# [830] 较大分组的位置
#
# https://leetcode-cn.com/problems/positions-of-large-groups/description/
#
# algorithms
# Easy (54.31%)
# Likes:    116
# Dislikes: 0
# Total Accepted:    51.1K
# Total Submissions: 94.1K
# Testcase Example:  '"abbxxxxzzy"'
#
# 在一个由小写字母构成的字符串 s 中，包含由一些连续的相同字符所构成的分组。
# 
# 例如，在字符串 s = "abbxxxxzyy" 中，就含有 "a", "bb", "xxxx", "z" 和 "yy" 这样的一些分组。
# 
# 分组可以用区间 [start, end] 表示，其中 start 和 end 分别表示该分组的起始和终止位置的下标。上例中的 "xxxx"
# 分组用区间表示为 [3,6] 。
# 
# 我们称所有包含大于或等于三个连续字符的分组为 较大分组 。
# 
# 找到每一个 较大分组 的区间，按起始位置下标递增顺序排序后，返回结果。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "abbxxxxzzy"
# 输出：[[3,6]]
# 解释："xxxx" 是一个起始于 3 且终止于 6 的较大分组。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "abc"
# 输出：[]
# 解释："a","b" 和 "c" 均不是符合要求的较大分组。
# 
# 
# 示例 3：
# 
# 
# 输入：s = "abcdddeeeeaabbbcd"
# 输出：[[3,5],[6,9],[12,14]]
# 解释：较大分组为 "ddd", "eeee" 和 "bbb"
# 
# 示例 4：
# 
# 
# 输入：s = "aba"
# 输出：[]
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 仅含小写英文字母
# 
# 
#

# @lc code=start
class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        prev, prev_index = '', -1
        ret = []

        for i, n in enumerate(s + ' '):
            if n != prev:
                length = i - prev_index
                if length >= 3:
                    ret.append([prev_index, i - 1])
                prev = n
                prev_index = i

        return ret
# @lc code=end


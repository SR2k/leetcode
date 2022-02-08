#
# @lc app=leetcode.cn id=1081 lang=python3
#
# [1081] 不同字符的最小子序列
#
# https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters/description/
#
# algorithms
# Medium (57.00%)
# Likes:    101
# Dislikes: 0
# Total Accepted:    12.5K
# Total Submissions: 21.9K
# Testcase Example:  '"bcabc"'
#
# 返回 s 字典序最小的子序列，该子序列包含 s 的所有不同字符，且只包含一次。
# 
# 注意：该题与 316 https://leetcode.com/problems/remove-duplicate-letters/ 相同
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "bcabc"
# 输出："abc"
# 
# 
# 示例 2：
# 
# 
# 输入：s = "cbacdcbc"
# 输出："acdb"
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        cnt = len(s)
        if cnt <= 1: return s

        last_appear: dict[str, int] = {}
        for i in range(cnt): last_appear[s[i]] = i

        char_cnt = len(last_appear.keys())

        stack: list[str] = []
        visited: set[str] = set()
        for i in range(cnt):
            char = s[i]

            if char in visited: continue
            visited.add(char)

            while stack and ord(stack[-1]) >= ord(char) and last_appear[char] > i:
                visited.remove(stack.pop())
            stack.append(char)

            if len(stack) == char_cnt: break

        return ''.join(stack)
# @lc code=end


#
# @lc app=leetcode.cn id=316 lang=python3
#
# [316] 去除重复字母
#
# https://leetcode-cn.com/problems/remove-duplicate-letters/description/
#
# algorithms
# Medium (47.59%)
# Likes:    547
# Dislikes: 0
# Total Accepted:    58.8K
# Total Submissions: 123.4K
# Testcase Example:  '"bcabc"'
#
# 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
# 
# 注意：该题与 1081
# https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters
# 相同
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
    def removeDuplicateLetters(self, s: str) -> str:
        cnt = len(s)
        if cnt <= 1: return s

        last_appear: dict[int, int] = {}
        for i in range(cnt): last_appear[s[i]] = i
        char_count = len(last_appear.keys())

        stack, visited = [], set()
        for i in range(cnt):
            char = s[i]

            if char in visited: continue
            visited.add(char)

            while ord(char) >= ord[stack[-1]] and last_appear[stack[-1]] > i:
                stack.pop()
            stack.append(char)

            if len(stack) == char_count:
                return ''.join(stack)

        return ''.join(stack)

# @lc code=end


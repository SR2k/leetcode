#
# @lc app=leetcode.cn id=267 lang=python3
#
# [267] 回文排列 II
#
# https://leetcode-cn.com/problems/palindrome-permutation-ii/description/
#
# algorithms
# Medium (45.09%)
# Likes:    83
# Dislikes: 0
# Total Accepted:    4.2K
# Total Submissions: 9.2K
# Testcase Example:  '"aabb"'
#
# 给定一个字符串 s ，返回 其重新排列组合后可能构成的所有回文字符串，并去除重复的组合 。
# 
# 你可以按 任意顺序 返回答案。如果 s 不能形成任何回文排列时，则返回一个空列表。
# 
# 
# 
# 示例 1：
# 
# 
# 输入: s = "aabb"
# 输出: ["abba", "baab"]
# 
# 示例 2：
# 
# 
# 输入: s = "abc"
# 输出: []
# 
# 
# 
# 
# 提示：
# 
# 
# 
# 
# 1 <= s.length <= 16
# s 仅由小写英文字母组成
# 
# 
#

# @lc code=start
from collections import Counter


class Solution:
    def generatePalindromes(self, s: str) -> list[str]:
        counter = Counter(s)
        even_chars, odd_chars = [], []
        for char in counter:
            if counter[char] % 2 == 1:
                odd_chars.append(char)
            else:
                even_chars.append(char)

        if len(odd_chars) > 1:
            return []

        curr = []
        for e in even_chars:
            for _ in range(counter[e] // 2):
                curr.append(e)

        single_char = odd_chars[0] if odd_chars else ''
        curr += [single_char for _ in range((counter[single_char] - 1) // 2)]
        result = []

        def helper(i: int):
            if i >= len(curr):
                half = "".join(curr)
                result.append(half + single_char + half[::-1])
                return

            helper(i + 1)

            seen = set([curr[i]])
            for j in range(i + 1, len(curr)):
                if curr[j] in seen:
                    continue

                seen.add(curr[j])
                curr[i], curr[j] = curr[j], curr[i]
                helper(i + 1)
                curr[i], curr[j] = curr[j], curr[i]

        helper(0)
        return result
# @lc code=end

s = Solution()
print(s.generatePalindromes("aaaaaa"))
print(s.generatePalindromes("aaa"))
print(s.generatePalindromes("aabb"))
print(s.generatePalindromes("aaaacbb"))
print(s.generatePalindromes("abc"))

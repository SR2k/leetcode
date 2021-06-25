#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#
# https://leetcode-cn.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (42.41%)
# Likes:    368
# Dislikes: 0
# Total Accepted:    89.1K
# Total Submissions: 210.1K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
# 
# 换句话说，第一个字符串的排列之一是第二个字符串的 子串 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入: s1 = "ab" s2 = "eidbaooo"
# 输出: True
# 解释: s2 包含 s1 的排列之一 ("ba").
# 
# 
# 示例 2：
# 
# 
# 输入: s1= "ab" s2 = "eidboaoo"
# 输出: False
# 
# 
# 
# 
# 提示：
# 
# 
# 输入的字符串只包含小写字母
# 两个字符串的长度都在 [1, 10,000] 之间
# 
# 
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2: return False

        freq: dict[str, int] = {}
        for char in s1: freq[char] = 1 + (freq.get(char) or 0)

        left, right = 0, 0

        while right - left + 1 < len1:
            char_right = s2[right]
            freq[char_right] = freq.get(char_right) or 0
            freq[char_right] -= 1
            right += 1

        while right < len2:
            freq[s2[right]] = (freq.get(s2[right]) or 0) - 1

            if max(freq.values()) == 0 and min(freq.values()) == 0:
                return True

            freq[s2[left]] += 1
            left += 1
            right += 1

        return False
# @lc code=end

print(Solution().checkInclusion("ab", "eidbaooo"))


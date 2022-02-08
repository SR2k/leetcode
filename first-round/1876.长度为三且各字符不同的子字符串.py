#
# @lc app=leetcode.cn id=1876 lang=python3
#
# [1876] 长度为三且各字符不同的子字符串
#
# https://leetcode-cn.com/problems/substrings-of-size-three-with-distinct-characters/description/
#
# algorithms
# Easy (72.92%)
# Likes:    7
# Dislikes: 0
# Total Accepted:    5.9K
# Total Submissions: 8.1K
# Testcase Example:  '"xyzzaz"'
#
# 如果一个字符串不含有任何重复字符，我们称这个字符串为 好 字符串。
# 
# 给你一个字符串 s ，请你返回 s 中长度为 3 的 好子字符串 的数量。
# 
# 注意，如果相同的好子字符串出现多次，每一次都应该被记入答案之中。
# 
# 子字符串 是一个字符串中连续的字符序列。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "xyzzaz"
# 输出：1
# 解释：总共有 4 个长度为 3 的子字符串："xyz"，"yzz"，"zza" 和 "zaz" 。
# 唯一的长度为 3 的好子字符串是 "xyz" 。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "aababcabc"
# 输出：4
# 解释：总共有 7 个长度为 3 的子字符串："aab"，"aba"，"bab"，"abc"，"bca"，"cab" 和 "abc" 。
# 好子字符串包括 "abc"，"bca"，"cab" 和 "abc" 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# s​​​​​​ 只包含小写英文字母。
# 
# 
#

# @lc code=start
from collections import defaultdict


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0

        count = defaultdict(int)
        r = True
        for right in [0, 1, 2]:
            count[s[right]] += 1

            if count[s[right]] > 1:
                r = False

        result = 1 if r else 0
        for right in range(3, len(s)):
            count[s[right]] += 1
            count[s[right - 3]] -= 1

            r = count[s[right]] <= 1 and count[s[right - 1]] <= 1 and count[s[right - 2]] <= 1
            if r:
                result += 1

        return result
# @lc code=end

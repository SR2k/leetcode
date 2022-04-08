#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
# https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (54.06%)
# Likes:    788
# Dislikes: 0
# Total Accepted:    151.6K
# Total Submissions: 280.3K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
# 
# 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
# 
# 
# 示例 2:
# 
# 
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= s.length, p.length <= 3 * 10^4
# s 和 p 仅包含小写字母
# 
# 
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        counter = [0 for _ in range(26)]
        for char in p:
            counter[ord(char) - 97] += 1

        for i in range(len(p)):
            idx = ord(s[i]) - 97
            counter[idx] -= 1

        diff = len([c for c in counter if c != 0])

        result = []
        if not diff:
            result.append(0)

        for i in range(1, len(s) - len(p) + 1):
            j_idx = ord(s[i + len(p) - 1]) - 97
            counter[j_idx] -= 1
            if counter[j_idx] == 0:
                diff -= 1
            elif counter[j_idx] == -1:
                diff += 1

            i_idx = ord(s[i - 1]) - 97
            counter[i_idx] += 1
            if counter[i_idx] == 0:
                diff -= 1
            elif counter[i_idx] == 1:
                diff += 1

            if not diff:
                result.append(i)

        return result
# @lc code=end


# 1 2 3 4 5
# 1 2
print(Solution().findAnagrams(s = "cbaebabacd", p = "abc"))
print(Solution().findAnagrams(s = "abab", p = "ab"))

print(Solution().findAnagrams("baa", "aa"))

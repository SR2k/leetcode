#
# @lc app=leetcode.cn id=1156 lang=python3
#
# [1156] 单字符重复子串的最大长度
#
# https://leetcode-cn.com/problems/swap-for-longest-repeated-character-substring/description/
#
# algorithms
# Medium (42.62%)
# Likes:    84
# Dislikes: 0
# Total Accepted:    6K
# Total Submissions: 14.1K
# Testcase Example:  '"ababa"'
#
# 如果字符串中的所有字符都相同，那么这个字符串是单字符重复的字符串。
# 
# 给你一个字符串 text，你只能交换其中两个字符一次或者什么都不做，然后得到一些单字符重复的子串。返回其中最长的子串的长度。
# 
# 
# 
# 示例 1：
# 
# 输入：text = "ababa"
# 输出：3
# 
# 
# 示例 2：
# 
# 输入：text = "aaabaaa"
# 输出：6
# 
# 
# 示例 3：
# 
# 输入：text = "aaabbaaa"
# 输出：4
# 
# 
# 示例 4：
# 
# 输入：text = "aaaaa"
# 输出：5
# 
# 
# 示例 5：
# 
# 输入：text = "abcdef"
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= text.length <= 20000
# text 仅由小写英文字母组成。
# 
# 
#

# @lc code=start
from collections import defaultdict


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        first_seen, last_seen = {}, {}
        for i, char in enumerate(text):
            if char not in first_seen:
                first_seen[char] = last_seen[char] = i
            else:
                last_seen[char] = i

        i = 0
        counter = defaultdict(int)
        chars = set()

        def check() -> bool:
            if len(chars) > 2:
                return False
            if len(chars) <= 1:
                return True

            c = sorted(chars, key=lambda x: counter[x])
            if counter[c[0]] > 1:
                return False

            min_value_chars = [c[1]]
            if counter[c[0]] == counter[c[1]]:
                min_value_chars = c

            for m in min_value_chars:
                if first_seen[m] < i or last_seen[m] > j:
                    return True

            return False

        result = 0
        for j in range(len(text)):
            counter[text[j]] += 1
            if counter[text[j]] == 1:
                chars.add(text[j])

            while not check():
                counter[text[i]] -= 1
                if counter[text[i]] == 0:
                    chars.remove(text[i])
                i += 1

            # print(i, j, text[i:j + 1])
            result = max(j - i + 1, result)

        return result
# @lc code=end

s = Solution()

print(s.maxRepOpt1("abcdef"))
print(s.maxRepOpt1("idhajechdbdbeichdjjddefdjicidieciebcjfcgbfgfabhbejhbediebagjhgjdafiaeiggjhdajejcacecifigbcedeejbgbdi"))
print(s.maxRepOpt1("a"))
print(s.maxRepOpt1("ababa"))
print(s.maxRepOpt1("aaabaaa"))
print(s.maxRepOpt1( "aaabbaaa"))
print(s.maxRepOpt1("aaaaa"))

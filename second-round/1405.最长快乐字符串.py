#
# @lc app=leetcode.cn id=1405 lang=python3
#
# [1405] 最长快乐字符串
#
# https://leetcode-cn.com/problems/longest-happy-string/description/
#
# algorithms
# Medium (51.15%)
# Likes:    55
# Dislikes: 0
# Total Accepted:    6.2K
# Total Submissions: 12.1K
# Testcase Example:  '1\n1\n7'
#
# 如果字符串中不含有任何 'aaa'，'bbb' 或 'ccc' 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。
# 
# 给你三个整数 a，b ，c，请你返回 任意一个 满足下列全部条件的字符串 s：
# 
# 
# s 是一个尽可能长的快乐字符串。
# s 中 最多 有a 个字母 'a'、b 个字母 'b'、c 个字母 'c' 。
# s 中只含有 'a'、'b' 、'c' 三种字母。
# 
# 
# 如果不存在这样的字符串 s ，请返回一个空字符串 ""。
# 
# 
# 
# 示例 1：
# 
# 输入：a = 1, b = 1, c = 7
# 输出："ccaccbcc"
# 解释："ccbccacc" 也是一种正确答案。
# 
# 
# 示例 2：
# 
# 输入：a = 2, b = 2, c = 1
# 输出："aabbc"
# 
# 
# 示例 3：
# 
# 输入：a = 7, b = 1, c = 0
# 输出："aabaa"
# 解释：这是该测试用例的唯一正确答案。
# 
# 
# 
# 提示：
# 
# 
# 0 <= a, b, c <= 100
# a + b + c > 0
# 
# 
#

# @lc code=start
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        chars = ['a', 'b', 'c']
        count = { 'a': a, 'b': b, 'c': c }
        chars.sort(key=lambda x: -count[x])

        result = ''
        while True:
            char = chars[0]
            if len(result) >= 2 and result[-1] == result[-2] == char:
                char = chars[1]
            if not count[char]:
                break
            result += char
            count[char] -= 1
            chars.sort(key=lambda x: -count[x])

        return result
# @lc code=end

s = Solution()

print(s.longestDiverseString(a = 1, b = 1, c = 7))
print(s.longestDiverseString(a = 1, b = 2, c = 7))
print(s.longestDiverseString(a = 2, b = 2, c = 1))
print(s.longestDiverseString(a = 7, b = 1, c = 0))
print(s.longestDiverseString(a = 8, b = 8, c = 8))

print(s.longestDiverseString(0, 8, 11))

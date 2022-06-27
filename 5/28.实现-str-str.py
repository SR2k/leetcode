#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#
# https://leetcode.cn/problems/implement-strstr/description/
#
# algorithms
# Easy (40.60%)
# Likes:    1440
# Dislikes: 0
# Total Accepted:    654.3K
# Total Submissions: 1.6M
# Testcase Example:  '"hello"\n"ll"'
#
# 实现 strStr() 函数。
# 
# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0
# 开始）。如果不存在，则返回  -1 。
# 
# 说明：
# 
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
# 
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf()
# 定义相符。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：haystack = "hello", needle = "ll"
# 输出：2
# 
# 
# 示例 2：
# 
# 
# 输入：haystack = "aaaaa", needle = "bba"
# 输出：-1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= haystack.length, needle.length <= 10^4
# haystack 和 needle 仅由小写英文字符组成
# 
# 
#

# @lc code=start
SCALE = 31
MODULO = 60000000
ORD_A = ord('a')

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle = len(needle)
        if len_needle > len(haystack):
            return -1

        hash_needle = Solution.hash(needle, 0, len_needle - 1)
        hash = Solution.hash(haystack, 0, len_needle - 1)

        if hash == hash_needle and Solution.check(haystack, needle, 0):
            return 0

        top_scale = 1
        for _ in range(len_needle - 1):
            top_scale = (top_scale * 31) % MODULO

        for end in range(len_needle, len(haystack)):
            prev_begin = end - len_needle
            begin = prev_begin + 1

            hash = (hash - (ord(haystack[prev_begin]) - ORD_A) * top_scale) % MODULO
            hash = (hash * SCALE + ord(haystack[end]) - ORD_A) % MODULO

            if hash == hash_needle and Solution.check(haystack, needle, begin):
                return begin

        return -1


    @staticmethod
    def hash(s: str, begin: int, end: int):
        result = 0
        for i in range(begin, end + 1):
            result = result * 31 + ord(s[i]) - ORD_A
            result %= MODULO
        return result


    @staticmethod
    def check(a: str, b: str, begin: int):
        if begin + len(b) - 1 >= len(a):
            return False

        for i in range(len(b)):
            if a[begin + i] != b[i]:
                return False
        return True
# @lc code=end

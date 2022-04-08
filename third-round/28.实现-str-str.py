#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#
# https://leetcode-cn.com/problems/implement-strstr/description/
#
# algorithms
# Easy (40.14%)
# Likes:    1347
# Dislikes: 0
# Total Accepted:    602K
# Total Submissions: 1.5M
# Testcase Example:  '"hello"\n"ll"'
#
# 实现 strStr() 函数。
# 
# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0
# 开始）。如果不存在，则返回  -1 。
# 
# 
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
# 示例 3：
# 
# 
# 输入：haystack = "", needle = ""
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# haystack 和 needle 仅由小写英文字符组成
# 
# 
#

# @lc code=start
MODULO = 6 * 10 ** 7
SCALE = 31


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        hash_needle = Solution.hash(needle)
        curr_hash = Solution.hash(haystack, 0, len(needle) - 1)

        if curr_hash == hash_needle and Solution.check(haystack, 0, len(needle) - 1, needle):
            return 0

        # print(curr_hash)

        top_digit_scale = 1
        for _ in range(len(needle) - 1):
            top_digit_scale = (top_digit_scale * SCALE) % MODULO

        for right in range(len(needle), len(haystack)):
            popped_index = right - len(needle)
            curr_hash = curr_hash - (ord(haystack[popped_index]) - ord('a')) * top_digit_scale + MODULO
            curr_hash %= MODULO
            curr_hash = (curr_hash * SCALE) % MODULO
            curr_hash += ord(haystack[right]) - ord('a')

            if curr_hash == hash_needle:
                if Solution.check(haystack, popped_index + 1, right, needle):
                    return popped_index + 1

        return -1


    @staticmethod
    def check(a: str, ai: int, aj: int, b: str):
        if aj - ai + 1 != len(b):
            return False

        for i, char in enumerate(b):
            if char != a[ai + i]:
                return False

        return True


    @staticmethod
    def hash(s: str, l = 0, r = None):
        r = len(s) - 1 if r is None else r
        i = l
        hash = 0
        while i <= r:
            hash = (hash * SCALE) % MODULO
            hash += ord(s[i]) - ord('a')
            hash %= MODULO
            i += 1
        return hash
# @lc code=end

s = Solution()
# print(s.strStr(haystack = "hello", needle = "ll"))
# print(s.strStr(haystack = "aaaaa", needle = "bba"))
# print(s.strStr(haystack = "", needle = ""))
# print(s.strStr(haystack = "aaa", needle = ""))
# print(s.strStr("https://market.m.taobao.com/ap", "mar"))
# print(s.strStr("https://market.m.taobao.com/app/place-shop/rax-pi/pages/weex?ut_sk=1.XkIFY6jB0IgDAOagBlUIr1PJ_21380790_1648198014268.Copy.10000&wh_weex=true&pagePath=shop%2Findex&pageId=0&shopId=0&suid=E4E032D4-1A37-422C-AEB2-E6DBE1DD2ABA&sellerId=307561225&bizCode=place_alihealth&tbShopContainer=1&wx_navbar_hidden=true&wx_navbar_transparent=true&sourceType=other&un=7eb5c8cabd912f6b7e9fbf4444ed5bfe&share_crt_v=1&un_site=0&spm=a2159r.13376460.0.0&sp_tk=5Lmf6L%2BZ5aSp5aSa5pyJ6L%2BZ5aSn5a2Q5pyJ5LuW5LqG&cpp=1&shareurl=true&short_name=h.foDwRMS&sm=a09fbd&app=chrome", "5Lmf6L%2BZ5aSp5aSa5pyJ6L%2BZ5aSn5a2Q5pyJ5LuW5LqG&cpp=1&shareurl=true&short_name="))


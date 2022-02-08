#
# @lc app=leetcode.cn id=1239 lang=python3
#
# [1239] 串联字符串的最大长度
#
# https://leetcode-cn.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/
#
# algorithms
# Medium (49.13%)
# Likes:    194
# Dislikes: 0
# Total Accepted:    36K
# Total Submissions: 73.2K
# Testcase Example:  '["un","iq","ue"]'
#
# 给定一个字符串数组 arr，字符串 s 是将 arr 某一子序列字符串连接所得的字符串，如果 s 中的每一个字符都只出现过一次，那么它就是一个可行解。
# 
# 请返回所有可行解 s 中最长长度。
# 
# 
# 
# 示例 1：
# 
# 输入：arr = ["un","iq","ue"]
# 输出：4
# 解释：所有可能的串联组合是 "","un","iq","ue","uniq" 和 "ique"，最大长度为 4。
# 
# 
# 示例 2：
# 
# 输入：arr = ["cha","r","act","ers"]
# 输出：6
# 解释：可能的解答有 "chaers" 和 "acters"。
# 
# 
# 示例 3：
# 
# 输入：arr = ["abcdefghijklmnopqrstuvwxyz"]
# 输出：26
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= arr.length <= 16
# 1 <= arr[i].length <= 26
# arr[i] 中只含有小写英文字母
# 
# 
#

# @lc code=start
class Solution:
    @staticmethod
    def word_2_int(word: str) -> int:
        l = 0
        seen = set()
        for char in word:
            if char in seen:
                return -1
            seen.add(char)
            l += 1 << (ord(char) - ord('a'))
        return l

    @staticmethod
    def calc(r: int) -> int:
        result = 0
        while r:
            if r % 2 == 1:
                result += 1
                r -= 1
            r //= 2
        return result

    def maxLength(self, arr: list[str]) -> int:
        arr = [Solution.word_2_int(x) for x in arr]
        arr = [x for x in arr if x > 0]
        result = 0

        def helper(curr: int, i: int):
            if i >= len(arr):
                nonlocal result
                result = max(Solution.calc(curr), result)
                return

            helper(curr, i + 1)

            if curr & arr[i] == 0:
                curr ^= arr[i]
                helper(curr, i + 1)
                curr ^= arr[i]

        helper(0, 0)
        return result
# @lc code=end

s = Solution()
print(s.maxLength(arr = ["un","iq","ue"]))
print(s.maxLength(arr = ["cha","r","act","ers"]))
print(s.maxLength(arr = ["abcdefghijklmnopqrstuvwxyz"]))

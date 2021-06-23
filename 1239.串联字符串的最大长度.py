#
# @lc app=leetcode.cn id=1239 lang=python3
#
# [1239] 串联字符串的最大长度
#
# https://leetcode-cn.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/
#
# algorithms
# Medium (41.26%)
# Likes:    90
# Dislikes: 0
# Total Accepted:    16.3K
# Total Submissions: 39.4K
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
    cache = [2 ** i for i in range(26)]

    @staticmethod
    def to_bits(s: str) -> int:
        ret = 0
        for char in s:
            idx = ord(char) - ord('a')
            print(char, idx, ret, ret | Solution.cache[idx], ret + Solution.cache[idx])
            if ret | Solution.cache[idx] != ret + Solution.cache[idx]: return None
            ret |= Solution.cache[idx]
        return ret

    def maxLength(self, arr: list[str]) -> int:
        temp = []
        for char in arr:
            pass

# @lc code=end

# print(Solution.cache, Solution.cache[ord('u') - ord('a')])
# print(Solution.to_bits('unique'))
print(Solution.to_bits('uniu'))

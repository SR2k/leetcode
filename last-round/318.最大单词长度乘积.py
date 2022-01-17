#
# @lc app=leetcode.cn id=318 lang=python3
#
# [318] 最大单词长度乘积
#
# https://leetcode-cn.com/problems/maximum-product-of-word-lengths/description/
#
# algorithms
# Medium (67.70%)
# Likes:    176
# Dislikes: 0
# Total Accepted:    17.3K
# Total Submissions: 25.6K
# Testcase Example:  '["abcw","baz","foo","bar","xtfn","abcdef"]'
#
# 给定一个字符串数组 words，找到 length(word[i]) * length(word[j])
# 的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
# 输出: 16 
# 解释: 这两个单词为 "abcw", "xtfn"。
# 
# 示例 2:
# 
# 
# 输入: ["a","ab","abc","d","cd","bcd","abcd"]
# 输出: 4 
# 解释: 这两个单词为 "ab", "cd"。
# 
# 示例 3:
# 
# 
# 输入: ["a","aa","aaa","aaaa"]
# 输出: 0 
# 解释: 不存在这样的两个单词。
# 
# 
# 
# 
# 提示：
# 
# 
# 2 
# 1 
# words[i] 仅包含小写字母
# 
# 
#

# @lc code=start
MAP = {}
for i in range(ord('a'), ord('z') + 1):
    MAP[chr(i)] = 1 << (i - ord('a'))

def word_2_bits(word: str) -> int:
    ret = 0
    for char in word:
        ret |= MAP[char]
    return ret

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        d = [word_2_bits(w) for w in words]
        ret = 0

        for i in range(len(d) - 1):
            wi = d[i]
            for j in range(i + 1, len(d)):
                wj = d[j]
                if wi & wj == 0:
                    ret = max(ret, len(words[i]) * len(words[j]))

        return ret
# @lc code=end


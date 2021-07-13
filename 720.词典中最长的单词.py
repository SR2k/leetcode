#
# @lc app=leetcode.cn id=720 lang=python3
#
# [720] 词典中最长的单词
#
# https://leetcode-cn.com/problems/longest-word-in-dictionary/description/
#
# algorithms
# Easy (48.57%)
# Likes:    142
# Dislikes: 0
# Total Accepted:    17.1K
# Total Submissions: 35.3K
# Testcase Example:  '["w","wo","wor","worl","world"]'
#
# 
# 给出一个字符串数组words组成的一本英语词典。从中找出最长的一个单词，该单词是由words词典中其他单词逐步添加一个字母组成。若其中有多个可行的答案，则返回答案中字典序最小的单词。
# 
# 若无答案，则返回空字符串。
# 
# 
# 
# 示例 1：
# 
# 输入：
# words = ["w","wo","wor","worl", "world"]
# 输出："world"
# 解释： 
# 单词"world"可由"w", "wo", "wor", 和 "worl"添加一个字母组成。
# 
# 
# 示例 2：
# 
# 输入：
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# 输出："apple"
# 解释：
# "apply"和"apple"都能由词典中的单词组成。但是"apple"的字典序小于"apply"。
# 
# 
# 
# 
# 提示：
# 
# 
# 所有输入的字符串都只包含小写字母。
# words数组长度范围为[1,1000]。
# words[i]的长度范围为[1,30]。
# 
# 
#

# @lc code=start
class Solution:
    def longestWord(self, words: list[str]) -> str:
        trie = {}
        for word in words:
            curr = trie
            for char in word:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            curr['#'] = {}

        ret, max_len = [], 0

        def helper(node: dict, prev: str, curr: str):
            nonlocal ret
            nonlocal max_len

            if curr == '#':
                if len(prev) > max_len:
                    ret = [prev]
                    max_len = len(prev)
                elif len(prev) == max_len:
                    ret.append(prev)
                return

            if '#' not in node:
                return
            for n in node:
                helper(node[n], prev + curr, n)

        for n in trie:
            helper(trie[n], '', n)
        ret.sort()
        return ret[0] if ret else ""
# @lc code=end

print(Solution().longestWord(["wo","wor","worl","world"]))


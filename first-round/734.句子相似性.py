#
# @lc app=leetcode.cn id=734 lang=python3
#
# [734] 句子相似性
#
# https://leetcode-cn.com/problems/sentence-similarity/description/
#
# algorithms
# Easy (47.77%)
# Likes:    22
# Dislikes: 0
# Total Accepted:    1.8K
# Total Submissions: 3.8K
# Testcase Example:  '["great","acting","skills"]\n' +
#  '["fine","drama","talent"]\n' +
#  '[["great","fine"],["drama","acting"],["skills","talent"]]'
#
# 给定两个句子 words1, words2 （每个用字符串数组表示），和一个相似单词对的列表 pairs ，判断是否两个句子是相似的。
# 
# 例如，当相似单词对是 pairs = [["great", "fine"], ["acting","drama"],
# ["skills","talent"]]的时候，"great acting skills" 和 "fine drama talent" 是相似的。
# 
# 注意相似关系是不具有传递性的。例如，如果 "great" 和 "fine" 是相似的，"fine" 和 "good" 是相似的，但是 "great" 和
# "good" 未必是相似的。
# 
# 但是，相似关系是具有对称性的。例如，"great" 和 "fine" 是相似的相当于 "fine" 和 "great" 是相似的。
# 
# 而且，一个单词总是与其自身相似。例如，句子 words1 = ["great"], words2 = ["great"], pairs = []
# 是相似的，尽管没有输入特定的相似单词对。
# 
# 最后，句子只会在具有相同单词个数的前提下才会相似。所以一个句子 words1 = ["great"] 永远不可能和句子 words2 =
# ["doubleplus","good"] 相似。
# 
# 
# 
# 注：
# 
# 
# words1 and words2 的长度不会超过 1000。
# pairs 的长度不会超过 2000。
# 每个pairs[i] 的长度为 2。
# 每个 words[i] 和 pairs[i][j] 的长度范围为 [1, 20]。
# 
# 
# 
# 
#

# @lc code=start
from collections import defaultdict


class Solution:
    def areSentencesSimilar(self, sentence1: list[str], sentence2: list[str], similarPairs: list[list[str]]) -> bool:
        len_1, len_2 = len(sentence1), len(sentence2)
        if len_1 != len_2:
            return False

        pairs: defaultdict[str, set[str]] = defaultdict(set)
        for a, b in similarPairs:
            pairs[a].add(b)

        for i in range(len_1):
            word_1, word_2 = sentence1[i], sentence2[i]
            if not word_1 == word_2 and not word_2 in pairs[word_1] and not word_1 in pairs[word_2]:
                return False
        return True
# @lc code=end


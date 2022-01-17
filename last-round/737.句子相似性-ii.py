#
# @lc app=leetcode.cn id=737 lang=python3
#
# [737] 句子相似性 II
#
# https://leetcode-cn.com/problems/sentence-similarity-ii/description/
#
# algorithms
# Medium (46.25%)
# Likes:    47
# Dislikes: 0
# Total Accepted:    3.4K
# Total Submissions: 7.4K
# Testcase Example:  '["great","acting","skills"]\n' +
#  '["fine","drama","talent"]\n' +
#  '[["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]'
#
# 给定两个句子 words1, words2 （每个用字符串数组表示），和一个相似单词对的列表 pairs ，判断是否两个句子是相似的。
# 
# 例如，当相似单词对是 pairs = [["great", "fine"], ["acting","drama"],
# ["skills","talent"]]的时候，words1 = ["great", "acting", "skills"] 和 words2 =
# ["fine", "drama", "talent"] 是相似的。
# 
# 注意相似关系是 具有 传递性的。例如，如果 "great" 和 "fine" 是相似的，"fine" 和 "good" 是相似的，则 "great" 和
# "good" 是相似的。
# 
# 而且，相似关系是具有对称性的。例如，"great" 和 "fine" 是相似的相当于 "fine" 和 "great" 是相似的。
# 
# 并且，一个单词总是与其自身相似。例如，句子 words1 = ["great"], words2 = ["great"], pairs = []
# 是相似的，尽管没有输入特定的相似单词对。
# 
# 最后，句子只会在具有相同单词个数的前提下才会相似。所以一个句子 words1 = ["great"] 永远不可能和句子 words2 =
# ["doubleplus","good"] 相似。
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

# @lc code=start
def find_root(parents: dict[str, str], word: str) -> str:
    if word not in parents:
        return word

    while word in parents and word != parents[word]:
        word = parents[word]

    return word

class Solution:
    def areSentencesSimilarTwo(self, sentence1: list[str], sentence2: list[str], similarPairs: list[list[str]]) -> bool:
        len_1, len_2 = len(sentence1), len(sentence2)
        if len_1 != len_2:
            return False

        parents: dict[str, str] = {}
        for a, b in similarPairs:
            parents[find_root(parents, a)] = find_root(parents, b)

        for i in range(len_1):
            word_1, word_2 = sentence1[i], sentence2[i]
            if find_root(parents, word_1) != find_root(parents, word_2):
                return False
        return True
# @lc code=end


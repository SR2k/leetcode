#
# @lc app=leetcode.cn id=244 lang=python3
#
# [244] 最短单词距离 II
#
# https://leetcode-cn.com/problems/shortest-word-distance-ii/description/
#
# algorithms
# Medium (54.82%)
# Likes:    53
# Dislikes: 0
# Total Accepted:    4.8K
# Total Submissions: 8.7K
# Testcase Example:  '["WordDistance","shortest","shortest"]\n' +
#  '[[["practice","makes","perfect","coding","makes"]],["coding","practice"],["makes","coding"]]'
#
# 请设计一个类，使该类的构造函数能够接收一个单词列表。然后再实现一个方法，该方法能够分别接收两个单词 word1 和
# word2，并返回列表中这两个单词之间的最短距离。您的方法将被以不同的参数调用 多次。
# 
# 示例:
# 假设 words = ["practice", "makes", "perfect", "coding", "makes"]
# 
# 输入: word1 = “coding”, word2 = “practice”
# 输出: 3
# 
# 
# 输入: word1 = "makes", word2 = "coding"
# 输出: 1
# 
# 注意:
# 你可以假设 word1 不等于 word2, 并且 word1 和 word2 都在列表里。
# 
#

# @lc code=start
from collections import defaultdict


class WordDistance:
    def __init__(self, wordsDict: list[str]):
        self.index_map = defaultdict(list)

        for i, str in enumerate(wordsDict):
            self.index_map[str].append(i)


    def shortest(self, word1: str, word2: str) -> int:
        index_1, index_2 = self.index_map[word1], self.index_map[word2]
        p1, p2 = 0, 0
        result = float('inf')

        while True:
            result = min(result, abs(index_1[p1] - index_2[p2]))

            if p1 == len(index_1) - 1 and p2 == len(index_2) - 1:
                break
            elif p1 == len(index_1) - 1:
                p2 += 1
            elif p2 == len(index_2) - 1:
                p1 += 1
            elif index_1[p1 + 1] < index_2[p2 + 1]:
                p1 += 1
            else:
                p2 += 1

        return result

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
# @lc code=end

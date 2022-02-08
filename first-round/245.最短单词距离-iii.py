#
# @lc app=leetcode.cn id=245 lang=python3
#
# [245] 最短单词距离 III
#
# https://leetcode-cn.com/problems/shortest-word-distance-iii/description/
#
# algorithms
# Medium (60.93%)
# Likes:    35
# Dislikes: 0
# Total Accepted:    4.2K
# Total Submissions: 6.8K
# Testcase Example:  '["practice", "makes", "perfect", "coding", "makes"]\n"makes"\n"coding"'
#
# 给定一个单词列表和两个单词 word1 和 word2，返回列表中这两个单词之间的最短距离。
# 
# word1 和 word2 是有可能相同的，并且它们将分别表示为列表中两个独立的单词。
# 
# 示例:
# 假设 words = ["practice", "makes", "perfect", "coding", "makes"].
# 
# 输入: word1 = “makes”, word2 = “coding”
# 输出: 1
# 
# 
# 输入: word1 = "makes", word2 = "makes"
# 输出: 3
# 
# 
# 注意:
# 你可以假设 word1 和 word2 都在列表里。
# 
#

# @lc code=start
from collections import defaultdict


class Solution:
    def shortestWordDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        index_map = defaultdict(list)
        for i, str in enumerate(wordsDict):
            index_map[str].append(i)

        if word1 == word2:
            index_list = index_map[word1]
            r = range(1, len(index_list))
            return min(index_list[i] - index_list[i - 1] for i in r)

        p1, p2 = 0, 0
        index_list_1, index_list_2 = index_map[word1], index_map[word2]
        result = len(wordsDict) + 1
        while True:
            result = min(result, abs(index_list_1[p1] - index_list_2[p2]))

            if p1 == len(index_list_1) - 1 and p2 == len(index_list_2) - 1:
                return result
            elif p1 == len(index_list_1) - 1:
                p2 += 1
            elif p2 == len(index_list_2) - 1:
                p1 += 1
            elif index_list_1[p1 + 1] < index_list_2[p2 + 1]:
                p1 += 1
            else:
                p2 += 1
# @lc code=end

#
# @lc app=leetcode.cn id=1181 lang=python3
#
# [1181] 前后拼接
#
# https://leetcode-cn.com/problems/before-and-after-puzzle/description/
#
# algorithms
# Medium (37.01%)
# Likes:    12
# Dislikes: 0
# Total Accepted:    1.5K
# Total Submissions: 3.9K
# Testcase Example:  '["writing code","code rocks"]'
#
# 给你一个「短语」列表 phrases，请你帮忙按规则生成拼接后的「新短语」列表。
# 
# 「短语」（phrase）是仅由小写英文字母和空格组成的字符串。「短语」的开头和结尾都不会出现空格，「短语」中的空格不会连续出现。
# 
# 「前后拼接」（Before and After puzzles）是合并两个「短语」形成「新短语」的方法。我们规定拼接时，第一个短语的最后一个单词 和
# 第二个短语的第一个单词 必须相同。
# 
# 返回每两个「短语」 phrases[i] 和 phrases[j]（i != j）进行「前后拼接」得到的「新短语」。
# 
# 注意，两个「短语」拼接时的顺序也很重要，我们需要同时考虑这两个「短语」。另外，同一个「短语」可以多次参与拼接，但「新短语」不能再参与拼接。
# 
# 请你按字典序排列并返回「新短语」列表，列表中的字符串应该是 不重复的 。
# 
# 
# 
# 示例 1：
# 
# 输入：phrases = ["writing code","code rocks"]
# 输出：["writing code rocks"]
# 
# 
# 示例 2：
# 
# 输入：phrases = ["mission statement",⁠"a quick bite to eat","a chip off the old block","chocolate bar","mission impossible","a man on a mission","block party","eat my words","bar of soap"]
# 输出：["a chip off the old block party",
# "a man on a mission impossible",
# "a man on a mission statement",
# "a quick bite to eat my words",
# ⁠     "chocolate bar of soap"]
# 
# 
# 示例 3：
# 
# 输入：phrases = ["a","b","a"]
# 输出：["a"]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= phrases.length <= 100
# 1 <= phrases[i].length <= 100
# 
# 
#

# @lc code=start
from collections import defaultdict


class Solution:
    def build(self, phrases: list[str], pair: tuple[int, int]):
        a, b = phrases[pair[0]], phrases[pair[1]]
        return " ".join(a.split(' ') + b.split(' ')[1:])


    def beforeAndAfterPuzzles(self, phrases: list[str]) -> list[str]:
        first_words, last_words = defaultdict(set), defaultdict(set)
        pairs = set()

        for i, p in enumerate(phrases):
            words = p.split(' ')
            first, last = words[0], words[-1]

            for matched_first in first_words[last]:
                pairs.add((i, matched_first))
            for matched_last in last_words[first]:
                pairs.add((matched_last, i))

            first_words[first].add(i)
            last_words[last].add(i)

        result = list(set(self.build(phrases, pair) for pair in pairs))
        result.sort()
        return result
# @lc code=end

l = ["mission statement","a quick bite to eat","a chip off the old block","chocolate bar","mission impossible","a man on a mission","block party","eat my words","bar of soap"]
print(Solution().beforeAndAfterPuzzles(l))

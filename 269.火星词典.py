#
# @lc app=leetcode.cn id=269 lang=python3
#
# [269] 火星词典
#
# https://leetcode-cn.com/problems/alien-dictionary/description/
#
# algorithms
# Hard (34.36%)
# Likes:    194
# Dislikes: 0
# Total Accepted:    7.1K
# Total Submissions: 20.7K
# Testcase Example:  '["wrt","wrf","er","ett","rftt"]'
#
# 现有一种使用英语字母的火星语言，这门语言的字母顺序与英语顺序不同。
# 
# 给你一个字符串列表 words ，作为这门语言的词典，words 中的字符串已经 按这门新语言的字母顺序进行了排序 。
# 
# 请你根据该词典还原出此语言中已知的字母顺序，并 按字母递增顺序 排列。若不存在合法字母顺序，返回 "" 。若存在多种可能的合法字母顺序，返回其中 任意一种
# 顺序即可。
# 
# 字符串 s 字典顺序小于 字符串 t 有两种情况：
# 
# 
# 在第一个不同字母处，如果 s 中的字母在这门外星语言的字母顺序中位于 t 中字母之前，那么 s 的字典顺序小于 t 。
# 如果前面 min(s.length, t.length) 字母都相同，那么 s.length < t.length 时，s 的字典顺序也小于 t
# 。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：words = ["wrt","wrf","er","ett","rftt"]
# 输出："wertf"
# 
# 
# 示例 2：
# 
# 
# 输入：words = ["z","x"]
# 输出："zx"
# 
# 
# 示例 3：
# 
# 
# 输入：words = ["z","x","z"]
# 输出：""
# 解释：不存在合法字母顺序，因此返回 "" 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# words[i] 仅由小写英文字母组成
# 
# 
#

# @lc code=start
from collections import defaultdict


def diff(s1: str, s2: str) -> tuple[str, str]:
    for i in range(min(len(s1), len(s2))):
        if s1[i] != s2[i]:
            return s1[i], s2[i]


def get_min(degrees: defaultdict[str, int], letters: set[str]):
    for key in letters:
        if key not in degrees or degrees[key] == 0:
            return key


class Solution:
    def alienOrder(self, words: list[str]) -> str:
        graph = defaultdict(set)
        degrees = defaultdict(int)
        all_letters = set()

        for word in words:
            all_letters.update(char for char in word)

        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                diff_result = diff(words[i], words[j])
                if not diff_result and len(words[i]) > len(words[j]):
                    return ''
                if not diff_result:
                    continue

                d1, d2 = diff_result
                if d2 not in graph[d1]:
                    degrees[d2] += 1
                graph[d1].add(d2)

        result = ''

        while all_letters:
            curr = get_min(degrees, all_letters)

            if not curr:
                return ''

            for children in graph[curr]:
                degrees[children] -= 1

            result += curr
            all_letters.remove(curr)

        return result
# @lc code=end

s = Solution()
print(s.alienOrder(["wrt","wrf","er","ett","rftt"]))
print(s.alienOrder(["z","x"]))
print(s.alienOrder(["z","x","z"]))
print(s.alienOrder(["zy","zx"]))
print(s.alienOrder(["abc","ab"]))

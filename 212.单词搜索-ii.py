#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#
# https://leetcode.cn/problems/word-search-ii/description/
#
# algorithms
# Hard (45.18%)
# Likes:    691
# Dislikes: 0
# Total Accepted:    80.8K
# Total Submissions: 178.9K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
#  '["oath","pea","eat","rain"]'
#
# 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words， 返回所有二维网格上的单词 。
# 
# 单词必须按照字母顺序，通过 相邻的单元格
# 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：board =
# [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
# words = ["oath","pea","eat","rain"]
# 输出：["eat","oath"]
# 
# 
# 示例 2：
# 
# 
# 输入：board = [["a","b"],["c","d"]], words = ["abcb"]
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] 是一个小写英文字母
# 1 <= words.length <= 3 * 10^4
# 1 <= words[i].length <= 10
# words[i] 由小写英文字母组成
# words 中的所有字符串互不相同
# 
# 
#

# @lc code=start
from typing import Optional


Point = tuple[int, int]


class Solution:
    directions = (0, 1), (0, -1), (1, 0), (-1, 0)


    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = self.build_trie(words)

        m, n = len(board), len(board[0])
        seen: set[Point] = set()
        path = [root]
        result: list[str] = []


        def find(i: int, j: int):
            if not (0 <= i < m and 0 <= j < n):
                return
            if not len(path[-1].children):
                return
            if (i, j) in seen:
                return

            char = board[i][j]
            prev_trie = path[-1]

            if not prev_trie.has(char) or not prev_trie.count:
                return

            curr_trie = prev_trie.get_or_create(char)
            if curr_trie.ending:
                result.append(curr_trie.ending)
                for t in path:
                    t.count -= 1
                curr_trie.ending = None

            seen.add((i, j))
            path.append(curr_trie)

            for di, dj in Solution.directions:
                find(i + di, j + dj)

            path.pop()
            seen.remove((i, j))


        for i in range(m):
            for j in range(n):
                find(i, j)
        return result


    def build_trie(self, words: list[str]):
        root = TrieNode('')
        root.count = len(words)

        for w in words:
            curr = root
            for c in w:
                curr = curr.get_or_create(c)
                curr.count += 1
            curr.ending = w

        return root

class TrieNode:
    def __init__(self, char: str) -> None:
        self.ending: Optional[str] = None
        self.count = 0
        self.children: dict[str, 'TrieNode'] = dict()
        self.char = char


    def has(self, char: str):
        return char in self.children


    def get_or_create(self, char: str):
        if char not in self.children:
            self.children[char] = TrieNode(char)
        return self.children[char]
# @lc code=end

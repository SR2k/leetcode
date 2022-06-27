#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#
# https://leetcode.cn/problems/word-search-ii/description/
#
# algorithms
# Hard (45.63%)
# Likes:    664
# Dislikes: 0
# Total Accepted:    75.9K
# Total Submissions: 166.4K
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
DIRECTIONS = (1, 0), (-1, 0), (0, 1), (0, -1)


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        m, n = len(board), len(board[0])
        result = []

        root_trie = {}
        for word in words:
            curr = root_trie
            for char in word:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            curr['#'] = word

        def find(trie: dict, i, j, seen):
            if '#' in trie:
                result.append(trie['#'])
                trie.pop('#')

            if not (0 <= i < m and 0 <= j < n):
                return
            if board[i][j] not in trie:
                return
            if (i, j) in seen:
                return

            next_trie = trie[board[i][j]]

            seen.add((i, j))
            for di, dj in DIRECTIONS:
                find(next_trie, i + di, j + dj, seen)
            seen.remove((i, j))


        for i in range(m):
            for j in range(n):
                find(root_trie, i, j, set())

        return result
# @lc code=end

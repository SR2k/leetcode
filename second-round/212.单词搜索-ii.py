#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#
# https://leetcode-cn.com/problems/word-search-ii/description/
#
# algorithms
# Hard (46.40%)
# Likes:    608
# Dislikes: 0
# Total Accepted:    68.1K
# Total Submissions: 146.7K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
#  '["oath","pea","eat","rain"]'
#
# 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。
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
# 1 
# board[i][j] 是一个小写英文字母
# 1 
# 1 
# words[i] 由小写英文字母组成
# words 中的所有字符串互不相同
# 
# 
#

# @lc code=start
DIRECTIONS = (0, 1), (0, -1), (1, 0), (-1, 0)


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root_trie = {}
        for word in words:
            curr = root_trie
            for char in word:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            curr['#'] = word

        m, n = len(board), len(board[0])
        result = set()
        seen: set[tuple[int, int]] = set()

        def helper(i: int, j: int, trie: dict):
            if not 0 <= i < m or not 0 <= j < n:
                return
            if (i, j) in seen:
                return
            if board[i][j] not in trie:
                return
            seen.add((i, j))
            trie = trie[board[i][j]]

            if '#' in trie:
                result.add(trie['#'])

            for di, dj in DIRECTIONS:
                helper(i + di, j + dj, trie)

            seen.remove((i, j))

        for i in range(m):
            for j in range(n):
                helper(i, j, root_trie)

        return list(result)
# @lc code=end

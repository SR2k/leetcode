#
# @lc app=leetcode.cn id=959 lang=python3
#
# [959] 由斜杠划分区域
#
# https://leetcode-cn.com/problems/regions-cut-by-slashes/description/
#
# algorithms
# Medium (74.36%)
# Likes:    267
# Dislikes: 0
# Total Accepted:    19K
# Total Submissions: 25.5K
# Testcase Example:  '[" /","/ "]'
#
# 在由 1 x 1 方格组成的 N x N 网格 grid 中，每个 1 x 1 方块由 /、\ 或空格构成。这些字符会将方块划分为一些共边的区域。
# 
# （请注意，反斜杠字符是转义的，因此 \ 用 "\\" 表示。）。
# 
# 返回区域的数目。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：
# [
# " /",
# "/ "
# ]
# 输出：2
# 解释：2x2 网格如下：
# 
# 
# 示例 2：
# 
# 输入：
# [
# " /",
# "  "
# ]
# 输出：1
# 解释：2x2 网格如下：
# 
# 
# 示例 3：
# 
# 输入：
# [
# "\\/",
# "/\\"
# ]
# 输出：4
# 解释：（回想一下，因为 \ 字符是转义的，所以 "\\/" 表示 \/，而 "/\\" 表示 /\。）
# 2x2 网格如下：
# 
# 
# 示例 4：
# 
# 输入：
# [
# "/\\",
# "\\/"
# ]
# 输出：5
# 解释：（回想一下，因为 \ 字符是转义的，所以 "/\\" 表示 /\，而 "\\/" 表示 \/。）
# 2x2 网格如下：
# 
# 
# 示例 5：
# 
# 输入：
# [
# "//",
# "/ "
# ]
# 输出：3
# 解释：2x2 网格如下：
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= grid.length == grid[0].length <= 30
# grid[i][j] 是 '/'、'\'、或 ' '。
# 
# 
#

# @lc code=start
class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        parents = []
        m, n = len(grid), len(grid[0])

        def find_root(n: int):
            while parents[n] != n and parents[n] != -1:
                n = parents[n]
            return n

        sub_grids = [[[-1, -1, -1, -1] for _ in range(n)] for __ in range(m)]

        def combine(i: int, j: int):
            char = grid[i][j]
            s = sub_grids[i][j]

            if i > 0:
                s[0] = sub_grids[i - 1][j][2]
            else:
                s[0] = len(parents)
                parents.append(-1)

            if j > 0:
                s[3] = sub_grids[i][j - 1][1]
            else:
                s[3] = len(parents)
                parents.append(-1)

            if char == '\\':
                s[1] = s[0]
                s[2] = s[3]
            elif char == '/':
                parents[find_root(s[0])] = find_root(s[3])
                n = len(parents)
                s[1] = s[2] = n
                parents.append(-1)
            else:
                parents[find_root(s[0])] = find_root(s[3])
                s[1] = s[2] = s[0]

        for i in range(m):
            for j in range(n):
                combine(i, j)

        count = 0
        for i, p in enumerate(parents):
            if p == -1 or p == i:
                count += 1
        return count
# @lc code=end


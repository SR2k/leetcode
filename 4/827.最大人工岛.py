#
# @lc app=leetcode.cn id=827 lang=python3
#
# [827] 最大人工岛
#
# https://leetcode-cn.com/problems/making-a-large-island/description/
#
# algorithms
# Hard (39.42%)
# Likes:    144
# Dislikes: 0
# Total Accepted:    12.4K
# Total Submissions: 31.4K
# Testcase Example:  '[[1,0],[0,1]]'
#
# 给你一个大小为 n x n 二进制矩阵 grid 。最多 只能将一格 0 变成 1 。
# 
# 返回执行此操作后，grid 中最大的岛屿面积是多少？
# 
# 岛屿 由一组上、下、左、右四个方向相连的 1 形成。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: grid = [[1, 0], [0, 1]]
# 输出: 3
# 解释: 将一格0变成1，最终连通两个小岛得到面积为 3 的岛屿。
# 
# 
# 示例 2:
# 
# 
# 输入: grid = [[1, 1], [1, 0]]
# 输出: 4
# 解释: 将一格0变成1，岛屿的面积扩大为 4。
# 
# 示例 3:
# 
# 
# 输入: grid = [[1, 1], [1, 1]]
# 输出: 4
# 解释: 没有0可以让我们变成1，面积依然为 4。
# 
# 
# 
# 提示：
# 
# 
# n == grid.length
# n == grid[i].length
# 1 
# grid[i][j] 为 0 或 1
# 
# 
#

# @lc code=start
Point = tuple[int, int]


class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        size: dict[Point, int] = {}
        root: dict[Point, Point] = {}
        m, n = len(grid), len(grid[0])

        seen = set()
        def visit(i: int, j: int, r: Point):
            if not (0 <= i < m and 0 <= j < n):
                return 0
            if grid[i][j] == 0:
                return 0
            if (i, j) in seen:
                return 0

            seen.add((i, j))
            result = 1

            for di, dj in (1, 0), (-1, 0), (0, 1), (0, -1):
                ni, nj = i + di, j + dj
                result += visit(ni, nj, r)

            if (i, j) == r:
                size[r] = result

            root[(i, j)] = r
            return result


        for i in range(m):
            for j in range(n):
                visit(i, j, (i, j))


        result = max(size.values() or [0])
        if result == 0:
            return 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    continue

                seen_root = set()
                curr_size = 1

                for di, dj in (1, 0), (-1, 0), (0, 1), (0, -1):
                    ni, nj = i + di, j + dj

                    if not (0 <= ni < m and 0 <= nj < n):
                        continue
                    if grid[ni][nj] != 1:
                        continue
                    r = root[(ni, nj)]

                    # print('merge', (i, j), (ni, nj))
                    if r in seen_root:
                        continue
                    seen_root.add(r)
                    curr_size += size[r]

                result = max(result, curr_size)

        return result
# @lc code=end

s = Solution()
print(s.largestIsland([[1,0],[1,0]]))
print(s.largestIsland([[0,0],[0,1]]))
print(s.largestIsland([[1]]))
print(s.largestIsland([[1,1],[1,0]]))

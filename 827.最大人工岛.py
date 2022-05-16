#
# @lc app=leetcode.cn id=827 lang=python3
#
# [827] 最大人工岛
#
# https://leetcode.cn/problems/making-a-large-island/description/
#
# algorithms
# Hard (39.45%)
# Likes:    149
# Dislikes: 0
# Total Accepted:    13.1K
# Total Submissions: 33.2K
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

DIRECTIONS = (1, 0), (-1, 0), (0, 1), (0, -1)
ISLAND = 1


Point = tuple[int, int]


class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        root: dict[Point, Point] = {}
        size: dict[Point, int] = {}
        seen: set[Point] = set()


        def walk(entry: Point):
            cnt = 0
            stack = [entry]
            seen.add(entry)

            while stack:
                i, j = stack.pop()
                cnt += 1
                root[(i, j)] = entry

                for di, dj in DIRECTIONS:
                    ni, nj = i + di, j + dj

                    if not (0 <= ni < m and 0 <= nj < n):
                        continue
                    if grid[ni][nj] != ISLAND:
                        continue
                    if (ni, nj) in seen:
                        continue

                    seen.add((ni, nj))
                    stack.append((ni, nj))

            size[entry] = cnt


        for i in range(m):
            for j in range(n):
                if grid[i][j] == ISLAND and (i, j) not in seen:
                    walk((i, j))

        # print(root, size)

        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == ISLAND:
                    result = max(size[root[(i, j)]], result)
                else:
                    around = set()

                    for di, dj in DIRECTIONS:
                        if (i + di, j + dj) in root:
                            around.add(root[(i + di, j + dj)])

                    # print(around)

                    curr = 1
                    for r in around:
                        curr += size[r]

                    result = max(curr, result)

        return result
# @lc code=end

s = Solution()
print(s.largestIsland([[1, 0], [0, 1]]))
print(s.largestIsland([[1, 1], [1, 0]]))
print(s.largestIsland([[1, 1], [1, 1]]))

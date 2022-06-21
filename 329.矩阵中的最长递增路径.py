#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] 矩阵中的最长递增路径
#
# https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (50.39%)
# Likes:    655
# Dislikes: 0
# Total Accepted:    75.9K
# Total Submissions: 150.5K
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# 给定一个 m x n 整数矩阵 matrix ，找出其中 最长递增路径 的长度。
# 
# 对于每个单元格，你可以往上，下，左，右四个方向移动。 你 不能 在 对角线 方向上移动或移动到 边界外（即不允许环绕）。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix = [[9,9,4],[6,6,8],[2,1,1]]
# 输出：4 
# 解释：最长递增路径为 [1, 2, 6, 9]。
# 
# 示例 2：
# 
# 
# 输入：matrix = [[3,4,5],[3,2,6],[2,2,1]]
# 输出：4 
# 解释：最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
# 
# 
# 示例 3：
# 
# 
# 输入：matrix = [[1]]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 
# 0 
# 
# 
#

# @lc code=start
DIRECTIONS = (0, 1), (0, -1), (1, 0), (-1, 0)
INF = float('inf')


# from collections import defaultdict, deque
#
#
# class Solution:
#     def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
#         children = defaultdict(list)
#         dependency_count = defaultdict(int)
#         m, n = len(matrix), len(matrix[0])

#         result = 1
#         max_cnt = defaultdict(int)
#         queue = deque()

#         for i in range(m):
#             for j in range(n):
#                 for di, dj in DIRECTIONS:
#                     ni, nj = i + di, j + dj
#                     if not ((0 <= ni < m) and (0 <= nj < n)):
#                         continue
#                     if matrix[ni][nj] < matrix[i][j]:
#                         children[(ni, nj)].append((i, j))
#                         dependency_count[(i, j)] += 1

#                 if not dependency_count[(i, j)]:
#                     max_cnt[(i, j)] = 1
#                     queue.append((i, j, 1))

#         while queue:
#             i, j, cnt = queue.popleft()
#             result = max(result, cnt)

#             for child in children[(i, j)]:
#                 dependency_count[child] -= 1
#                 max_cnt[child] = max(max_cnt[child], cnt + 1)

#                 if dependency_count[child] == 0:
#                     ci, cj = child
#                     queue.append((ci, cj, max_cnt[child]))

#         # print(max_cnt)
#         return result


class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        memo: dict[tuple[int, int], int] = {}
        m, n = len(matrix), len(matrix[0])

        def helper(i: int, j: int):
            if (i, j) in memo:
                return memo[(i, j)]

            result = 1

            for di, dj in DIRECTIONS:
                ni, nj = i + di, j + dj

                if not (0 <= ni < m and 0 <= nj < n):
                    continue
                if matrix[ni][nj] >= matrix[i][j]:
                    continue
                result = max(result, helper(ni, nj) + 1)

            memo[(i, j)] = result
            return result

        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, helper(i, j))

        return result
# @lc code=end

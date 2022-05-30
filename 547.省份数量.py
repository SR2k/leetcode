#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#
# https://leetcode.cn/problems/number-of-provinces/description/
#
# algorithms
# Medium (62.07%)
# Likes:    793
# Dislikes: 0
# Total Accepted:    212.3K
# Total Submissions: 342K
# Testcase Example:  '[[1,1,0],[1,1,0],[0,0,1]]'
#
# 
# 
# 有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c
# 间接相连。
# 
# 省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
# 
# 给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而
# isConnected[i][j] = 0 表示二者不直接相连。
# 
# 返回矩阵中 省份 的数量。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# 输出：2
# 
# 
# 示例 2：
# 
# 
# 输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] 为 1 或 0
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        city_cnt = province_cnt = len(isConnected)
        parent: dict[int, int] = {}
        find_root = Solution.get_find_root(parent)

        for i in range(city_cnt):
            for j in range(city_cnt):
                if not isConnected[i][j]:
                    continue

                root_i, root_j = find_root(i), find_root(j)
                if root_i == root_j:
                    continue

                province_cnt -= 1
                parent[root_j] = root_i

        return province_cnt


    @staticmethod
    def get_find_root(parent: dict[int, int]):
        def find_root(i: int):
            while i in parent and parent[i] != i:
                i = parent[i]
            return i

        return find_root
# @lc code=end

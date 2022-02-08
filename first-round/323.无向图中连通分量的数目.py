#
# @lc app=leetcode.cn id=323 lang=python3
#
# [323] 无向图中连通分量的数目
#
# https://leetcode-cn.com/problems/number-of-connected-components-in-an-undirected-graph/description/
#
# algorithms
# Medium (63.14%)
# Likes:    89
# Dislikes: 0
# Total Accepted:    8.3K
# Total Submissions: 13.1K
# Testcase Example:  '5\n[[0,1],[1,2],[3,4]]'
#
# 给定编号从 0 到 n-1 的 n 个节点和一个无向边列表（每条边都是一对节点），请编写一个函数来计算无向图中连通分量的数目。
# 
# 示例 1:
# 
# 输入: n = 5 和 edges = [[0, 1], [1, 2], [3, 4]]
# 
# ⁠    0          3
# ⁠    |          |
# ⁠    1 --- 2    4 
# 
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: n = 5 和 edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
# 
# ⁠    0           4
# ⁠    |           |
# ⁠    1 --- 2 --- 3
# 
# 输出:  1
# 
# 
# 注意:
# 你可以假设在 edges 中不会出现重复的边。而且由于所以的边都是无向边，[0, 1] 与 [1, 0]  相同，所以它们不会同时在 edges 中出现。
# 
#

# @lc code=start
def find_root(parents: list[int], n: int) -> int:
    while parents[n] != -1:
        n = parents[n]
    return n

class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        parents = [-1 for _ in range(n)]

        for a, b in edges:
            ra, rb = find_root(parents, b), find_root(parents, a)
            if ra != rb:
                parents[ra] = rb

        ret = 0
        for p in parents:
            if p < 0:
                ret += 1

        return ret
# @lc code=end


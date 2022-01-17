#
# @lc app=leetcode.cn id=802 lang=python3
#
# [802] 找到最终的安全状态
#
# https://leetcode-cn.com/problems/find-eventual-safe-states/description/
#
# algorithms
# Medium (48.79%)
# Likes:    142
# Dislikes: 0
# Total Accepted:    9.3K
# Total Submissions: 19.1K
# Testcase Example:  '[[1,2],[2,3],[5],[0],[5],[],[]]'
#
# 在有向图中，从某个节点和每个转向处开始出发，沿着图的有向边走。如果到达的节点是终点（即它没有连出的有向边），则停止。
# 
# 如果从起始节点出发，最后必然能走到终点，就认为起始节点是 最终安全 的。更具体地说，对于最终安全的起始节点而言，存在一个自然数 k
# ，无论选择沿哪条有向边行走 ，走了不到 k 步后必能停止在一个终点上。
# 
# 返回一个由图中所有最终安全的起始节点组成的数组作为答案。答案数组中的元素应当按 升序 排列。
# 
# 该有向图有 n 个节点，按 0 到 n - 1 编号，其中 n 是 graph 的节点数。图以下述形式给出：graph[i] 是编号 j
# 节点的一个列表，满足 (i, j) 是图的一条有向边。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# 输出：[2,4,5,6]
# 解释：示意图如上。
# 
# 
# 示例 2：
# 
# 
# 输入：graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
# 输出：[4]
# 
# 
# 
# 
# 提示：
# 
# 
# n == graph.length
# 1 
# 0 
# graph[i] 按严格递增顺序排列。
# 图中可能包含自环。
# 图中边的数目在范围 [1, 4 * 10^4] 内。
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        to_degrees = [len(x) for x in graph]
        to_2_from: dict[int, list[int]] = {}
        for i, to_nodes in enumerate(graph):
            for to_node in to_nodes:
                if to_node not in to_2_from:
                    to_2_from[to_node] = [i]
                else:
                    to_2_from[to_node].append(i)

        ret: list[int] = []
        while True:
            i = to_degrees.index(0) if 0 in to_degrees else -1
            if i < 0:
                return sorted(ret)
            ret.append(i)
            to_degrees[i] -= 1
            from_nodes = to_2_from.get(i) or []
            for from_node in from_nodes:
                to_degrees[from_node] -= 1
# @lc code=end


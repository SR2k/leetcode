#
# @lc app=leetcode.cn id=785 lang=python3
#
# [785] 判断二分图
#
# https://leetcode-cn.com/problems/is-graph-bipartite/description/
#
# algorithms
# Medium (50.82%)
# Likes:    271
# Dislikes: 0
# Total Accepted:    36K
# Total Submissions: 70.8K
# Testcase Example:  '[[1,2,3],[0,2],[0,1,3],[0,2]]'
#
# 存在一个 无向图 ，图中有 n 个节点。其中每个节点都有一个介于 0 到 n - 1 之间的唯一编号。给你一个二维数组 graph ，其中
# graph[u] 是一个节点数组，由节点 u 的邻接节点组成。形式上，对于 graph[u] 中的每个 v ，都存在一条位于节点 u 和节点 v
# 之间的无向边。该无向图同时具有以下属性：
# 
# 不存在自环（graph[u] 不包含 u）。
# 不存在平行边（graph[u] 不包含重复值）。
# 如果 v 在 graph[u] 内，那么 u 也应该在 graph[v] 内（该图是无向图）
# 这个图可能不是连通图，也就是说两个节点 u 和 v 之间可能不存在一条连通彼此的路径。
# 
# 
# 二分图 定义：如果能将一个图的节点集合分割成两个独立的子集 A 和 B ，并使图中的每一条边的两个节点一个来自 A 集合，一个来自 B
# 集合，就将这个图称为 二分图 。
# 
# 如果图是二分图，返回 true ；否则，返回 false 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# 输出：false
# 解释：不能将节点分割成两个独立的子集，以使每条边都连通一个子集中的一个节点与另一个子集中的一个节点。
# 
# 示例 2：
# 
# 
# 输入：graph = [[1,3],[0,2],[1,3],[0,2]]
# 输出：true
# 解释：可以将节点分成两组: {0, 2} 和 {1, 3} 。
# 
# 
# 
# 提示：
# 
# 
# graph.length == n
# 1 
# 0 
# 0 
# graph[u] 不会包含 u
# graph[u] 的所有值 互不相同
# 如果 graph[u] 包含 v，那么 graph[v] 也会包含 u
# 
# 
#

# @lc code=start
class Node:
    def __init__(self, value: int):
        self.value = value
        self.neighbors: list[int] = []


class Graph:
    def __init__(self, edges: list[list[int]]):
        self.node_map: dict[int, Node] = {}
        for i, neighbors in enumerate(edges):
            for neighbor in neighbors:
                self.get_node(i).neighbors.append(neighbor)

    def get_node(self, value: int):
        if not value in self.node_map:
            self.node_map[value] = Node(value)
        return self.node_map[value]


class Solution:
    def isBipartite(self, neighbors: list[list[int]]) -> bool:
        n = len(neighbors)
        not_visited = set(range(n))
        graph = Graph(neighbors)
        queue = [0]
        visited_0: set[int] = set(queue)
        visited_1: set[int] = set()
        curr_group = 0

        while not_visited:
            queue = [not_visited.pop()]

            while queue:
                level_length = len(queue)
                curr_group = 1 - curr_group

                for _ in range(level_length):
                    curr = graph.get_node(queue.pop(0))
                    if curr.value in not_visited:
                        not_visited.remove(curr.value)
                    for next_val in curr.neighbors:
                        if curr_group == 0:
                            if next_val in visited_1: return False
                            if next_val not in visited_0:
                                visited_0.add(next_val)
                                queue.append(next_val)
                        if curr_group == 1:
                            if next_val in visited_0: return False
                            if next_val not in visited_1:
                                visited_1.add(next_val)
                                queue.append(next_val)

        return True
# @lc code=end

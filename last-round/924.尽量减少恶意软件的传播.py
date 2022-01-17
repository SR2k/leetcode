#
# @lc app=leetcode.cn id=924 lang=python3
#
# [924] 尽量减少恶意软件的传播
#
# https://leetcode-cn.com/problems/minimize-malware-spread/description/
#
# algorithms
# Hard (35.96%)
# Likes:    67
# Dislikes: 0
# Total Accepted:    6.8K
# Total Submissions: 19K
# Testcase Example:  '[[1,1,0],[1,1,0],[0,0,1]]\n[0,1]'
#
# 在节点网络中，只有当 graph[i][j] = 1 时，每个节点 i 能够直接连接到另一个节点 j。
# 
# 一些节点 initial
# 最初被恶意软件感染。只要两个节点直接连接，且其中至少一个节点受到恶意软件的感染，那么两个节点都将被恶意软件感染。这种恶意软件的传播将继续，直到没有更多的节点可以被这种方式感染。
# 
# 假设 M(initial) 是在恶意软件停止传播之后，整个网络中感染恶意软件的最终节点数。
# 
# 如果从初始列表中移除某一节点能够最小化 M(initial)， 返回该节点。如果有多个节点满足条件，就返回索引最小的节点。
# 
# 请注意，如果某个节点已从受感染节点的列表 initial 中删除，它以后可能仍然因恶意软件传播而受到感染。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：graph = [[1,1,0],[1,1,0],[0,0,1]], initial = [0,1]
# 输出：0
# 
# 
# 示例 2：
# 
# 
# 输入：graph = [[1,0,0],[0,1,0],[0,0,1]], initial = [0,2]
# 输出：0
# 
# 
# 示例 3：
# 
# 
# 输入：graph = [[1,1,1],[1,1,1],[1,1,1]], initial = [1,2]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 < graph.length = graph[0].length <= 300
# 0 <= graph[i][j] == graph[j][i] <= 1
# graph[i][i] == 1
# 1 <= initial.length < graph.length
# 0 <= initial[i] < graph.length
# 
# 
#

# @lc code=start
from collections import defaultdict, deque


class Solution:
    def minMalwareSpread(self, graph: list[list[int]], initial: list[int]) -> int:
        children: defaultdict[int, set[int]] = defaultdict(set)
        n = len(graph)

        for i in range(n):
            for j in range(i + 1, n):
                if graph[i][j] == 0:
                    continue
                children[i].add(j)
                children[j].add(i)

        initial_affected = set(initial)

        visited: set[int] = set()
        count = [0 for _ in range(n)]
        affected_count = [0 for _ in range(n)]

        for i in range(n):
            if i in visited:
                continue

            visited.add(i)

            curr_count, curr_affected_count = 0, 0
            result = []
            queue = deque([i])

            while queue:
                curr = queue.popleft()
                result.append(curr)
                curr_count += 1

                if curr in initial_affected:
                    curr_affected_count += 1

                for child in children[curr]:
                    if child in visited:
                        continue
                    visited.add(child)
                    queue.append(child)

            for r in result:
                count[r] = curr_count
                affected_count[r] = curr_affected_count

        max_decrease, result_i = 0, initial[0]
        for affected in initial:
            decrease = 0
            if affected_count[affected] == 1:
                decrease = count[affected]

            if decrease > max_decrease or (decrease == max_decrease and affected < result_i):
                result_i = affected
                max_decrease = decrease

        return result_i
# @lc code=end

s = Solution()
print(s.minMalwareSpread(graph = [[1,1,0],[1,1,0],[0,0,1]], initial = [0,1]))
print(s.minMalwareSpread(graph = [[1,0,0],[0,1,0],[0,0,1]], initial = [0,2]))
print(s.minMalwareSpread(graph = [[1,1,1],[1,1,1],[1,1,1]], initial = [1,2]))
print(s.minMalwareSpread([[1,0,0,0],[0,1,0,0],[0,0,1,1],[0,0,1,1]], [3,1]))
print(s.minMalwareSpread([[1,0,0,0,1,0,0,0,0,0,1],[0,1,0,1,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,1,0,0,0],[0,1,0,1,0,1,0,0,0,0,0],[1,0,0,0,1,0,0,0,0,0,0],[0,0,0,1,0,1,0,0,1,1,0],[0,0,0,0,0,0,1,1,0,0,0],[0,0,1,0,0,0,1,1,0,0,0],[0,0,0,0,0,1,0,0,1,0,0],[0,0,0,0,0,1,0,0,0,1,0],[1,0,0,0,0,0,0,0,0,0,1]], [7,8,6,2,3])) # 2

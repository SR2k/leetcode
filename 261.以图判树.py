#
# @lc app=leetcode.cn id=261 lang=python3
#
# [261] 以图判树
#
# https://leetcode-cn.com/problems/graph-valid-tree/description/
#
# algorithms
# Medium (49.78%)
# Likes:    147
# Dislikes: 0
# Total Accepted:    9.6K
# Total Submissions: 19.3K
# Testcase Example:  '5\n[[0,1],[0,2],[0,3],[1,4]]'
#
# 给定从 0 到 n-1 标号的 n 个结点，和一个无向边列表（每条边以结点对来表示），请编写一个函数用来判断这些边是否能够形成一个合法有效的树结构。
# 
# 示例 1：
# 
# 输入: n = 5, 边列表 edges = [[0,1], [0,2], [0,3], [1,4]]
# 输出: true
# 
# 示例 2:
# 
# 输入: n = 5, 边列表 edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# 输出: false
# 
# 注意：你可以假定边列表 edges 中不会出现重复的边。由于所有的边是无向边，边 [0,1] 和边 [1,0] 是相同的，因此不会同时出现在边列表
# edges 中。
# 
#

# @lc code=start
from collections import defaultdict, deque


class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        children: defaultdict[int, set[int]] = defaultdict(set)

        for a, b in edges:
            children[a].add(b)
            children[b].add(a)

        queue, seen = deque([0]), set([0])
        while queue:
            curr = queue.popleft()
            children_list = list(children[curr])

            for child in children_list:
                children[child].remove(curr)
                children[curr].remove(child)

                if child in seen:
                    return False

                seen.add(child)
                queue.append(child)

        return len(seen) == n
# @lc code=end

s = Solution()
print(s.validTree(5, [[0,1], [0,2], [0,3], [1,4]]))
print(s.validTree(5, [[0,1], [1,2], [2,3], [1,3], [1,4]]))

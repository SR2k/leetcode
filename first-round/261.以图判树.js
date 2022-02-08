/*
 * @lc app=leetcode.cn id=261 lang=javascript
 *
 * [261] 以图判树
 *
 * https://leetcode-cn.com/problems/graph-valid-tree/description/
 *
 * algorithms
 * Medium (49.85%)
 * Likes:    109
 * Dislikes: 0
 * Total Accepted:    6.7K
 * Total Submissions: 13.4K
 * Testcase Example:  '5\n[[0,1],[0,2],[0,3],[1,4]]'
 *
 * 给定从 0 到 n-1 标号的 n 个结点，和一个无向边列表（每条边以结点对来表示），请编写一个函数用来判断这些边是否能够形成一个合法有效的树结构。
 * 
 * 示例 1：
 * 
 * 输入: n = 5, 边列表 edges = [[0,1], [0,2], [0,3], [1,4]]
 * 输出: true
 * 
 * 示例 2:
 * 
 * 输入: n = 5, 边列表 edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
 * 输出: false
 * 
 * 注意：你可以假定边列表 edges 中不会出现重复的边。由于所有的边是无向边，边 [0,1] 和边 [1,0] 是相同的，因此不会同时出现在边列表
 * edges 中。
 * 
 */

// @lc code=start
/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {boolean}
 */
var validTree = function(n, edges) {
  if (n - 1 !== edges.length) return false

  class Graph {
    constructor(edges) {
      this.neighborsMap = {}

      for (const edge of edges) {
        const [v1, v2] = edge
        if (!this.neighborsMap[v1]) this.neighborsMap[v1] = new Set()
        if (!this.neighborsMap[v2]) this.neighborsMap[v2] = new Set()
        this.neighborsMap[v1].add(v2)
        this.neighborsMap[v2].add(v1)
      }
    }

    getNeighbors(idx) {
      return Array.from(this.neighborsMap[idx] || [])
    }
  }

  const graph = new Graph(edges)
  const set = new Set()
  const queue = [0]
  set.add(queue[0])

  while (queue.length) {
    const point = queue.shift()
    const neighbors = graph.getNeighbors(point)
    for (const n of neighbors) {
      if (set.has(n)) continue
      set.add(n)
      queue.push(n)
    }
  }

  return set.size === n
};
// @lc code=end


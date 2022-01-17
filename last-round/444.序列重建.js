/*
 * @lc app=leetcode.cn id=444 lang=javascript
 *
 * [444] 序列重建
 *
 * https://leetcode-cn.com/problems/sequence-reconstruction/description/
 *
 * algorithms
 * Medium (24.03%)
 * Likes:    36
 * Dislikes: 0
 * Total Accepted:    2.6K
 * Total Submissions: 10.9K
 * Testcase Example:  '[1,2,3]\r\n[[1,2],[1,3]]\r'
 *
 * 验证原始的序列 org 是否可以从序列集 seqs 中唯一地重建。序列 org 是 1 到 n 整数的排列，其中 1 ≤ n ≤
 * 10^4。重建是指在序列集 seqs 中构建最短的公共超序列。（即使得所有  seqs 中的序列都是该最短序列的子序列）。确定是否只可以从 seqs
 * 重建唯一的序列，且该序列就是 org 。
 * 
 * 示例 1：
 * 
 * 输入：
 * org: [1,2,3], seqs: [[1,2],[1,3]]
 * 
 * 输出：
 * false
 * 
 * 解释：
 * [1,2,3] 不是可以被重建的唯一的序列，因为 [1,3,2] 也是一个合法的序列。
 * 
 * 
 * 
 * 
 * 示例 2：
 * 
 * 输入：
 * org: [1,2,3], seqs: [[1,2]]
 * 
 * 输出：
 * false
 * 
 * 解释：
 * 可以重建的序列只有 [1,2]。
 * 
 * 
 * 
 * 
 * 示例 3：
 * 
 * 输入：
 * org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]
 * 
 * 输出：
 * true
 * 
 * 解释：
 * 序列 [1,2], [1,3] 和 [2,3] 可以被唯一地重建为原始的序列 [1,2,3]。
 * 
 * 
 * 
 * 
 * 示例 4：
 * 
 * 输入：
 * org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]
 * 
 * 输出：
 * true
 * 
 * 
 */

// @lc code=start
class SequenceGraph {
  inDegreeMap = {}
  postNodesMap = {}
  nodes = new Set()

  constructor(seqs) {
    const edgeExpressionSet = new Set()

    for (const seq of seqs) {
      if (seq.length === 1) this.nodes.add(seq[0])

      for (let i = 0; i < seq.length - 1; i++) {
        const pre = seq[i], post = seq[i + 1]

        this.nodes.add(pre)
        this.nodes.add(post)

        const edgeExpression = [pre, post].join(',')
        if (edgeExpressionSet.has(edgeExpression)) continue
        edgeExpressionSet.add(edgeExpression)

        this.inDegreeMap[post] = (this.inDegreeMap[post] || 0) + 1
        this.postNodesMap[pre] = (this.postNodesMap[pre] || []).concat(post)
      }
    }
  }

  getEntrances() {
    return Array.from(this.nodes).filter(x => !this.inDegreeMap[x])
  }

  passAndGet0InDegreeNeighbours(node) {
    const allNeighbours = this.postNodesMap[node] || []
    const ret = []
    allNeighbours.forEach(neighbour => {
      this.inDegreeMap[neighbour]--
      if (!this.inDegreeMap[neighbour]) ret.push(neighbour)
    })

    return ret
  }
}

/**
 * @param {number[]} org
 * @param {number[][]} seqs
 * @return {boolean}
 */
var sequenceReconstruction = function(org, seqs) {
  if (!seqs.length) return org.length === 0

  const sequenceGraph = new SequenceGraph(seqs)
  const entrance = sequenceGraph.getEntrances()

  // console.log(entrance, sequenceGraph.nodes, sequenceGraph.inDegreeMap)
  if (sequenceGraph.nodes.size !== 1 && entrance.length !== 1) return false
  if (sequenceGraph.nodes.size !== org.length) return false

  let pointer = 0
  const queue = [...entrance]
  const ret = []

  while (queue.length) {
    const node = queue.shift()
    // console.log(node, org, pointer, org[pointer])
    if (node !== org[pointer]) return false
    pointer++

    ret.push(node)

    const zeroInDegreeNeighbours = sequenceGraph.passAndGet0InDegreeNeighbours(node)
    // console.log('zeroInDegreeNeighbours of ' + node, zeroInDegreeNeighbours)
    if (zeroInDegreeNeighbours.length !== 1 && ret.length !== org.length) return false
    queue.push(...zeroInDegreeNeighbours)
  }

  // console.log(ret, org)

  return ret.length === org.length
};
// @lc code=end

// console.log(sequenceReconstruction(
//   [1], [[1],[1],[1]]
// ))


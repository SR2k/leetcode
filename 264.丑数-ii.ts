/*
 * @lc app=leetcode.cn id=264 lang=typescript
 *
 * [264] 丑数 II
 *
 * https://leetcode-cn.com/problems/ugly-number-ii/description/
 *
 * algorithms
 * Medium (57.07%)
 * Likes:    664
 * Dislikes: 0
 * Total Accepted:    83.6K
 * Total Submissions: 146.2K
 * Testcase Example:  '10'
 *
 * 给你一个整数 n ，请你找出并返回第 n 个 丑数 。
 * 
 * 丑数 就是只包含质因数 2、3 和/或 5 的正整数。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：n = 10
 * 输出：12
 * 解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：n = 1
 * 输出：1
 * 解释：1 通常被视为丑数。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 
 * 
 * 
 */

// @lc code=start
/*
class PriorityQueue {
  private static parent = i => ((i + 1) >>> 1) - 1;
  private static left = i => (i << 1) + 1;
  private static right = i => (i + 1) << 1;

  private top = 0;
  private heap: number[] = []
  private savedMap: Record<number, boolean> = {}

  constructor(private readonly comparator = (a, b) => a > b) {
    this.heap = [];
  }

  size() {
    return this.heap.length;
  }

  isEmpty() {
    return this.size() == 0;
  }

  peek() {
    return this.heap[this.top];
  }

  push(...values) {
    values.forEach(value => {
      if (this.savedMap[value]) return
      this.savedMap[value] = true

      this.heap.push(value);
      this.shiftUp();
    });
    return this.size();
  }

  pop() {
    const poppedValue = this.peek();
    const bottom = this.size() - 1;
    if (bottom > this.top) {
      this.swap(this.top, bottom);
    }
    this.heap.pop();
    this.shiftDown();
    return poppedValue;
  }

  replace(value) {
    const replacedValue = this.peek();
    this.heap[this.top] = value;
    this.shiftDown();
    return replacedValue;
  }

  private greater(i, j) {
    return this.comparator(this.heap[i], this.heap[j]);
  }

  private swap(i, j) {
    [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
  }

  private shiftUp() {
    let node = this.size() - 1;
    while (node > this.top && this.greater(node, PriorityQueue.parent(node))) {
      this.swap(node, PriorityQueue.parent(node));
      node = PriorityQueue.parent(node);
    }
  }

  private shiftDown() {
    let node = this.top;
    while (
      (PriorityQueue.left(node) < this.size() && this.greater(PriorityQueue.left(node), node)) ||
      (PriorityQueue.right(node) < this.size() && this.greater(PriorityQueue.right(node), node))
    ) {
      let maxChild = (PriorityQueue.right(node) < this.size() && this.greater(PriorityQueue.right(node), PriorityQueue.left(node))) ? PriorityQueue.right(node) : PriorityQueue.left(node);
      this.swap(node, maxChild);
      node = maxChild;
    }
  }
}

function nthUglyNumber(n: number): number {
  const pq = new PriorityQueue((a, b) => b > a)

  let i = 1
  let ret = 1
  while (i < n) {
    pq.push(ret * 2, ret * 3, ret * 5)
    ret = pq.pop()
    i++
  }

  return ret
};
*/
function nthUglyNumber(n: number): number {
  const dp = [1]
  let p2 = 0, p3 = 0, p5 = 0

  for (let i = 1; i < n; i++) {
    const ret2 = dp[p2] * 2
    const ret3 = dp[p3] * 3
    const ret5 = dp[p5] * 5

    dp[i] = Math.min(ret2, ret3, ret5)

    switch (dp[i]) {
      case ret2: p2++; break
      case ret3: p3++; break
      case ret5: p5++; break
    }

    if (dp[i] === dp[i - 1]) i--
  }

  return dp[n - 1]
};
// @lc code=end


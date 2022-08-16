/*
 * @lc app=leetcode.cn id=239 lang=typescript
 *
 * [239] 滑动窗口最大值
 *
 * https://leetcode.cn/problems/sliding-window-maximum/description/
 *
 * algorithms
 * Hard (49.95%)
 * Likes:    1715
 * Dislikes: 0
 * Total Accepted:    313.7K
 * Total Submissions: 628.2K
 * Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
 *
 * 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k
 * 个数字。滑动窗口每次只向右移动一位。
 *
 * 返回 滑动窗口中的最大值 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
 * 输出：[3,3,5,5,6,7]
 * 解释：
 * 滑动窗口的位置                最大值
 * ---------------               -----
 * [1  3  -1] -3  5  3  6  7       3
 * ⁠1 [3  -1  -3] 5  3  6  7       3
 * ⁠1  3 [-1  -3  5] 3  6  7       5
 * ⁠1  3  -1 [-3  5  3] 6  7       5
 * ⁠1  3  -1  -3 [5  3  6] 7       6
 * ⁠1  3  -1  -3  5 [3  6  7]      7
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [1], k = 1
 * 输出：[1]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 10^5
 * -10^4 <= nums[i] <= 10^4
 * 1 <= k <= nums.length
 *
 *
 */

export
// @lc code=start
function maxSlidingWindow(nums: number[], k: number): number[] {
  const queue = new MyQueue<number>()
  const result = []

  for (let i = 0; i < nums.length; i++) {
    while (queue.length && nums[queue.peakTail()] < nums[i]) {
      queue.pop()
    }
    while (queue.length && queue.peakHead() < i - k + 1) {
      queue.shift()
    }

    queue.append(i)
    if (i >= k - 1) {
      result.push(nums[queue.peakHead()])
    }
  }

  return result
}

class MyQueue<T> {
  private readonly dummyHead = new QueueNode<T>(-1 as any)

  private readonly dummyTail = new QueueNode<T>(-1 as any)

  public length = 0

  constructor() {
    this.dummyHead.next = this.dummyTail
    this.dummyTail.prev = this.dummyHead
  }

  private insert(
    node: QueueNode<T>,
    prev: QueueNode<T> | null,
    next: QueueNode<T> | null,
  ) {
    this.length++

    node.prev = prev
    node.next = next

    if (prev) {
      prev.next = node
    }
    if (next) {
      next.prev = node
    }
  }

  private delete(node: QueueNode<T>) {
    this.length--
    const prev = node.prev, next = node.next

    if (prev) {
      prev.next = next
    }
    if (next) {
      next.prev = prev
    }
  }

  append(value: T) {
    const node = new QueueNode(value)
    this.insert(node, this.dummyTail.prev, this.dummyTail)
  }

  shift(): T {
    if (this.length === 0) {
      throw new Error('Shifting from an empty queue')
    }

    const node = this.dummyHead.next!
    this.delete(node)
    return node.value
  }

  pop(): T {
    if (this.length === 0) {
      throw new Error('Popping from an empty queue')
    }

    const node = this.dummyTail.prev!
    this.delete(node)
    return node.value
  }

  peakTail(): T {
    if (this.length === 0) {
      throw new Error('Peaking from an empty queue')
    }

    const node = this.dummyTail.prev!
    return node.value
  }

  peakHead(): T {
    if (this.length === 0) {
      throw new Error('Peaking from an empty queue')
    }

    const node = this.dummyHead.next!
    return node.value
  }
}

class QueueNode<T> {
  constructor(
    public value: T,
    public prev: QueueNode<T> | null = null,
    public next: QueueNode<T> | null = null,
  ) {}
}
// @lc code=end

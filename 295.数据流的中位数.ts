/*
 * @lc app=leetcode.cn id=295 lang=typescript
 *
 * [295] 数据流的中位数
 *
 * https://leetcode.cn/problems/find-median-from-data-stream/description/
 *
 * algorithms
 * Hard (52.94%)
 * Likes:    735
 * Dislikes: 0
 * Total Accepted:    91.3K
 * Total Submissions: 172.4K
 * Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n' +
  '[[],[1],[2],[],[3],[]]'
 *
 * 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。
 *
 * 例如，
 *
 * [2,3,4] 的中位数是 3
 *
 * [2,3] 的中位数是 (2 + 3) / 2 = 2.5
 *
 * 设计一个支持以下两种操作的数据结构：
 *
 *
 * void addNum(int num) - 从数据流中添加一个整数到数据结构中。
 * double findMedian() - 返回目前所有元素的中位数。
 *
 *
 * 示例：
 *
 * addNum(1)
 * addNum(2)
 * findMedian() -> 1.5
 * addNum(3)
 * findMedian() -> 2
 *
 * 进阶:
 *
 *
 * 如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
 * 如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
 *
 *
 */

export
// @lc code=start
class MedianFinder {
  private readonly frontHeap = new Heap<number>([], (a, b) => b - a)

  private readonly backHeap = new Heap<number>([], (a, b) => a - b)

  addNum(num: number): void {
    if (!this.frontHeap.length || num <= this.frontHeap.peak()!) {
      this.frontHeap.push(num)
    } else {
      this.backHeap.push(num)
    }

    // 前 = 后 + 1 || 前 = 后
    if (this.frontHeap.length > this.backHeap.length + 1) {
      const t = this.frontHeap.pop()!
      this.backHeap.push(t)
    } else if (this.backHeap.length > this.frontHeap.length) {
      const t = this.backHeap.pop()!
      this.frontHeap.push(t)
    }
  }

  findMedian(): number {
    if (this.frontHeap.length > this.backHeap.length) {
      return this.frontHeap.peak()!
    }
    return (this.frontHeap.peak()! + this.backHeap.peak()!) / 2
  }
}

class Heap<T> {
  constructor(
    private readonly values: T[],
    private readonly compare: (a: T, b: T) => number,
  ) {
    this.heapifty()
  }

  public push(value: T): void {
    this.values.push(value)
    this.shiftUp(this.length - 1)
  }

  public pop(): T | undefined {
    if (!this.length) return undefined

    this.swap(0, this.length - 1)
    const result = this.values.pop()!
    this.shiftDown(0)
    return result
  }

  public peak(): T | undefined {
    return this.length ? this.values[0] : undefined
  }

  public get length() {
    return this.values.length
  }

  private shiftUp(childIndex: number) {
    while (true) {
      const parentIndex = Heap.parentIndex(childIndex)
      if (!this.shouldSwap(parentIndex, childIndex)) break

      this.swap(parentIndex, childIndex)
      childIndex = parentIndex
    }
  }

  private shiftDown(parentIndex: number) {
    while (true) {
      const childIndex = this.pickChild(parentIndex)
      if (!this.shouldSwap(parentIndex, childIndex)) break

      this.swap(parentIndex, childIndex)
      parentIndex = childIndex
    }
  }

  private heapifty() {
    for (let i = 0; i < this.length; i++) {
      this.shiftUp(i)
    }
  }

  private static childrenIndex(i: number): [number, number] {
    const left = i * 2 + 1
    return [left, left + 1]
  }

  private static parentIndex(i: number) {
    return (i - 1) >> 1
  }

  private pickChild(i: number) {
    const [left, right] = Heap.childrenIndex(i)

    if (left >= this.length) return -1
    if (right >= this.length) return left

    return this.compare(this.values[left], this.values[right]) <= 0
      ? left
      : right
  }

  private shouldSwap(parentIndex: number, childIndex: number) {
    if (parentIndex < 0 || parentIndex >= this.length) {
      return false
    }
    if (childIndex < 0 || childIndex >= this.length) {
      return false
    }

    return this.compare(this.values[parentIndex], this.values[childIndex]) > 0
  }

  private swap(i: number, j: number) {
    const temp = this.values[i]
    this.values[i] = this.values[j]
    this.values[j] = temp
  }
}
// @lc code=end

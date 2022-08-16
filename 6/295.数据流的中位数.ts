/*
 * @lc app=leetcode.cn id=295 lang=typescript
 *
 * [295] 数据流的中位数
 *
 * https://leetcode.cn/problems/find-median-from-data-stream/description/
 *
 * algorithms
 * Hard (52.78%)
 * Likes:    709
 * Dislikes: 0
 * Total Accepted:    86.5K
 * Total Submissions: 163.8K
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

// [1,0,0]
// [2,2,3]

export
// @lc code=start
class MedianFinder {
  private readonly heap1 = new Heap<number>([], (a, b) => b - a)

  private readonly heap2 = new Heap<number>([], (a, b) => a - b)

  addNum(num: number): void {
    if (num > this.heap1.top) {
      this.heap2.push(num)
    } else {
      this.heap1.push(num)
    }

    if (this.heap1.length > this.heap2.length + 1) {
      this.heap2.push(this.heap1.pop())
    }
    if (this.heap2.length > this.heap1.length) {
      this.heap1.push(this.heap2.pop())
    }

    // console.log((this.heap1 as any).values, (this.heap2 as any).values)
  }

  findMedian(): number {
    if (this.heap1.length > this.heap2.length) {
      return this.heap1.top
    }
    return (this.heap1.top + this.heap2.top) / 2
  }
}

type CompareFunc<T> = (a: T, b: T) => number

class Heap<T> {
  constructor(
    private readonly values: T[],
    private readonly compare: CompareFunc<T>,
  ) {
    this.heapify()
  }

  public get length() {
    return this.values.length
  }

  private get lastIndex() {
    return this.length - 1
  }

  public get top(): T {
    return this.values[0]
  }

  public pop(): T {
    // console.log('before pop',  this.values)
    this.swap(0, this.lastIndex)
    const result = this.values.pop()!
    this.shiftDown(0)
    // console.log('after pop', result, this.values)
    return result
  }

  public push(value: T) {
    this.values.push(value)
    this.shiftUp(this.lastIndex)
  }

  private static parentIndex(i: number) {
    return Math.floor((i - 1) / 2)
  }

  private static childrenIndex(i: number): [number, number] {
    const left = i * 2 + 1
    return [left, left + 1]
  }

  private pickChild(i: number) {
    const [left, right] = Heap.childrenIndex(i)

    if (left > this.lastIndex) return -1
    if (right > this.lastIndex) return left
    return this.compare(this.values[left], this.values[right]) <= 0
      ? left
      : right
  }

  private shouldSwap(parentIndex: number, childIndex: number) {
    if (parentIndex < 0 || parentIndex > this.lastIndex) {
      return false
    }
    if (childIndex < 0 || childIndex > this.lastIndex) {
      return false
    }
    return this.compare(this.values[parentIndex], this.values[childIndex]) > 0
  }

  private swap(i: number, j: number) {
    const temp = this.values[i]
    this.values[i] = this.values[j]
    this.values[j] = temp
  }

  private shiftUp(i: number) {
    while (i > 0 && i <= this.lastIndex) {
      const parentIndex = Heap.parentIndex(i)
      if (!this.shouldSwap(parentIndex, i)) {
        break
      }
      this.swap(parentIndex, i)
      i = parentIndex
    }
  }

  private shiftDown(i: number) {
    while (i >= 0 && i <= this.lastIndex) {
      const childIndex = this.pickChild(i)
      if (!this.shouldSwap(i, childIndex)) {
        break
      }
      this.swap(i, childIndex)
      i = childIndex
    }
  }

  private heapify() {
    for (let i = 0; i < this.length; i++) {
      this.shiftUp(i)
    }
  }
}
// @lc code=end

// ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
// [[],            [-1],     [],         [-2],     [],          [-3],     [],        [-4],     [],         [-5],      []]

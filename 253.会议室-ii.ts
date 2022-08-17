/*
 * @lc app=leetcode.cn id=253 lang=typescript
 *
 * [253] 会议室 II
 *
 * https://leetcode.cn/problems/meeting-rooms-ii/description/
 *
 * algorithms
 * Medium (51.84%)
 * Likes:    458
 * Dislikes: 0
 * Total Accepted:    54K
 * Total Submissions: 104.2K
 * Testcase Example:  '[[0,30],[5,10],[15,20]]'
 *
 * 给你一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi]
 * ，返回 所需会议室的最小数量 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：intervals = [[0,30],[5,10],[15,20]]
 * 输出：2
 *
 *
 * 示例 2：
 *
 *
 * 输入：intervals = [[7,10],[2,4]]
 * 输出：1
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= intervals.length <= 10^4
 * 0 <= starti < endi <= 10^6
 *
 *
 */

// @lc code=start
class Heap<T> {
  constructor(
    private readonly values: T[],
    private readonly compare: (a: T, b: T) => number,
  ) {
    for (let i = 0; i < this.length; i++) {
      this.shiftUp(i)
    }
  }

  public push(value: T): void {
    this.values.push(value)
    this.shiftUp(this.length - 1)
  }

  public pop(): T | undefined {
    if (!this.length) {
      return undefined
    }

    this.swap(0, this.length - 1)
    const result = this.values.pop()!
    this.shiftDown(0)
    return result
  }

  public peak(): T | undefined {
    if (!this.length) {
      return undefined
    }
    return this.values[0]
  }

  public get length(): number {
    return this.values.length
  }

  private static parentIndex(i: number) {
    return Math.floor((i - 1) / 2)
  }

  private static childrenIndex(i: number): [number, number] {
    const left = i * 2 + 1
    return [left, left + 1]
  }

  private shiftUp(i: number) {
    let childIndex = i
    while (true) {
      const parentIndex = Heap.parentIndex(childIndex)
      if (!this.shouldSwap(parentIndex, childIndex)) {
        break
      }
      this.swap(parentIndex, childIndex)
      childIndex = parentIndex
    }
  }

  private shiftDown(i: number) {
    let parentIndex = i
    while (true) {
      const childIndex = this.pickChild(parentIndex)
      if (!this.shouldSwap(parentIndex, childIndex)) {
        break
      }
      this.swap(parentIndex, childIndex)
      parentIndex = childIndex
    }
  }

  private pickChild(parentIndex: number): number {
    const [left, right] = Heap.childrenIndex(parentIndex)

    if (left >= this.length) {
      return -1
    }
    if (right >= this.length) {
      return left
    }

    return this.compare(this.values[left], this.values[right]) <= 0
      ? left
      : right
  }

  private shouldSwap(parentIndex: number, childIndex: number) {
    if (parentIndex < 0 || parentIndex >= this.length) {
      return false
    }
    if (childIndex <= 0 || childIndex >= this.length) {
      return false
    }

    return this.compare(this.values[parentIndex], this.values[childIndex]) > 0
  }

  private swap(i: number, j: number) {
    const temp = this.values[j]
    this.values[j] = this.values[i]
    this.values[i] = temp
  }
}

function minMeetingRooms(intervals: number[][]): number {
  const t: Array<[number, number]> = []
  intervals.forEach(([begin, end]) => {
    t.push([begin, 1])
    t.push([end, -1])
  })

  const heap = new Heap<[number, number]>(
    t,
    (a, b) => {
      if (a[0] !== b[0]) return a[0] - b[0]
      return a[1] - b[1]
    },
  )

  let result = 0
  let curr = 0

  while (heap.length) {
    const [ts, delta] = heap.pop()!
    curr += delta
    result = Math.max(curr, result)
  }

  return result
}
// @lc code=end

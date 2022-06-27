/*
 * @lc app=leetcode.cn id=759 lang=typescript
 *
 * [759] 员工空闲时间
 *
 * https://leetcode.cn/problems/employee-free-time/description/
 *
 * algorithms
 * Hard (68.86%)
 * Likes:    81
 * Dislikes: 0
 * Total Accepted:    3.2K
 * Total Submissions: 4.6K
 * Testcase Example:  '[[[1,2],[5,6]],[[1,3]],[[4,10]]]'
 *
 * 给定员工的 schedule 列表，表示每个员工的工作时间。
 *
 * 每个员工都有一个非重叠的时间段  Intervals 列表，这些时间段已经排好序。
 *
 * 返回表示 所有 员工的 共同，正数长度的空闲时间 的有限时间段的列表，同样需要排好序。
 *
 * 示例 1：
 *
 * 输入：schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
 * 输出：[[3,4]]
 * 解释：
 * 共有 3 个员工，并且所有共同的
 * 空间时间段是 [-inf, 1], [3, 4], [10, inf]。
 * 我们去除所有包含 inf 的时间段，因为它们不是有限的时间段。
 *
 *
 *
 *
 * 示例 2：
 *
 * 输入：schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
 * 输出：[[5,6],[7,9]]
 *
 *
 *
 *
 * （尽管我们用 [x, y] 的形式表示 Intervals ，内部的对象是 Intervals
 * 而不是列表或数组。例如，schedule[0][0].start = 1, schedule[0][0].end = 2，并且
 * schedule[0][0][0] 是未定义的）
 *
 * 而且，答案中不包含 [5, 5] ，因为长度为 0。
 *
 *
 *
 * 注：
 *
 *
 * schedule 和 schedule[i] 为长度范围在 [1, 50]的列表。
 * 0 <= schedule[i].start < schedule[i].end <= 10^8。
 *
 *
 * 注：输入类型于 2019 年 4 月 15 日 改变。请重置为默认代码的定义以获取新方法。
 *
 *
 *
 */

class Interval {
  constructor(
    public readonly start: number,
    public readonly end: number,
  ) {}
}

export
// @lc code=start
function employeeFreeTime(schedule: Interval[][]): Interval[] {
  const values: Array<[number, number]> = []
  schedule.forEach((p) => {
    p.forEach((s) => {
      values.push([s.start, 1])
      values.push([s.end, -1])
    })
  })
  const heap = new Heap(
    values,
    (a, b) => {
      if (a[0] === b[0]) {
        return a[1] - b[1]
      }
      return a[0] - b[0]
    },
  )

  const result: Interval[] = []
  let curr = 0, begin = -1
  while (heap.length) {
    const [ts, delta] = heap.pop()

    curr += delta

    if (curr === 0) {
      begin = ts
    } else if (curr === 1) {
      if (ts !== begin && begin >= 0) {
        result.push(new Interval(begin, ts))
      }
      begin = -1
    }
  }

  return result
}

class Heap<T> {
  constructor(
    private readonly values: T[],
    private readonly compare: (a: T, b: T) => number,
  ) {
    this.heapify()
  }

  public pop() {
    this.swap(0, this.values.length - 1)
    const result = this.values.pop()!
    this.shiftDown(0)
    return result
  }

  public get length() {
    return this.values.length
  }

  private static parentIndex(i: number) {
    return Math.floor((i - 1) / 2)
  }

  private static childrenIndex(i: number): [number, number] {
    const left = i * 2 + 1
    return [left, left + 1]
  }

  private heapify() {
    for (let i = 0; i < this.values.length; i++) {
      this.shiftUp(i)
    }
  }

  private shiftUp(i: number) {
    if (i >= this.values.length || i < 0) return

    while (i > 0) {
      const parentIndex = Heap.parentIndex(i)
      if (!this.shouldSwap(parentIndex, i)) {
        break
      }
      this.swap(parentIndex, i)
      i = parentIndex
    }
  }

  private shiftDown(i: number) {
    if (i >= this.values.length || i < 0) return

    while (i < this.values.length) {
      const childIndex = this.pickChild(i)
      if (!this.shouldSwap(i, childIndex)) {
        break
      }
      this.swap(i, childIndex)
      i = childIndex
    }
  }

  private shouldSwap(parentIndex: number, childIndex: number) {
    if (parentIndex >= this.values.length || childIndex >= this.values.length) {
      return false
    }
    if (parentIndex < 0 || childIndex < 0) {
      return false
    }
    if (parentIndex >= childIndex) {
      return false
    }
    return this.compare(this.values[parentIndex], this.values[childIndex]) > 0
  }

  private pickChild(i: number) {
    const [left, right] = Heap.childrenIndex(i)

    if (left >= this.values.length) return -1
    if (right >= this.values.length) return left

    if (this.compare(this.values[left], this.values[right]) <= 0) {
      return left
    }
    return right
  }

  private swap(i: number, j: number) {
    const temp = this.values[i]
    this.values[i] = this.values[j]
    this.values[j] = temp
  }
}
// @lc code=end

// [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]

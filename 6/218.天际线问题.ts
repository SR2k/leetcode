/*
 * @lc app=leetcode.cn id=218 lang=typescript
 *
 * [218] 天际线问题
 *
 * https://leetcode.cn/problems/the-skyline-problem/description/
 *
 * algorithms
 * Hard (54.89%)
 * Likes:    685
 * Dislikes: 0
 * Total Accepted:    40.7K
 * Total Submissions: 74.1K
 * Testcase Example:  '[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]'
 *
 * 城市的 天际线 是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。给你所有建筑物的位置和高度，请返回 由这些建筑物形成的 天际线 。
 *
 * 每个建筑物的几何信息由数组 buildings 表示，其中三元组 buildings[i] = [lefti, righti, heighti]
 * 表示：
 *
 *
 * lefti 是第 i 座建筑物左边缘的 x 坐标。
 * righti 是第 i 座建筑物右边缘的 x 坐标。
 * heighti 是第 i 座建筑物的高度。
 *
 *
 * 你可以假设所有的建筑都是完美的长方形，在高度为 0 的绝对平坦的表面上。
 *
 * 天际线 应该表示为由 “关键点” 组成的列表，格式 [[x1,y1],[x2,y2],...] ，并按 x 坐标 进行 排序
 * 。关键点是水平线段的左端点。列表中最后一个点是最右侧建筑物的终点，y 坐标始终为 0
 * ，仅用于标记天际线的终点。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。
 *
 * 注意：输出天际线中不得有连续的相同高度的水平线。例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...]
 * 是不正确的答案；三条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...]
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
 * 输出：[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
 * 解释：
 * 图 A 显示输入的所有建筑物的位置和高度，
 * 图 B 显示由这些建筑物形成的天际线。图 B 中的红点表示输出列表中的关键点。
 *
 * 示例 2：
 *
 *
 * 输入：buildings = [[0,2,3],[2,5,3]]
 * 输出：[[0,3],[5,0]]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= buildings.length <= 10^4
 * 0 <= lefti < righti <= 2^31 - 1
 * 1 <= heighti <= 2^31 - 1
 * buildings 按 lefti 非递减排序
 *
 *
 */

export
// @lc code=start
function getSkyline(buildings: number[][]): number[][] {
  const lines: Array<[number, number, XType]> = []
  for (const [begin, end, height] of buildings) {
    lines.push([begin, height, XType.Enter])
    lines.push([end, height, XType.Exit])
  }

  const heap = new Heap(
    lines,
    (a, b) => {
      if (a[0] !== b[0]) return a[0] - b[0]
      if (a[1] !== b[1]) return a[1] - b[1]
      return a[2] - b[2]
    },
  )

  const popped = new Heap<number>([], (a, b) => b - a)
  const heights = new Heap([0], (a, b) => b - a)
  const result: number[][] = []

  while (heap.length) {
    const [x, y, type] = heap.pop()

    if (type === XType.Enter) {
      // 进入一个新的大楼，将高度 push 到高度堆中
      heights.push(y)
    } else {
      // 退出大楼，将高度 push 到退出堆中
      popped.push(y)
    }

    while (popped.length && popped.peak() === heights.peak()) {
      heights.pop()
      popped.pop()
    }

    const currHeight = heights.peak()
    if (result.length && result[result.length - 1][1] === currHeight) {
      // nothing to do...
    } else if (!result.length || result[result.length - 1][0] !== x) {
      result.push([x, currHeight])
    } else {
      const prev = result[result.length - 1]
      prev[1] = Math.max(prev[1], currHeight)
    }
  }

  return result
}

const enum XType {
  Enter,
  Exit,
}

class Heap<T> {
  constructor(
    private readonly values: T[],
    private readonly compare: (a: T, b: T) => number,
  ) {
    this.heapify()
  }

  public get length() {
    return this.values.length
  }

  public push(value: T) {
    this.values.push(value)
    this.shiftUp(this.values.length - 1)
  }

  public pop(): T {
    if (!this.length) {
      throw new Error('Popping from an empty heap')
    }

    this.swap(0, this.length - 1)
    const result = this.values.pop()!
    this.shiftDown(0)
    return result
  }

  public peak(): T {
    if (!this.length) {
      throw new Error('Peaking an empty heap')
    }

    return this.values[0]
  }

  private static parentIndex(i: number): number {
    return (i - 1) >> 1
  }

  private static childrenIndex(i: number): [number, number] {
    const left = i * 2 + 1
    return [left, left + 1]
  }

  private heapify() {
    for (let i = 0; i < this.length; i++) {
      this.shiftUp(i)
    }
  }

  private pickChild(i: number): number {
    const [left, right] = Heap.childrenIndex(i)

    if (left >= this.length) return -1
    if (right >= this.length) return left

    return this.compare(this.values[left], this.values[right]) <= 0
      ? left
      : right
  }

  private shiftUp(i: number) {
    let childIndex = i
    while (childIndex > 0 && childIndex < this.length) {
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
    while (parentIndex >= 0 && parentIndex < this.length - 1) {
      const childIndex = this.pickChild(parentIndex)
      if (!this.shouldSwap(parentIndex, childIndex)) {
        break
      }
      this.swap(parentIndex, childIndex)
      parentIndex = childIndex
    }
  }

  private shouldSwap(parentIndex: number, childIndex: number): boolean {
    if (parentIndex < 0 || parentIndex >= this.length) return false
    if (childIndex < 0 || childIndex >= this.length) return false

    return this.compare(this.values[parentIndex], this.values[childIndex]) > 0
  }

  private swap(i: number, j: number) {
    const temp = this.values[i]
    this.values[i] = this.values[j]
    this.values[j] = temp
  }
}
// @lc code=end

console.log(getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))

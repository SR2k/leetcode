/*
 * @lc app=leetcode.cn id=692 lang=typescript
 *
 * [692] 前K个高频单词
 *
 * https://leetcode.cn/problems/top-k-frequent-words/description/
 *
 * algorithms
 * Medium (56.87%)
 * Likes:    482
 * Dislikes: 0
 * Total Accepted:    89.7K
 * Total Submissions: 157.9K
 * Testcase Example:  '["i","love","leetcode","i","love","coding"]\n2'
 *
 * 给定一个单词列表 words 和一个整数 k ，返回前 k 个出现次数最多的单词。
 *
 * 返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率， 按字典顺序 排序。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入: words = ["i", "love", "leetcode", "i", "love", "coding"], k = 2
 * 输出: ["i", "love"]
 * 解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
 * ⁠   注意，按字母顺序 "i" 在 "love" 之前。
 *
 *
 * 示例 2：
 *
 *
 * 输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
 * k = 4
 * 输出: ["the", "is", "sunny", "day"]
 * 解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
 * ⁠   出现次数依次为 4, 3, 2 和 1 次。
 *
 *
 *
 *
 * 注意：
 *
 *
 * 1 <= words.length <= 500
 * 1 <= words[i] <= 10
 * words[i] 由小写英文字母组成。
 * k 的取值范围是 [1, 不同 words[i] 的数量]
 *
 *
 *
 *
 * 进阶：尝试以 O(n log k) 时间复杂度和 O(n) 空间复杂度解决。
 *
 */

export
// @lc code=start
function topKFrequent(words: string[], k: number): string[] {
  const wordSet = new Set<string>()
  const counter: Record<string, number> = {}
  for (const w of words) {
    wordSet.add(w)
    counter[w] = (counter[w] || 0) + 1
  }

  return Heap.topK(
    [...wordSet],
    (a, b) => {
      if (counter[a] !== counter[b]) {
        return counter[b] - counter[a]
      }
      return a > b ? 1 : -1
    },
    k,
  )
}

type CompareFn<T> = (a: T, b: T) => number

class Heap<T> {
  constructor(
    private readonly values: T[],
    private readonly compare: CompareFn<T>,
  ) {
    for (let i = 0; i < this.length; i++) {
      this.shiftUp(i)
    }
  }

  public static topK<U>(arr: U[], compare: CompareFn<U>, k: number) {
    const heap = new Heap(arr, compare)

    const result: U[] = []
    while (k-- && heap.length) {
      result.push(heap.pop()!)
    }
    return result
  }

  public get length() {
    return this.values.length
  }

  pop(): T | undefined {
    if (!this.length) {
      return undefined
    }

    this.swap(0, this.length - 1)
    const result = this.values.pop()!
    this.shiftDown(0)
    return result
  }

  private static getChildrenIndexOf(i: number): [number, number] {
    const left = i * 2 + 1
    return [left, left + 1]
  }

  private static getParentIndexOf(i: number) {
    return (i - 1) >> 1
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

  private shiftUp(i: number) {
    let childIndex = i
    while (true) {
      const parentIndex = Heap.getParentIndexOf(childIndex)
      if (!this.shouldSwap(parentIndex, childIndex)) {
        break
      }
      this.swap(parentIndex, childIndex)
      childIndex = parentIndex
    }
  }

  private pickChild(i: number) {
    const [left, right] = Heap.getChildrenIndexOf(i)
    if (left < 0 || left >= this.length) return -1
    if (right < 0 || right >= this.length) return left
    return this.compare(this.values[left], this.values[right]) <= 0
      ? left
      : right
  }

  private swap(i: number, j: number) {
    const temp = this.values[i]
    this.values[i] = this.values[j]
    this.values[j] = temp
  }

  private shouldSwap(parentIndex: number, childIndex: number) {
    if (parentIndex < 0 || parentIndex >= this.length) return false
    if (childIndex < 0 || childIndex >= this.length) return false
    return this.compare(this.values[parentIndex], this.values[childIndex]) > 0
  }
}
// @lc code=end

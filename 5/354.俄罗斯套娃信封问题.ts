/*
 * @lc app=leetcode.cn id=354 lang=typescript
 *
 * [354] 俄罗斯套娃信封问题
 *
 * https://leetcode.cn/problems/russian-doll-envelopes/description/
 *
 * algorithms
 * Hard (41.85%)
 * Likes:    748
 * Dislikes: 0
 * Total Accepted:    86.8K
 * Total Submissions: 208.3K
 * Testcase Example:  '[[5,4],[6,4],[6,7],[2,3]]'
 *
 * 给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。
 *
 * 当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
 *
 * 请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
 *
 * 注意：不允许旋转信封。
 *
 *
 * 示例 1：
 *
 *
 * 输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
 * 输出：3
 * 解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
 *
 * 示例 2：
 *
 *
 * 输入：envelopes = [[1,1],[1,1],[1,1]]
 * 输出：1
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= envelopes.length <= 10^5
 * envelopes[i].length == 2
 * 1 <= wi, hi <= 10^5
 *
 *
 */

export
// @lc code=start
function maxEnvelopes(envelopes: number[][]): number {
  quickSort(envelopes, (a, b) => {
    if (a[0] !== b[0]) {
      return a[0] - b[0]
    }
    return b[1] - a[1]
  })

  // console.log(envelopes)

  const top: number[] = []
  for (const [_, height] of envelopes) {
    const i = binarySearchFirstGreater(top, height, (a, b) => a - b)
    if (i < 0) {
      top.push(height)
    } else {
      top[i] = height
    }
    // console.log(top)
  }

  return top.length
}

interface CompareFunc<T> {
  (a: T, b: T): number
}

function binarySearchFirstGreater<T>(arr: T[], target: T, cmp: CompareFunc<T>) {
  if (!arr.length) return -1

  let left = 0, right = arr.length
  while (left + 1 < right) {
    const middle = Math.floor((left + right) / 2)

    if (cmp(arr[middle], target) >= 0) {
      right = middle
    } else {
      left = middle
    }
  }

  if (cmp(arr[left], target) >= 0) {
    return left
  }
  if (cmp(arr[right], target) >= 0) {
    return right
  }
  return -1
}

function quickSort<T>(arr: T[], cmp: CompareFunc<T>, left = 0, right = arr.length - 1) {
  if (left >= right) return

  const i = partition(arr, cmp, left, right)
  quickSort(arr, cmp, left, i - 1)
  quickSort(arr, cmp, i + 1, right)
}

function partition<T>(arr: T[], cmp: CompareFunc<T>, left: number, right: number) {
  const randomIndex = Math.floor(Math.random() * (right - left) + left)
  swap(arr, left, randomIndex)
  const pivotValue = arr[left]

  let i = left, j = right
  while (i < j) {
    while (i < j && cmp(arr[j], pivotValue) > 0) {
      j -= 1
    }
    while (i < j && cmp(arr[i], pivotValue) <= 0) {
      i += 1
    }
    swap(arr, i, j)
  }

  swap(arr, left, i)
  return i
}

function swap(arr: any[], i: number, j: number) {
  const temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp
}
// @lc code=end

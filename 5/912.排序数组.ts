/*
 * @lc app=leetcode.cn id=912 lang=typescript
 *
 * [912] 排序数组
 *
 * https://leetcode.cn/problems/sort-an-array/description/
 *
 * algorithms
 * Medium (55.60%)
 * Likes:    574
 * Dislikes: 0
 * Total Accepted:    375.8K
 * Total Submissions: 675.8K
 * Testcase Example:  '[5,2,3,1]'
 *
 * 给你一个整数数组 nums，请你将该数组升序排列。
 *
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [5,2,3,1]
 * 输出：[1,2,3,5]
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [5,1,1,2,0,0]
 * 输出：[0,0,1,1,2,5]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 5 * 10^4
 * -5 * 10^4 <= nums[i] <= 5 * 10^4
 *
 *
 */

/*
          0
      1       2
    3   4   5   6
*/

export
// @lc code=start
function sortArray(nums: number[]): number[] {
  // const heap = new Heap(nums, (a, b) => a - b)
  // const result = []

  // while (heap.length) {
  //   result.push(heap.pop())
  // }

  // return result

  // return mergeSort(nums, (a, b) => a - b)

  mergeIteration(nums, (a, b) => a - b)
  return nums
}

function mergeIteration<T>(arr: T[], compare: (a: T, b: T) => number) {
  const temp = arr.map((x) => x)

  for (let segment = 1; segment <= arr.length; segment += segment) {
    for (let begin = 0; begin < arr.length - segment; begin += 2 * segment) {
      const middle = begin + segment
      const nextBegin = Math.min(begin + segment * 2, arr.length)

      let a = begin, b = middle
      let i = begin

      while (a < middle || b < nextBegin) {
        if (a >= middle) {
          temp[i++] = arr[b++]
        } else if (b >= nextBegin) {
          temp[i++] = arr[a++]
        } else if (compare(arr[a], arr[b]) <= 0) {
          temp[i++] = arr[a++]
        } else {
          temp[i++] = arr[b++]
        }
      }

      // console.log('begin=', begin, 'middle=', middle, 'nextBegin=', nextBegin, arr)

      for (let x = begin; x < nextBegin; x++) {
        arr[x] = temp[x]
      }
    }
  }
}

function mergeSortRecursive<T>(arr: T[], compare: (a: T, b: T) => number) {
  if (arr.length <= 1) {
    return arr
  }

  const middle = Math.floor(arr.length / 2)
  const front = mergeSortRecursive(arr.slice(0, middle), compare)
  const end = mergeSortRecursive(arr.slice(middle, arr.length), compare)

  const result: T[] = []
  let i = 0, j = 0
  while (i < front.length || j < end.length) {
    if (i >= front.length) {
      result.push(end[j])
      j += 1
    } else if (j >= end.length) {
      result.push(front[i])
      i += 1
    } else if (compare(front[i], end[j]) <= 0) {
      result.push(front[i])
      i += 1
    } else {
      result.push(end[j])
      j += 1
    }
  }

  return result
}

class Heap<T> {
  private readonly values: T[]

  constructor(
    values: T[] | undefined,
    private readonly compare: (a: T, b: T) => number,
  ) {
    this.values = values?.length ? values : []
    this.heapify()
  }

  private heapify() {
    for (let i = 0; i < this.values.length; i++) {
      this.shiftUp(i)
    }
  }

  private static parentIndex(i: number) {
    return Math.floor((i - 1) / 2)
  }

  private static childrenIndex(i: number): [number, number] {
    const leftIndex = i * 2 + 1
    return [leftIndex, leftIndex + 1]
  }

  private chooseChild(i: number) {
    const [leftIndex, rightIndex] = Heap.childrenIndex(i)

    if (leftIndex >= this.values.length) {
      return -1
    }
    if (rightIndex >= this.values.length) {
      return leftIndex
    }
    if (this.compare(this.values[leftIndex], this.values[rightIndex]) <= 0) {
      return leftIndex
    }
    return rightIndex
  }

  private shiftUp(i: number) {
    if (i >= this.values.length) {
      return
    }

    while (i > 0) {
      const parentIndex = Heap.parentIndex(i)
      const parentValue = this.values[parentIndex]
      const value = this.values[i]

      if (this.compare(parentValue, value) >= 0) {
        this.swap(parentIndex, i)
        i = parentIndex
      } else {
        break
      }
    }
  }

  private shiftDown(i: number) {
    while (true) {
      const childIndex = this.chooseChild(i)

      if (childIndex < 0 || this.compare(this.values[childIndex], this.values[i]) >= 0) {
        break
      } else {
        this.swap(childIndex, i)
        i = childIndex
      }
    }
  }

  private swap(i: number, j: number) {
    const temp = this.values[j]
    this.values[j] = this.values[i]
    this.values[i] = temp
  }

  get length() {
    return this.values.length
  }

  pop(): T {
    const result = this.values[0]
    this.swap(0, this.values.length - 1)
    this.values.pop()
    this.shiftDown(0)
    return result
  }
}

const quickSort = <T>(arr: T[], cmp: (a: T, b: T) => number) => {
  if (!arr.length) return

  const stack: Array<[number, number]> = [[0, arr.length - 1]]

  while (stack.length) {
    const [left, right] = stack.pop()!
    const i = partition(arr, left, right, cmp)

    if (left < i - 1) {
      stack.push([left, i - 1])
    }
    if (right > i + 1) {
      stack.push([i + 1, right])
    }
  }
}

const partition = <T>(arr: T[], left: number, right: number, cmp: (a: T, b: T) => number) => {
  const randomIndex = Math.floor(Math.random() * (right - left) + left)
  swap(arr, left, randomIndex)
  const pivot = arr[left]

  let i = left, j = right
  while (i < j) {
    while (i < j && cmp(arr[j], pivot) > 0) {
      j -= 1
    }
    while (i < j && cmp(arr[i], pivot) <= 0) {
      i += 1
    }
    swap(arr, i, j)
  }

  swap(arr, left, i)
  return i
}

const swap = (arr: any[], i: number, j: number) => {
  const temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp
}
// @lc code=end

console.log(sortArray([]))
console.log(sortArray([1]))
console.log(sortArray([1, 2]))
console.log(sortArray([4, 1, 2]))
console.log(sortArray([5, 2, 3, 1]))
console.log(sortArray([5, 1, 1, 2, 0]))
console.log(sortArray([5, 1, 1, 2, 0, 0]))

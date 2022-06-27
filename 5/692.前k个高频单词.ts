/*
 * @lc app=leetcode.cn id=692 lang=typescript
 *
 * [692] 前K个高频单词
 *
 * https://leetcode.cn/problems/top-k-frequent-words/description/
 *
 * algorithms
 * Medium (56.86%)
 * Likes:    456
 * Dislikes: 0
 * Total Accepted:    82K
 * Total Submissions: 144.2K
 * Testcase Example:  '["i", "love", "leetcode", "i", "love", "coding"]\n2'
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
  const counter: Record<string, number> = {}
  words.forEach((x) => {
    counter[x] = (counter[x] || 0) + 1
  })

  const list = Object.keys(counter)

  quickSortPart(list, k, 0, list.length - 1, (a: string, b: string) => {
    if (counter[a] !== counter[b]) {
      return counter[b] - counter[a]
    }
    return a > b ? 1 : -1
  })

  return list.slice(0, k)
}

const quickSortPart = <T>(arr: T[], k: number, left: number, right: number, cmp: (a: T, b: T) => number) => {
  if (left >= right) return

  const i = partition(arr, left, right, cmp)
  const target = left + k - 1

  if (i > target) {
    quickSortPart(arr, k, left, i - 1, cmp)
  } else {
    quickSortPart(arr, i - left, left, i - 1, cmp)
    quickSortPart(arr, target - i, i + 1, right, cmp)
  }
}

const partition = <T>(arr: T[], left: number, right: number, cmp: (a: T, b: T) => number) => {
  const randIndex = Math.floor(Math.random() * (right - left)) + left
  swap(arr, randIndex, left)

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

  swap(arr, i, left)
  return i
}

const swap = (arr: any[], i: number, j: number) => {
  const tmp = arr[i]
  arr[i] = arr[j]
  arr[j] = tmp
}
// @lc code=end

// ["plpaboutit","jnoqzdute","sfvkdqf","mjc","nkpllqzjzp","foqqenbey","ssnanizsav","nkpllqzjzp","sfvkdqf","isnjmy","pnqsz","hhqpvvt","fvvdtpnzx","jkqonvenhx","cyxwlef","hhqpvvt","fvvdtpnzx","plpaboutit","sfvkdqf","mjc","fvvdtpnzx","bwumsj","foqqenbey","isnjmy","nkpllqzjzp","hhqpvvt","foqqenbey","fvvdtpnzx","bwumsj","hhqpvvt","fvvdtpnzx","jkqonvenhx","jnoqzdute","foqqenbey","jnoqzdute","foqqenbey","hhqpvvt","ssnanizsav","mjc","foqqenbey","bwumsj","ssnanizsav","fvvdtpnzx","nkpllqzjzp","jkqonvenhx","hhqpvvt","mjc","isnjmy","bwumsj","pnqsz","hhqpvvt","nkpllqzjzp","jnoqzdute","pnqsz","nkpllqzjzp","jnoqzdute","foqqenbey","nkpllqzjzp","hhqpvvt","fvvdtpnzx","plpaboutit","jnoqzdute","sfvkdqf","fvvdtpnzx","jkqonvenhx","jnoqzdute","nkpllqzjzp","jnoqzdute","fvvdtpnzx","jkqonvenhx","hhqpvvt","isnjmy","jkqonvenhx","ssnanizsav","jnoqzdute","jkqonvenhx","fvvdtpnzx","hhqpvvt","bwumsj","nkpllqzjzp","bwumsj","jkqonvenhx","jnoqzdute","pnqsz","foqqenbey","sfvkdqf","sfvkdqf"]\n1

// ["a","b","c","a","b","c","d","e","f"]\n3

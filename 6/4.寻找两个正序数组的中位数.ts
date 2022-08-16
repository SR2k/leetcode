/*
 * @lc app=leetcode.cn id=4 lang=typescript
 *
 * [4] 寻找两个正序数组的中位数
 *
 * https://leetcode.cn/problems/median-of-two-sorted-arrays/description/
 *
 * algorithms
 * Hard (41.45%)
 * Likes:    5574
 * Dislikes: 0
 * Total Accepted:    744.8K
 * Total Submissions: 1.8M
 * Testcase Example:  '[1,3]\n[2]'
 *
 * 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
 *
 * 算法的时间复杂度应该为 O(log (m+n)) 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums1 = [1,3], nums2 = [2]
 * 输出：2.00000
 * 解释：合并数组 = [1,2,3] ，中位数 2
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums1 = [1,2], nums2 = [3,4]
 * 输出：2.50000
 * 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
 *
 *
 *
 *
 *
 *
 * 提示：
 *
 *
 * nums1.length == m
 * nums2.length == n
 * 0 <= m <= 1000
 * 0 <= n <= 1000
 * 1 <= m + n <= 2000
 * -10^6 <= nums1[i], nums2[i] <= 10^6
 *
 *
 */

export
// @lc code=start
function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
  if (nums1.length > nums2.length) {
    return findMedianSortedArrays(nums2, nums1)
  }

  const len1 = nums1.length, len2 = nums2.length
  const total = len1 + len2, leftTotal = total - (total >> 1)

  let leftResult = MIN_VAL, rightResult = MAX_VAL
  const judge = (leftCount1: number) => {
    const leftCount2 = leftTotal - leftCount1

    const l1 = leftCount1 > 0 ? nums1[leftCount1 - 1] : MIN_VAL
    const l2 = leftCount2 > 0 ? nums2[leftCount2 - 1] : MIN_VAL

    const r1 = leftCount1 < len1 ? nums1[leftCount1] : MAX_VAL
    const r2 = leftCount2 < len2 ? nums2[leftCount2] : MAX_VAL

    if (l1 <= r2 && l2 <= r1) {
      leftResult = Math.max(l1, l2)
      rightResult = Math.min(r1, r2)
      return FindMedianJudgeResult.Found
    } else if (l1 > l2) {
      return FindMedianJudgeResult.SearchLeftPart
    } else {
      return FindMedianJudgeResult.SearchRightPart
    }
  }

  let left = 0, right = nums1.length
  while (left + 1 < right) {
    const middle = left + ((right - left) >> 1)
    const judgeResult = judge(middle)

    if (judgeResult === FindMedianJudgeResult.Found) {
      break
    } else if (judgeResult === FindMedianJudgeResult.SearchRightPart) {
      left = middle
    } else {
      right = middle
    }
  }

  judge(left)
  judge(right)

  if (total & 1) {
    return leftResult
  }
  return (leftResult + rightResult) / 2
}

const MAX_VAL = Number.MAX_SAFE_INTEGER
const MIN_VAL = Number.MIN_SAFE_INTEGER

const enum FindMedianJudgeResult {
  Found,
  SearchLeftPart,
  SearchRightPart,
}
// @lc code=end

console.log(findMedianSortedArrays([1, 3], [2]))
console.log(findMedianSortedArrays([1, 2], [3, 4]))
console.log(findMedianSortedArrays([1, 2, 3, 4, 5, 6], [3, 4, 5, 6, 7, 8]))
console.log(findMedianSortedArrays([1, 2, 3, 4, 5, 6], [3, 4, 5, 6, 7]))
console.log(findMedianSortedArrays([], [3, 4, 5, 6, 7]))
console.log(findMedianSortedArrays([], [3, 4]))
console.log(findMedianSortedArrays([], [3]))

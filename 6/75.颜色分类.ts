/*
 * @lc app=leetcode.cn id=75 lang=typescript
 *
 * [75] 颜色分类
 *
 * https://leetcode.cn/problems/sort-colors/description/
 *
 * algorithms
 * Medium (60.12%)
 * Likes:    1313
 * Dislikes: 0
 * Total Accepted:    402.6K
 * Total Submissions: 669.7K
 * Testcase Example:  '[2,0,2,1,1,0]'
 *
 * 给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
 *
 * 我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
 *
 *
 *
 *
 * 必须在不使用库的sort函数的情况下解决这个问题。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [2,0,2,1,1,0]
 * 输出：[0,0,1,1,2,2]
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [2,0,1]
 * 输出：[0,1,2]
 *
 *
 *
 *
 * 提示：
 *
 *
 * n == nums.length
 * 1 <= n <= 300
 * nums[i] 为 0、1 或 2
 *
 *
 *
 *
 * 进阶：
 *
 *
 * 你可以不使用代码库中的排序函数来解决这道题吗？
 * 你能想出一个仅使用常数空间的一趟扫描算法吗？
 *
 *
 */

//                  i
//                  j
// const a = [0, 0, 1, 1, 2, 2]
//                     n

export
// @lc code=start
function sortColors(nums: number[]): void {
  threeWayPartition(nums)
}

const threeWayPartition = (arr: number[]) => {
  const pivotValue = 1

  let i = 0, j = 0, n = arr.length - 1
  while (j <= n) {
    if (arr[j] < pivotValue) {
      swap(arr, i, j)
      i++
      j++
    } else if (arr[j] > pivotValue) {
      swap(arr, j, n)
      n--
    } else {
      j++
    }
  }
}

function swap(arr: any[], i: number, j: number) {
  const temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp
}
// @lc code=end

const arr = [2, 0, 1]
sortColors(arr)
console.log(arr)

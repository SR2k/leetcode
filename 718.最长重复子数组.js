/*
 * @lc app=leetcode.cn id=718 lang=javascript
 *
 * [718] 最长重复子数组
 *
 * https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/description/
 *
 * algorithms
 * Medium (55.85%)
 * Likes:    443
 * Dislikes: 0
 * Total Accepted:    61.4K
 * Total Submissions: 109.9K
 * Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
 *
 * 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
 * 
 * 
 * 
 * 示例：
 * 
 * 输入：
 * A: [1,2,3,2,1]
 * B: [3,2,1,4,7]
 * 输出：3
 * 解释：
 * 长度最长的公共子数组是 [3, 2, 1] 。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= len(A), len(B) <= 1000
 * 0 <= A[i], B[i] < 100
 * 
 * 
 */

// @lc code=start
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
 var findLength = function(nums1, nums2) {
  let maxCount = 0
  if (!nums1 || !nums2) return maxCount

  // step 1. 定义状态
  // step 2. 定义边界
  const dp = new Array(nums1.length + 1)
      .fill(0)
      .map(x => new Array(nums2.length + 1).fill(0))

  // step 3. 状态转移
  for (let i = 1; i <= nums1.length; i++) {
      for (let j = 1; j <= nums2.length; j++) {
          dp[i][j] = nums1[i - 1] === nums2[j - 1]
              ? (dp[i - 1][j - 1] + 1)
              : 0
          maxCount = Math.max(maxCount, dp[i][j])
      }
  }

  return maxCount
};
// @lc code=end

#
# @lc app=leetcode.cn id=1818 lang=python3
#
# [1818] 绝对差值和
#
# https://leetcode-cn.com/problems/minimum-absolute-sum-difference/description/
#
# algorithms
# Medium (38.58%)
# Likes:    47
# Dislikes: 0
# Total Accepted:    8.4K
# Total Submissions: 21.1K
# Testcase Example:  '[1,7,5]\n[2,3,5]'
#
# 给你两个正整数数组 nums1 和 nums2 ，数组的长度都是 n 。
# 
# 数组 nums1 和 nums2 的 绝对差值和 定义为所有 |nums1[i] - nums2[i]|（0 ）的 总和（下标从 0 开始）。
# 
# 你可以选用 nums1 中的 任意一个 元素来替换 nums1 中的 至多 一个元素，以 最小化 绝对差值和。
# 
# 在替换数组 nums1 中最多一个元素 之后 ，返回最小绝对差值和。因为答案可能很大，所以需要对 10^9 + 7 取余 后返回。
# 
# |x| 定义为：
# 
# 
# 如果 x >= 0 ，值为 x ，或者
# 如果 x  ，值为 -x
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums1 = [1,7,5], nums2 = [2,3,5]
# 输出：3
# 解释：有两种可能的最优方案：
# - 将第二个元素替换为第一个元素：[1,7,5] => [1,1,5] ，或者
# - 将第二个元素替换为第三个元素：[1,7,5] => [1,5,5]
# 两种方案的绝对差值和都是 |1-2| + (|1-3| 或者 |5-3|) + |5-5| = 3
# 
# 
# 示例 2：
# 
# 
# 输入：nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]
# 输出：0
# 解释：nums1 和 nums2 相等，所以不用替换元素。绝对差值和为 0
# 
# 
# 示例 3：
# 
# 
# 输入：nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]
# 输出：20
# 解释：将第一个元素替换为第二个元素：[1,10,4,4,2,7] => [10,10,4,4,2,7]
# 绝对差值和为 |10-9| + |10-3| + |4-5| + |4-1| + |2-7| + |7-4| = 20
# 
# 
# 
# 
# 提示：
# 
# 
# n == nums1.length
# n == nums2.length
# 1 
# 1 
# 
# 
#

# @lc code=start
def b_find(nums: list[int], n: int) -> int:
    if nums[0] >= n:
        return 0
    count = len(nums)
    if nums[-1] <= n:
        return count - 1

    left, right = 0, len(nums) - 1
    while left + 1 < right:
        middle = (left + right) // 2
        m = nums[middle]

        if m == n:
            return middle
        elif m > n:
            right = middle
        else:
            left = middle

    dl, dr = abs(nums[left] - n), abs(nums[right] - n)
    return left if dl <= dr else right


MOD = 10 ** 9 + 7


class Solution:
    def minAbsoluteSumDiff(self, nums1: list[int], nums2: list[int]) -> int:
        original_diff = [abs(nums1[i] - nums2[i]) % MOD for i in range(len(nums1))]
        nums1.sort()
        n_diff = [(original_diff[i] - abs(nums1[b_find(nums1, nums2[i])] - nums2[i])) % MOD for i in range(len(nums2))]

        return (sum(original_diff) - max(n_diff) + MOD) % MOD
# @lc code=end


print(Solution().minAbsoluteSumDiff([1, 7, 5], [2, 3, 5]))


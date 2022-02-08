#
# @lc app=leetcode.cn id=1775 lang=python3
#
# [1775] 通过最少操作次数使数组的和相等
#
# https://leetcode-cn.com/problems/equal-sum-arrays-with-minimum-number-of-operations/description/
#
# algorithms
# Medium (47.44%)
# Likes:    41
# Dislikes: 0
# Total Accepted:    4.3K
# Total Submissions: 9.1K
# Testcase Example:  '[1,2,3,4,5,6]\n[1,1,2,2,2,2]'
#
# 给你两个长度可能不等的整数数组 nums1 和 nums2 。两个数组中的所有值都在 1 到 6 之间（包含 1 和 6）。
# 
# 每次操作中，你可以选择 任意 数组中的任意一个整数，将它变成 1 到 6 之间 任意 的值（包含 1 和 6）。
# 
# 请你返回使 nums1 中所有数的和与 nums2 中所有数的和相等的最少操作次数。如果无法使两个数组的和相等，请返回 -1 。
# 
# 
# 
# 示例 1：
# 
# 输入：nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
# 输出：3
# 解释：你可以通过 3 次操作使 nums1 中所有数的和与 nums2 中所有数的和相等。以下数组下标都从 0 开始。
# - 将 nums2[0] 变为 6 。 nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2] 。
# - 将 nums1[5] 变为 1 。 nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2] 。
# - 将 nums1[2] 变为 2 。 nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2] 。
# 
# 
# 示例 2：
# 
# 输入：nums1 = [1,1,1,1,1,1,1], nums2 = [6]
# 输出：-1
# 解释：没有办法减少 nums1 的和或者增加 nums2 的和使二者相等。
# 
# 
# 示例 3：
# 
# 输入：nums1 = [6,6], nums2 = [1]
# 输出：3
# 解释：你可以通过 3 次操作使 nums1 中所有数的和与 nums2 中所有数的和相等。以下数组下标都从 0 开始。
# - 将 nums1[0] 变为 2 。 nums1 = [2,6], nums2 = [1] 。
# - 将 nums1[1] 变为 2 。 nums1 = [2,2], nums2 = [1] 。
# - 将 nums2[0] 变为 4 。 nums1 = [2,2], nums2 = [4] 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums1.length, nums2.length <= 10^5
# 1 <= nums1[i], nums2[i] <= 6
# 
# 
#

# @lc code=start
class Solution:
    def minOperations(self, nums1: list[int], nums2: list[int]) -> int:
        sum_1, sum_2 = sum(nums1), sum(nums2)

        d = abs(sum_2 - sum_1)
        if d == 0:
            return 0

        nums1.sort()
        nums2.sort()

        if sum_2 < sum_1:
            nums1, nums2 = nums2, nums1
        if len(nums1) * 6 < len(nums2):
            return -1

        p1, p2, result = 0, len(nums2) - 1, 0
        while d > 0:
            d1 = 6 - nums1[p1] if p1 < len(nums1) else -1
            d2 = nums2[p2] - 1 if p2 >= 0 else -1

            if d1 > d2:
                d -= d1
                p1 += 1
            else:
                d -= d2
                p2 -= 1

            result += 1

        return result
# @lc code=end

s = Solution()
print(s.minOperations(nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]))
print(s.minOperations(nums1 = [1,1,1,1,1,1,1], nums2 = [6]))
print(s.minOperations(nums1 = [6,6], nums2 = [1]))

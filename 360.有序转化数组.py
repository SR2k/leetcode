#
# @lc app=leetcode.cn id=360 lang=python3
#
# [360] 有序转化数组
#
# https://leetcode-cn.com/problems/sort-transformed-array/description/
#
# algorithms
# Medium (60.69%)
# Likes:    48
# Dislikes: 0
# Total Accepted:    2.7K
# Total Submissions: 4.5K
# Testcase Example:  '[-4,-2,2,4]\n1\n3\n5'
#
# 给你一个已经 排好序 的整数数组 nums 和整数 a、b、c。对于数组中的每一个数 x，计算函数值 f(x) = ax^2 + bx +
# c，请将函数值产生的数组返回。
# 
# 要注意，返回的这个数组必须按照 升序排列，并且我们所期望的解法时间复杂度为 O(n)。
# 
# 示例 1：
# 
# 输入: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
# 输出: [3,9,15,33]
# 
# 
# 示例 2：
# 
# 输入: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
# 输出: [-23,-5,1,7]
# 
# 
#

# @lc code=start
def calc(x: int, a: int, b: int, c: int):
    return a * x * x + b * x + c


def b_find(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left + 1 < right:
        middle = (left + right) // 2
        nums_middle = nums[middle]

        if nums_middle == target:
            return middle
        elif nums_middle < target:
            left = middle
        else:
            right = middle

    if nums[left] >= target:
        return left
    if nums[right] >= target:
        return right
    return -1


class Solution:
    def sortTransformedArray(self, nums: list[int], a: int, b: int, c: int) -> list[int]:
        if a == 0:
            result = list(map(lambda x: calc(x, a, b, c), nums))
            return result if b > 0 else result[::-1]

        axis = b / -2 / a
        first_greater_index = b_find(nums, axis)

        if first_greater_index <= 0:
            return list(map(lambda x: calc(x, a, b, c), nums))

        pl, pr = first_greater_index - 1, first_greater_index
        result = []

        while True:
            if pl < 0 and pr >= len(nums):
                return result if a > 0 else result[::-1]
            elif pr >= len(nums):
                result.append(calc(nums[pl], a, b, c))
                pl -= 1
            elif pl < 0:
                result.append(calc(nums[pr], a, b, c))
                pr += 1
            elif abs(nums[pl] - axis) <  abs(nums[pr] - axis):
                result.append(calc(nums[pl], a, b, c))
                pl -= 1
            else:
                result.append(calc(nums[pr], a, b, c))
                pr += 1
# @lc code=end

#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#
# https://leetcode-cn.com/problems/sort-an-array/description/
#
# algorithms
# Medium (55.64%)
# Likes:    494
# Dislikes: 0
# Total Accepted:    309.2K
# Total Submissions: 555.9K
# Testcase Example:  '[5,2,3,1]'
#
# 给你一个整数数组 nums，请你将该数组升序排列。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 5 * 10^4
# -5 * 10^4 <= nums[i] <= 5 * 10^4
# 
# 
#

# @lc code=start
class Heap:
    def __init__(self, values: list[int]) -> None:
        self.values = values
        self._heapify()

    def _heapify(self):
        for i in range(len(self.values)):
            self._shift_up(i)

    def _pop(self) -> int:
        self._swap(0, -1)
        result = self.values.pop()
        self._shift_down(0)
        return result


    def _shift_down(self, i: int):
        child = self._get_smaller_child(i)

        # print(i, child, self._should_swap(i, child))
        while self._should_swap(i, child):
            # print(i, child, self._should_swap(i, child))
            self._swap(i, child)
            i = child
            child = self._get_smaller_child(i)


    def _get_smaller_child(self, i):
        left, right = self._left_child(i), self._right_child(i)
        if not self._is_valid_index(left) and not self._is_valid_index(right):
            return -1
        if not self._is_valid_index(left):
            return right
        if not self._is_valid_index(right):
            return left

        if self.values[left] <= self.values[right]:
            return left
        return right


    def _is_valid_index(self, i):
        return 0 <= i < len(self.values)


    def _shift_up(self, i: int):
        while self._should_swap(self._parent(i), i):
            self._swap(self._parent(i), i)
            i = self._parent(i)


    def _should_swap(self, parent: int, child: int):
        if parent == child or not self._is_valid_index(parent) or not self._is_valid_index(child):
            return False
        return self.values[parent] > self.values[child]

    def _parent(self, i: int):
        return (i - 1) // 2

    def _left_child(self, i: int):
        return self._right_child(i) - 1
        
    def _right_child(self, i: int):
        return 2 * (i + 1)

    def _swap(self, i: int, j: int):
        self.values[i], self.values[j] = self.values[j], self.values[i]


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        h = Heap(nums)
        result = []
        while h.values:
            # print(h.values)
            result.append(h._pop())
        return result
# @lc code=end


# print(Solution().sortArray([-4,0,7,4,9,-5,-1,0,-7,-1]))

# [         -5
#      -1,        -4,
#    0,   9,    7,    -1,
# 4,  0]


#
# @lc app=leetcode.cn id=1533 lang=python3
#
# [1533] 找到最大整数的索引
#
# https://leetcode-cn.com/problems/find-the-index-of-the-large-integer/description/
#
# algorithms
# Medium (61.38%)
# Likes:    5
# Dislikes: 0
# Total Accepted:    267
# Total Submissions: 435
# Testcase Example:  '[7,7,7,7,10,7,7,7]'
#
# 我们有这样一个整数数组 arr ，除了一个最大的整数外，其他所有整数都相等。你不能直接访问该数组，你需要通过 API ArrayReader
# 来间接访问，这个 API 有以下成员函数：
# 
# 
# int compareSub(int l, int r, int x, int y)：其中 0 <= l, r, x, y <
# ArrayReader.length()， l <= r 且 x <= y。这个函数比较子数组 arr[l..r] 与子数组 arr[x..y]
# 的和。该函数返回：
# 
# 
# 1 若 arr[l]+arr[l+1]+...+arr[r] > arr[x]+arr[x+1]+...+arr[y] 。
# 0 若 arr[l]+arr[l+1]+...+arr[r] == arr[x]+arr[x+1]+...+arr[y] 。
# -1 若 arr[l]+arr[l+1]+...+arr[r] < arr[x]+arr[x+1]+...+arr[y] 。
# 
# 
# int length()：返回数组的长度。
# 
# 
# 你最多可以调用函数 compareSub() 20 次。你可以认为这两个函数的时间复杂度都为 O(1) 。
# 
# 返回 arr 中最大整数的索引。
# 
# 进阶
# 
# 
# 如果 arr 中有两个整数比其他数大呢？
# 如果有一个数比其他数大，另一个数比其他数小呢？
# 
# 
# 
# 
# 示例 1：
# 
# 输入: arr = [7,7,7,7,10,7,7,7]
# 输出: 4
# 解释: API 的调用如下：
# reader.compareSub(0, 0, 1, 1) // 返回 0。比较子数组 (0, 0) 与子数组 (1, 1) （即比较 arr[0] 和
# arr[1]）。
# 因此我们知道 arr[0] 和 arr[1] 不包含最大元素。
# reader.compareSub(2, 2, 3, 3) // 返回 0。我们可以排除 arr[2] 和 arr[3]。
# reader.compareSub(4, 4, 5, 5) // 返回 1。因此，可以确定 arr[4] 是数组中最大的元素。
# 注意，我们只调用了 3 次 compareSub，所以这个答案是有效的。
# 
# 
# 示例 2:
# 
# 输入: nums = [6,6,12]
# 输出: 2
# 
# 
# 
# 
# 提示:
# 
# 
# 2 <= arr.length <= 5 * 10^5
# 1 <= arr[i] <= 100
# arr 中除一个最大元素外，其余所有元素都相等。
# 
# 
#

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
class ArrayReader(object):
	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
   def compareSub(self, l: int, r: int, x: int, y: int) -> int:
       pass

	 # Returns the length of the array
   def length(self) -> int:
       pass


# @lc code=start
class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        left, right = 0, reader.length() - 1

        while left + 1 < right:
            if (right - left + 1) % 2 == 0:
                l, y = left, right
                r = (y - l) // 2 + l
                x = r + 1
            else:
                l, y = left, right - 1
                r = (y - l) // 2 + l
                x = r + 1

            reader_result = reader.compareSub(l, r, x, y)
            if reader_result < 0:
                left, right = x, y
            elif reader_result > 0:
                left, right = l, r
            else:
                return right

        if left == right:
            return left

        reader_result = reader.compareSub(left, left, right, right)
        if reader_result > 0:
            return left
        return right
# @lc code=end


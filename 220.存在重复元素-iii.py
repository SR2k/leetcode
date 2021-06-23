#
# @lc app=leetcode.cn id=220 lang=python3
#
# [220] 存在重复元素 III
#
# https://leetcode-cn.com/problems/contains-duplicate-iii/description/
#
# algorithms
# Medium (28.69%)
# Likes:    467
# Dislikes: 0
# Total Accepted:    59.4K
# Total Submissions: 206.8K
# Testcase Example:  '[1,2,3,1]\n3\n0'
#
# 给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j])
# ，同时又满足 abs(i - j)  。
# 
# 如果存在则返回 true，不存在返回 false。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,3,1], k = 3, t = 0
# 输出：true
# 
# 示例 2：
# 
# 
# 输入：nums = [1,0,1,1], k = 1, t = 2
# 输出：true
# 
# 示例 3：
# 
# 
# 输入：nums = [1,5,9,1,5,9], k = 2, t = 3
# 输出：false
# 
# 
# 
# 提示：
# 
# 
# 0 
# -2^31 
# 0 
# 0 
# 
# 
#

# @lc code=start
class Window:
    def __init__(self, nums: list[int] = None):
        self.list = sorted(nums or [])

    def push(self, n: int):
        if not self.list:
            self.list = [n]
            return

        l, r = 0, len(self.list) - 1
        while l + 1 < r:
            mid = (l + r) // 2

            if self.list[mid] == n:
                self.list.insert(mid, n)
                return
            
            if self.list[mid] > n:
                r = mid
            else:
                l = mid

        if self.list[l] > n:
            self.list.insert(l, n)
        elif self.list[r] > n:
            self.list.insert(r, n)
        else:
            self.list.insert(r + 1, n)

    def pop(self, n: int):
        l, r = 0, len(self.list) - 1
        while l + 1 < r:
            mid = (l + r) // 2

            if self.list[mid] == n:
                self.list.pop(mid)
                return
            
            if self.list[mid] > n:
                r = mid
            else:
                l = mid

        if self.list[l] == n:
            self.list.pop(l)
        elif self.list[r] == n:
            self.list.pop(r)

    def find_first_greater_or_equal(self, n: int) -> int:
        l, r = 0, len(self.list) - 1
        while l + 1 < r:
            mid = (l + r) // 2

            if self.list[mid] == n:
                return n

            if self.list[mid] > n:
                r = mid
            else:
                l = mid

        if self.list[l] >= n:
            return self.list[l]
        elif self.list[r] >= n:
            return self.list[r]

        return None

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        cnt = len(nums)
        if cnt <= 1: return False

        l, r = 0, 1
        window = Window([nums[0]])
        while r < cnt:
            # print(l, r, '//', nums[r], window)
            # print(window[0], nums[r] + t)
            # print(window[-1], nums[r] - t)
            
            f = window.find_first_greater_or_equal(nums[r] - t)
            # print({ 'l': l, 'r': r, 'f': f, 'window': window.list })
            if f != None and f <= nums[r] + t:
                return True

            window.push(nums[r])
            r += 1
            if r - l > k:
                window.pop(nums[l])
                l += 1

        return False

# @lc code=end


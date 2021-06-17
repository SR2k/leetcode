#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
# https://leetcode-cn.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (53.57%)
# Likes:    786
# Dislikes: 0
# Total Accepted:    124.8K
# Total Submissions: 232.1K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
# 
# 
# 
# 进阶：你可以设计并实现时间复杂度为 O(n) 的解决方案吗？
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
# 
# 示例 2：
# 
# 
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# -10^9 
# 
# 
#

# @lc code=start
class Solution:
    def __init__(self):
        self.parent = {}
        self.rootLen = {}
        self.ret = 1

    def findRoot(self, i: int) -> int:
        while self.parent.get(i) != None:
            i = self.parent[i]
        return i

    def union(self, a: int, b: int) -> None:
        rA, rB = self.findRoot(a), self.findRoot(b)
        if rA == rB: return

        if self.rootLen[rB] > self.rootLen[rA]:
            self.parent[rA] = rB
            self.rootLen[rB] += self.rootLen[rA]
            self.ret = max(self.ret, self.rootLen[rB])
        else:
            self.parent[rB] = rA
            self.rootLen[rA] += self.rootLen[rB]
            self.ret = max(self.ret, self.rootLen[rA])

    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) <= 1: return len(nums)

        for i in nums:
            self.parent[i] = None
            self.rootLen[i] = 1

        for i in nums:
            if i - 1 not in self.parent and i + 1 not in self.parent:
                continue
            if i - 1 in self.parent:
                self.union(i, i - 1)
            if i + 1 in self.parent:
                self.union(i, i + 1)

        return self.ret

# @lc code=end

# print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
# print(Solution().longestConsecutive( [100,4,200,1,3,2]))

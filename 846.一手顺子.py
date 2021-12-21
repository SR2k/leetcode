#
# @lc app=leetcode.cn id=846 lang=python3
#
# [846] 一手顺子
#
# https://leetcode-cn.com/problems/hand-of-straights/description/
#
# algorithms
# Medium (51.39%)
# Likes:    114
# Dislikes: 0
# Total Accepted:    9.3K
# Total Submissions: 18.1K
# Testcase Example:  '[1,2,3,6,2,3,4,7,8]\n3'
#
# Alice 手中有一把牌，她想要重新排列这些牌，分成若干组，使每一组的牌数都是 groupSize ，并且由 groupSize 张连续的牌组成。
# 
# 给你一个整数数组 hand 其中 hand[i] 是写在第 i 张牌，和一个整数 groupSize 。如果她可能重新排列这些牌，返回 true
# ；否则，返回 false 。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# 输出：true
# 解释：Alice 手中的牌可以被重新排列为 [1,2,3]，[2,3,4]，[6,7,8]。
# 
# 示例 2：
# 
# 
# 输入：hand = [1,2,3,4,5], groupSize = 4
# 输出：false
# 解释：Alice 手中的牌无法被重新排列成几个大小为 4 的组。
# 
# 
# 
# 提示：
# 
# 
# 1 <= hand.length <= 10^4
# 0 <= hand[i] <= 10^9
# 1 <= groupSize <= hand.length
# 
# 
# 
# 
# 注意：此题目与 1296
# 重复：https://leetcode-cn.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
# 
#

# @lc code=start
from collections import Counter, deque


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        counter = Counter(hand)
        nums = deque(sorted(counter.keys()))

        while nums:
            curr = nums[0]

            for _ in range(groupSize):
                if not counter[curr]:
                    return False

                counter[curr] -= 1
                if not counter[curr]:
                    nums.popleft()

                curr += 1

        return True
# @lc code=end

s = Solution()
print(s.isNStraightHand(hand = [1,2,3,6,2,3,4,7,8], groupSize = 3))
print(s.isNStraightHand(hand = [1,2,3,4,5], groupSize = 4))

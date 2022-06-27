#
# @lc app=leetcode.cn id=1497 lang=python3
#
# [1497] 检查数组对是否可以被 k 整除
#
# https://leetcode.cn/problems/check-if-array-pairs-are-divisible-by-k/description/
#
# algorithms
# Medium (39.89%)
# Likes:    65
# Dislikes: 0
# Total Accepted:    10.1K
# Total Submissions: 25.3K
# Testcase Example:  '[1,2,3,4,5,10,6,7,8,9]\n5'
#
# 给你一个整数数组 arr 和一个整数 k ，其中数组长度是偶数，值为 n 。
# 
# 现在需要把数组恰好分成 n / 2 对，以使每对数字的和都能够被 k 整除。
# 
# 如果存在这样的分法，请返回 True ；否则，返回 False 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：arr = [1,2,3,4,5,10,6,7,8,9], k = 5
# 输出：true
# 解释：划分后的数字对为 (1,9),(2,8),(3,7),(4,6) 以及 (5,10) 。
# 
# 
# 示例 2：
# 
# 
# 输入：arr = [1,2,3,4,5,6], k = 7
# 输出：true
# 解释：划分后的数字对为 (1,6),(2,5) 以及 (3,4) 。
# 
# 
# 示例 3：
# 
# 
# 输入：arr = [1,2,3,4,5,6], k = 10
# 输出：false
# 解释：无法在将数组中的数字分为三对的同时满足每对数字和能够被 10 整除的条件。
# 
# 
# 
# 
# 提示：
# 
# 
# arr.length == n
# 1 <= n <= 10^5
# n 为偶数
# -10^9 <= arr[i] <= 10^9
# 1 <= k <= 10^5
# 
# 
#

# @lc code=start
from collections import Counter


class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        mods = Counter()
        for n in arr:
            mods[n % k] += 1

        keys = mods.keys()
        for key in keys:
            if key == 0:
                if mods[key] % 2 != 0:
                    return False
                continue

            if mods[k - key] < mods[key]:
                return False
            mods[k - key] -= mods[key]
            mods[key] = 0

        return True
# @lc code=end

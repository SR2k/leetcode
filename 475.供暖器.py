#
# @lc app=leetcode.cn id=475 lang=python3
#
# [475] 供暖器
#
# https://leetcode-cn.com/problems/heaters/description/
#
# algorithms
# Medium (33.01%)
# Likes:    212
# Dislikes: 0
# Total Accepted:    20K
# Total Submissions: 60.5K
# Testcase Example:  '[1,2,3]\n[2]'
#
# 冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
# 
# 在加热器的加热半径范围内的每个房屋都可以获得供暖。
# 
# 现在，给出位于一条水平线上的房屋 houses 和供暖器 heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。
# 
# 说明：所有供暖器都遵循你的半径标准，加热的半径也一样。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: houses = [1,2,3], heaters = [2]
# 输出: 1
# 解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。
# 
# 
# 示例 2:
# 
# 
# 输入: houses = [1,2,3,4], heaters = [1,4]
# 输出: 1
# 解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
# 
# 
# 示例 3：
# 
# 
# 输入：houses = [1,5], heaters = [2]
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        houses.sort()
        heaters.sort()

        left, right = 0, 0
        result = 0

        for house in houses:
            while left + 1 < len(heaters) and heaters[left + 1] <= house:
                left += 1

            while right + 1 < len(heaters) and heaters[right] < house:
                right += 1

            result = max(result, min(abs(heaters[left] - house), abs(heaters[right] - house)))

        return result
# @lc code=end

s = Solution()
print(s.findRadius(houses = [1,2,3], heaters = [2]))
print(s.findRadius(houses = [1,2,3,4], heaters = [1,4]))
print(s.findRadius(houses = [1,5], heaters = [2]))
print(s.findRadius([1,2,3], [1,2,3]))
print(s.findRadius([1,2,3,4],[1,4]))

print(s.findRadius([282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923],[823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612])) # 161834419

#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#
# https://leetcode-cn.com/problems/candy/description/
#
# algorithms
# Hard (48.68%)
# Likes:    741
# Dislikes: 0
# Total Accepted:    114.2K
# Total Submissions: 234.7K
# Testcase Example:  '[1,0,2]'
#
# n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。
# 
# 你需要按照以下要求，给这些孩子分发糖果：
# 
# 
# 每个孩子至少分配到 1 个糖果。
# 相邻两个孩子评分更高的孩子会获得更多的糖果。
# 
# 
# 请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：ratings = [1,0,2]
# 输出：5
# 解释：你可以分别给第一个、第二个、第三个孩子分发 2、1、2 颗糖果。
# 
# 
# 示例 2：
# 
# 
# 输入：ratings = [1,2,2]
# 输出：4
# 解释：你可以分别给第一个、第二个、第三个孩子分发 1、2、1 颗糖果。
# ⁠    第三个孩子只得到 1 颗糖果，这满足题面中的两个条件。
# 
# 
# 
# 提示：
# 
# 
# n == ratings.length
# 1 <= n <= 2 * 10^4
# 0 <= ratings[i] <= 2 * 10^4
# 
# 
#

# @lc code=start
class Solution:
    def candy(self, ratings: list[int]) -> int:

        left = [0 for _ in ratings]
        for i, rating in enumerate(ratings):
            left[i] = 1
            if i > 0 and rating > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        ret = [0 for _ in ratings]
        prev_right = 1
        for i in range(len(ratings) - 1, -1, -1):
            right = 1
            if i < len(ratings) - 1 and ratings[i] > ratings[i + 1]:
                right = prev_right + 1
            ret[i] = max(left[i], right)

            prev_right = right

        return sum(ret)
# @lc code=end

s = Solution()
print(s.candy(ratings = [1,0,2]))
print(s.candy(ratings = [1,2,2]))
print(s.candy(ratings = [1,3,2,2,1]))
#                       [1,2,1,1,1]
print(s.candy(ratings = [1,2,87,87,87,2,1]))
#                       [1,2,2, 1, 3, 2,1]

#
# @lc app=leetcode.cn id=275 lang=python3
#
# [275] H 指数 II
#
# https://leetcode-cn.com/problems/h-index-ii/description/
#
# algorithms
# Medium (41.13%)
# Likes:    109
# Dislikes: 0
# Total Accepted:    21.9K
# Total Submissions: 53.1K
# Testcase Example:  '[0,1,3,5,6]'
#
# 给定一位研究者论文被引用次数的数组（被引用次数是非负整数），数组已经按照 升序排列 。编写一个方法，计算出研究者的 h 指数。
# 
# h 指数的定义: “h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）总共有 h
# 篇论文分别被引用了至少 h 次。（其余的 N - h 篇论文每篇被引用次数不多于 h 次。）"
# 
# 
# 
# 示例:
# 
# 输入: citations = [0,1,3,5,6]
# 输出: 3 
# 解释: 给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 0, 1, 3, 5, 6 次。
# 由于研究者有 3 篇论文每篇至少被引用了 3 次，其余两篇论文每篇被引用不多于 3 次，所以她的 h 指数是 3。
# 
# 
# 
# 说明:
# 
# 如果 h 有多有种可能的值 ，h 指数是其中最大的那个。
# 
# 
# 
# 进阶：
# 
# 
# 这是 H 指数 的延伸题目，本题中的 citations 数组是保证有序的。
# 你可以优化你的算法到对数时间复杂度吗？
# 
# 
#

# @lc code=start
class Solution:
    def hIndex(self, citations: list[int]) -> int:
        total = len(citations)
        left, right = 0, total - 1

        while left + 1 < right:
            middle = (left + right) // 2
            count = total - middle

            if count >= citations[middle]:
                left = middle
            else:
                right = middle

        if total - left <= citations[left]:
            return total - left
        if total - right <= citations[right]:
            return total - right

        return 0
# @lc code=end


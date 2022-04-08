#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#
# https://leetcode-cn.com/problems/n-queens-ii/description/
#
# algorithms
# Hard (82.29%)
# Likes:    348
# Dislikes: 0
# Total Accepted:    88.4K
# Total Submissions: 107.5K
# Testcase Example:  '4'
#
# n 皇后问题 研究的是如何将 n 个皇后放置在 n × n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 
# 给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 4
# 输出：2
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 9
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        result = 0
        rows = cols = diag = revr = 0


        def helper(i: int, j: int, cnt: int):
            if cnt == n:
                nonlocal result
                result += 1
                return
            if i == n:
                return

            # no enough rows for another queen
            if n - i + 1 < n - cnt:
                return

            ni, nj = Solution.get_next(i, j, n)
            helper(ni, nj, cnt)

            d, r = Solution.get_repr(i, j, n)
            nonlocal rows, cols, diag, revr
            if rows & 1 << i or cols & 1 << j or diag & 1 << d or revr & 1 << r:
                return

            rows ^= 1 << i
            cols ^= 1 << j
            diag ^= 1 << d
            revr ^= 1 << r
            helper(ni, nj, cnt + 1)
            rows ^= 1 << i
            cols ^= 1 << j
            diag ^= 1 << d
            revr ^= 1 << r


        helper(0, 0, 0)
        return result


    @staticmethod
    def get_next(i: int, j: int, n: int):
        if j == n - 1:
            return i + 1, 0
        return i, j + 1


    @staticmethod
    def get_diag_repr(i: int, j: int, n: int):
        d = abs(i - j)

        if i >= j:
            return d
        return n + d


    @staticmethod
    def get_repr(i: int, j: int, n: int):
        return Solution.get_diag_repr(i, j, n), Solution.get_diag_repr(i, n - 1 - j, n)
# @lc code=end

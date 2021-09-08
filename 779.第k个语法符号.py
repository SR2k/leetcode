#
# @lc app=leetcode.cn id=779 lang=python3
#
# [779] 第K个语法符号
#
# https://leetcode-cn.com/problems/k-th-symbol-in-grammar/description/
#
# algorithms
# Medium (43.57%)
# Likes:    134
# Dislikes: 0
# Total Accepted:    18.7K
# Total Submissions: 42.8K
# Testcase Example:  '1\n1'
#
# 在第一行我们写上一个 0。接下来的每一行，将前一行中的0替换为01，1替换为10。
# 
# 给定行数 N 和序数 K，返回第 N 行中第 K个字符。（K从1开始）
# 
# 
# 例子:
# 
# 输入: N = 1, K = 1
# 输出: 0
# 
# 输入: N = 2, K = 1
# 输出: 0
# 
# 输入: N = 2, K = 2
# 输出: 1
# 
# 输入: N = 4, K = 5
# 输出: 1
# 
# 解释:
# 第一行: 0
# 第二行: 01
# 第三行: 0110
# 第四行: 01101001
# 
# 
# 
# 注意：
# 
# 
# N 的范围 [1, 30].
# K 的范围 [1, 2^(N-1)].
# 
# 
#

# @lc code=start
def map(prev, col):
    if prev == 0:
        return 0 if col % 2 == 1 else 1
    else:
        return 1 if col % 2 == 1 else 0


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        cols = []
        while n > 1:
            n -= 1
            cols.append(k)
            k = (k + 1) // 2

        prev = 0
        while cols:
            col = cols.pop()
            prev = map(prev, col)

        return prev
# @lc code=end


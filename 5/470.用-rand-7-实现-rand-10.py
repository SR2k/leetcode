#
# @lc app=leetcode.cn id=470 lang=python3
#
# [470] 用 Rand7() 实现 Rand10()
#
# https://leetcode.cn/problems/implement-rand10-using-rand7/description/
#
# algorithms
# Medium (55.12%)
# Likes:    397
# Dislikes: 0
# Total Accepted:    82.6K
# Total Submissions: 149.8K
# Testcase Example:  '1'
#
# 给定方法 rand7 可生成 [1,7] 范围内的均匀随机整数，试写一个方法 rand10 生成 [1,10] 范围内的均匀随机整数。
# 
# 你只能调用 rand7() 且不能调用其他方法。请不要使用系统的 Math.random() 方法。
# 
# 
# 
# 
# 每个测试用例将有一个内部参数 n，即你实现的函数 rand10() 在测试时将被调用的次数。请注意，这不是传递给 rand10() 的参数。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: 1
# 输出: [2]
# 
# 
# 示例 2:
# 
# 
# 输入: 2
# 输出: [2,8]
# 
# 
# 示例 3:
# 
# 
# 输入: 3
# 输出: [3,8,10]
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= n <= 10^5
# 
# 
# 
# 
# 进阶:
# 
# 
# rand7()调用次数的 期望值 是多少 ?
# 你能否尽量少调用 rand7() ?
# 
# 
#

# @lc code=start
mapping = {
    6: 1,
    2: 2,
    3: 2,
    1: 3,
    4: 3,
    5: 4,
    7: 4,
    8: 5,
    10: 5,
    12: 6,
    14: 7,
    15: 7,
    18: 8,
    20: 8,
    21: 9,
    24: 9,
    28: 10,
    30: 10,
}

class Solution:
    def rand10(self):
        while True:
            rand = rand7() * rand7()

            if rand in mapping:
                return mapping[rand]
# @lc code=end

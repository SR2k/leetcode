#
# @lc app=leetcode.cn id=402 lang=python3
#
# [402] 移掉 K 位数字
#
# https://leetcode.cn/problems/remove-k-digits/description/
#
# algorithms
# Medium (32.34%)
# Likes:    819
# Dislikes: 0
# Total Accepted:    107.5K
# Total Submissions: 332.6K
# Testcase Example:  '"1432219"\n3'
#
# 给你一个以字符串表示的非负整数 num 和一个整数 k ，移除这个数中的 k 位数字，使得剩下的数字最小。请你以字符串形式返回这个最小的数字。
# 
# 
# 示例 1 ：
# 
# 
# 输入：num = "1432219", k = 3
# 输出："1219"
# 解释：移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219 。
# 
# 
# 示例 2 ：
# 
# 
# 输入：num = "10200", k = 1
# 输出："200"
# 解释：移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
# 
# 
# 示例 3 ：
# 
# 
# 输入：num = "10", k = 2
# 输出："0"
# 解释：从原数字移除所有的数字，剩余为空就是 0 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# num 仅由若干位数字（0 - 9）组成
# 除了 0 本身之外，num 不含任何前导零
# 
# 
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for char in num:
            while stack and k and stack[-1] > char:
                stack.pop()
                k -= 1

            if stack or char != '0':
                stack.append(char)

        while k and stack:
            stack.pop()
            k -= 1

        if not stack:
            return '0'
        return ''.join(stack)
# @lc code=end

# "1432219", k = 0

# [1, 2, 1, 9]

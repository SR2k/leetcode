#
# @lc app=leetcode.cn id=402 lang=python3
#
# [402] 移掉 K 位数字
#
# https://leetcode-cn.com/problems/remove-k-digits/description/
#
# algorithms
# Medium (32.50%)
# Likes:    773
# Dislikes: 0
# Total Accepted:    100K
# Total Submissions: 308.1K
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

        for n in num:
            while stack and stack[-1] > n and k:
                stack.pop()
                k -= 1
            if stack or n != '0':
                stack.append(n)

        while k and stack:
            stack.pop()
            k -= 1

        return "".join(stack) or '0'
# @lc code=end

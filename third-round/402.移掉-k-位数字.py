#
# @lc app=leetcode.cn id=402 lang=python3
#
# [402] 移掉 K 位数字
#
# https://leetcode-cn.com/problems/remove-k-digits/description/
#
# algorithms
# Medium (32.53%)
# Likes:    756
# Dislikes: 0
# Total Accepted:    96.7K
# Total Submissions: 297.2K
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
from collections import deque


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return '0'

        result = deque()
        for char in num:
            while result and result[-1] > char and k:
                result.pop()
                k -= 1

            result.append(char)

        while k:
            result.pop()
            k -= 1

        while result and result[0] == '0':
            result.popleft()

        return "".join(result) if result else '0'
# @lc code=end

s = Solution()
print(s.removeKdigits("1432219", k = 3))
print(s.removeKdigits( "10200", k = 1))
print(s.removeKdigits("10", k = 2))
print(s.removeKdigits("0", k = 1))
print(s.removeKdigits("10000000", k = 2))
print(s.removeKdigits("10000001", k = 2))
print(s.removeKdigits("12345", k = 2))

#
# @lc app=leetcode.cn id=537 lang=python3
#
# [537] 复数乘法
#
# https://leetcode-cn.com/problems/complex-number-multiplication/description/
#
# algorithms
# Medium (70.93%)
# Likes:    58
# Dislikes: 0
# Total Accepted:    10.9K
# Total Submissions: 15.3K
# Testcase Example:  '"1+1i"\n"1+1i"'
#
# 复数 可以用字符串表示，遵循 "实部+虚部i" 的形式，并满足下述条件：
# 
# 
# 实部 是一个整数，取值范围是 [-100, 100]
# 虚部 也是一个整数，取值范围是 [-100, 100]
# i^2 == -1
# 
# 
# 给你两个字符串表示的复数 num1 和 num2 ，请你遵循复数表示形式，返回表示它们乘积的字符串。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：num1 = "1+1i", num2 = "1+1i"
# 输出："0+2i"
# 解释：(1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i ，你需要将它转换为 0+2i 的形式。
# 
# 
# 示例 2：
# 
# 
# 输入：num1 = "1+-1i", num2 = "1+-1i"
# 输出："0+-2i"
# 解释：(1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i ，你需要将它转换为 0+-2i 的形式。 
# 
# 
# 
# 
# 提示：
# 
# 
# num1 和 num2 都是有效的复数表示。
# 
# 
#

# @lc code=start
def parse(cn: str) -> tuple[int, int]:
    real, imaginary = cn.split('+')
    return (int(real), int(imaginary[:-1]))


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        r1, i1 = parse(num1)
        r2, i2 = parse(num2)
        
        r = r1 * r2 - i1 * i2
        i = r1 * i2 + r2 * i1

        return f"{r}+{i}i"
# @lc code=end


#
# @lc app=leetcode.cn id=282 lang=python3
#
# [282] 给表达式添加运算符
#
# https://leetcode-cn.com/problems/expression-add-operators/description/
#
# algorithms
# Hard (39.15%)
# Likes:    328
# Dislikes: 0
# Total Accepted:    16.7K
# Total Submissions: 34.9K
# Testcase Example:  '"123"\n6'
#
# 给定一个仅包含数字 0-9 的字符串 num 和一个目标值整数 target ，在 num 的数字之间添加 二元 运算符（不是一元）+、- 或 *
# ，返回所有能够得到目标值的表达式。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: num = "123", target = 6
# 输出: ["1+2+3", "1*2*3"] 
# 
# 
# 示例 2:
# 
# 
# 输入: num = "232", target = 8
# 输出: ["2*3+2", "2+3*2"]
# 
# 示例 3:
# 
# 
# 输入: num = "105", target = 5
# 输出: ["1*0+5","10-5"]
# 
# 示例 4:
# 
# 
# 输入: num = "00", target = 0
# 输出: ["0+0", "0-0", "0*0"]
# 
# 
# 示例 5:
#
#
# 输入: num = "3456237490", target = 9191
# 输出: []
#
#
#
# 提示：
#
#
# 1 <= num.length <= 10
# num 仅含数字
# -2^31 <= target <= 2^31 - 1
#
#
#

# @lc code=start
class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        result = []

        # i - curr begin
        def helper(i: int, prev: list[int], prev_exp: str):
            if i >= len(num):
                if sum(prev) == target:
                    result.append(prev_exp)
                return

            max_j = i + 1 if num[i] == '0' else len(num)
            for j in range(i + 1, max_j + 1):
                n = int(num[i:j])

                prev.append(n)
                helper(j, prev, f"{prev_exp}+{n}" if prev_exp else str(n))
                prev.pop()

                if prev:
                    prev.append(-n)
                    helper(j, prev, f"{prev_exp}-{n}")
                    prev.pop()

                    last_num = prev[-1]
                    prev[-1] *= n
                    helper(j, prev, f"{prev_exp}*{n}")
                    prev[-1] = last_num

        helper(0, [], '')
        return result
# @lc code=end

s = Solution()
# print(s.addOperators(num = "123", target = 6))
# print(s.addOperators(num = "232", target = 8))
# print(s.addOperators(num = "105", target = 5))
print(s.addOperators(num = "00", target = 0))
# print(s.addOperators(num = "3456237490", target = 9191))
# 

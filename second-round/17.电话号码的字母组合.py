#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (57.55%)
# Likes:    1682
# Dislikes: 0
# Total Accepted:    393K
# Total Submissions: 682.8K
# Testcase Example:  '"23"'
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
# 
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
# 
# 
# 示例 2：
# 
# 
# 输入：digits = ""
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：digits = "2"
# 输出：["a","b","c"]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= digits.length <= 4
# digits[i] 是范围 ['2', '9'] 的一个数字。
# 
# 
#

# @lc code=start
CHARECTERS = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        result = CHARECTERS[digits[0]]
        for d in digits[1:]:
            temp = []

            for char in CHARECTERS[d]:
                for r in result:
                    temp.append(r + char)

            result = temp
        return result
# @lc code=end

s = Solution()
print(s.letterCombinations('23'))

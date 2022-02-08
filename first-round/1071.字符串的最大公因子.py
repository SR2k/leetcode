#
# @lc app=leetcode.cn id=1071 lang=python3
#
# [1071] 字符串的最大公因子
#
# https://leetcode-cn.com/problems/greatest-common-divisor-of-strings/description/
#
# algorithms
# Easy (58.70%)
# Likes:    217
# Dislikes: 0
# Total Accepted:    35.4K
# Total Submissions: 60.2K
# Testcase Example:  '"ABCABC"\n"ABC"'
#
# 对于字符串 S 和 T，只有在 S = T + ... + T（T 自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。
# 
# 返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：str1 = "ABCABC", str2 = "ABC"
# 输出："ABC"
# 
# 
# 示例 2：
# 
# 
# 输入：str1 = "ABABAB", str2 = "ABAB"
# 输出："AB"
# 
# 
# 示例 3：
# 
# 
# 输入：str1 = "LEET", str2 = "CODE"
# 输出：""
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# str1[i] 和 str2[i] 为大写英文字母
# 
# 
#

# @lc code=start
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1

        if len(str1) < len(str2):
            str1, str2 = str2, str1

        if str1[0:len(str2)] != str2:
            return ''

        return self.gcdOfStrings(str2, str1[len(str2):])
# @lc code=end

s = Solution()
print(s.gcdOfStrings(str1 = "ABCABC", str2 = "ABC"))
print(s.gcdOfStrings(str1 = "ABABAB", str2 = "ABAB"))
print(s.gcdOfStrings(str1 = "LEET", str2 = "CODE"))

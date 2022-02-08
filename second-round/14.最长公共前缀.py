#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (41.58%)
# Likes:    1973
# Dislikes: 0
# Total Accepted:    706.9K
# Total Submissions: 1.7M
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
# 
# 
# 示例 2：
# 
# 
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。
# 
# 
# 
# 提示：
# 
# 
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] 仅由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ''

        for i in range(len(strs[0])):
            char = strs[0][i]
            for str in strs:
                if i >= len(str):
                    return result
                if str[i] != char:
                    return result

            result += char

        return result
# @lc code=end

s = Solution()
print(s.longestCommonPrefix(strs = ["flower","flow","flight"]))
print(s.longestCommonPrefix(strs = ["flower","flow","flowht"]))
print(s.longestCommonPrefix(strs = ["dog","racecar","car"]))

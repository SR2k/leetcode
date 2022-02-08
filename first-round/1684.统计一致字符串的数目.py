#
# @lc app=leetcode.cn id=1684 lang=python3
#
# [1684] 统计一致字符串的数目
#
# https://leetcode-cn.com/problems/count-the-number-of-consistent-strings/description/
#
# algorithms
# Easy (82.82%)
# Likes:    15
# Dislikes: 0
# Total Accepted:    15K
# Total Submissions: 18.1K
# Testcase Example:  '"ab"\n["ad","bd","aaab","baa","badab"]'
#
# 给你一个由不同字符组成的字符串 allowed 和一个字符串数组 words 。如果一个字符串的每一个字符都在 allowed 中，就称这个字符串是
# 一致字符串 。
# 
# 请你返回 words 数组中 一致字符串 的数目。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
# 输出：2
# 解释：字符串 "aaab" 和 "baa" 都是一致字符串，因为它们只包含字符 'a' 和 'b' 。
# 
# 
# 示例 2：
# 
# 
# 输入：allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
# 输出：7
# 解释：所有字符串都是一致的。
# 
# 
# 示例 3：
# 
# 
# 输入：allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
# 输出：4
# 解释：字符串 "cc"，"acd"，"ac" 和 "d" 是一致字符串。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 1 
# allowed 中的字符 互不相同 。
# words[i] 和 allowed 只包含小写英文字母。
# 
# 
#

# @lc code=start
def check(s: str, char_set: set[str]) -> bool:
    for char in s:
        if char not in char_set:
            return False
    return True

class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        char_set = set()
        for char in allowed: char_set.add(char)
        count = 0
        for word in words:
            if check(word, char_set):
                count += 1
        return count
# @lc code=end


#
# @lc app=leetcode.cn id=1832 lang=python3
#
# [1832] 判断句子是否为全字母句
#
# https://leetcode-cn.com/problems/check-if-the-sentence-is-pangram/description/
#
# algorithms
# Easy (82.26%)
# Likes:    11
# Dislikes: 0
# Total Accepted:    12.8K
# Total Submissions: 15.5K
# Testcase Example:  '"thequickbrownfoxjumpsoverthelazydog"'
#
# 全字母句 指包含英语字母表中每个字母至少一次的句子。
# 
# 给你一个仅由小写英文字母组成的字符串 sentence ，请你判断 sentence 是否为 全字母句 。
# 
# 如果是，返回 true ；否则，返回 false 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：sentence = "thequickbrownfoxjumpsoverthelazydog"
# 输出：true
# 解释：sentence 包含英语字母表中每个字母至少一次。
# 
# 
# 示例 2：
# 
# 
# 输入：sentence = "leetcode"
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# sentence 由小写英语字母组成
# 
# 
#

# @lc code=start
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = set([chr(i + ord('a')) for i in range(26)])
        for char in sentence:
            if char in s:
                s.remove(char)

            if not s:
                return True

        return False
# @lc code=end

#
# @lc app=leetcode.cn id=1078 lang=python3
#
# [1078] Bigram 分词
#
# https://leetcode-cn.com/problems/occurrences-after-bigram/description/
#
# algorithms
# Easy (62.20%)
# Likes:    22
# Dislikes: 0
# Total Accepted:    11.5K
# Total Submissions: 18.5K
# Testcase Example:  '"alice is a good girl she is a good student"\n"a"\n"good"'
#
# 给出第一个词 first 和第二个词 second，考虑在某些文本 text 中可能以 "first second third" 形式出现的情况，其中
# second 紧随 first 出现，third 紧随 second 出现。
# 
# 对于每种这样的情况，将第三个词 "third" 添加到答案中，并返回答案。
# 
# 
# 
# 示例 1：
# 
# 输入：text = "alice is a good girl she is a good student", first = "a", second =
# "good"
# 输出：["girl","student"]
# 
# 
# 示例 2：
# 
# 输入：text = "we will we will rock you", first = "we", second = "will"
# 输出：["we","rock"]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= text.length <= 1000
# text 由一些用空格分隔的单词组成，每个单词都由小写英文字母组成
# 1 <= first.length, second.length <= 10
# first 和 second 由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        words = text.split(' ')
        result = []
        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                result.append(words[i + 2])
        return result
# @lc code=end

#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#
# https://leetcode-cn.com/problems/word-break/description/
#
# algorithms
# Medium (52.76%)
# Likes:    1538
# Dislikes: 0
# Total Accepted:    278K
# Total Submissions: 526.1K
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。
# 
# 注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
# 
# 
# 
# 示例 1：
# 
# 
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
# 
# 
# 示例 2：
# 
# 
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
# 注意，你可以重复使用字典中的单词。
# 
# 
# 示例 3：
# 
# 
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s 和 wordDict[i] 仅有小写英文字母组成
# wordDict 中的所有字符串 互不相同
# 
# 
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        matched = [False for _ in range(len(s) + 1)]
        matched[0] = True

        dict = set(wordDict)
        sizes = set([len(w) for w in wordDict])

        for i in range(1, len(s) + 1):
            for len_w in sizes:
                if i - len_w < 0:
                    continue
                # print(i, w, matched[i - len_w], s[i - len_w:i])
                if matched[i - len_w] and s[i - len_w:i] in dict:
                    matched[i] = True
                    # print(i, '--', True)
                    break

        # print(matched)
        return matched[-1]
# @lc code=end

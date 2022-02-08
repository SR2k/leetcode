#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#
# https://leetcode-cn.com/problems/word-break/description/
#
# algorithms
# Medium (52.11%)
# Likes:    1340
# Dislikes: 0
# Total Accepted:    229.8K
# Total Submissions: 440.9K
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
        words = set(wordDict)
        dp = [False for _ in s]

        for i in range(len(s)):
            if s[:i+1] in words:
                dp[i] = True
                continue

            for j in range(i - 1, -1, -1):
                if dp[j] and s[j+1:i+1] in words:
                    dp[i] = True
                    break
                
        return dp[-1]
# @lc code=end

s = Solution()
print(s.wordBreak(s = "leetcode", wordDict = ["leet", "code"]))
print(s.wordBreak(s = "applepenapple", wordDict = ["apple", "pen"]))
print(s.wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]))

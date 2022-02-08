#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
# https://leetcode-cn.com/problems/group-anagrams/description/
#
# algorithms
# Medium (66.84%)
# Likes:    971
# Dislikes: 0
# Total Accepted:    266.7K
# Total Submissions: 399.1K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
# 
# 字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
# 
# 示例 2:
# 
# 
# 输入: strs = [""]
# 输出: [[""]]
# 
# 
# 示例 3:
# 
# 
# 输入: strs = ["a"]
# 输出: [["a"]]
# 
# 
# 
# 提示：
# 
# 
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] 仅包含小写字母
# 
# 
#

# @lc code=start
from collections import Counter, defaultdict


class Solution:
    @staticmethod
    def hash(s: str):
        c = Counter(s)
        result = ''
        keys = sorted(c.keys())
        for key in keys:
            result += key * c[key]
        return result


    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = defaultdict(list)
        for s in strs:
            d[Solution.hash(s)].append(s)
        return [d[k] for k in d]
# @lc code=end

s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(s.groupAnagrams([""]))
print(s.groupAnagrams(["a"]))

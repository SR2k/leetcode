#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#
# https://leetcode-cn.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (53.99%)
# Likes:    497
# Dislikes: 0
# Total Accepted:    256.6K
# Total Submissions: 474.8K
# Testcase Example:  '"leetcode"'
#
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
# 
# 
# 
# 示例：
# 
# s = "leetcode"
# 返回 0
# 
# s = "loveleetcode"
# 返回 2
# 
# 
# 
# 
# 提示：你可以假定该字符串只包含小写字母。
# 
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        first_seen = {}

        for i, char in enumerate(s):
            if char in seen and char in first_seen:
                first_seen.pop(char)
            if char not in seen:
                first_seen[char] = i
                seen.add(char)

        values = first_seen.values()
        return min(values) if values else -1
# @lc code=end

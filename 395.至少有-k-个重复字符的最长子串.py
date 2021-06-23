#
# @lc app=leetcode.cn id=395 lang=python3
#
# [395] 至少有 K 个重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
#
# algorithms
# Medium (51.84%)
# Likes:    499
# Dislikes: 0
# Total Accepted:    45.7K
# Total Submissions: 88.1K
# Testcase Example:  '"aaabb"\n3'
#
# 给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串， 要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "aaabb", k = 3
# 输出：3
# 解释：最长子串为 "aaa" ，其中 'a' 重复了 3 次。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "ababbc", k = 2
# 输出：5
# 解释：最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 仅由小写英文字母组成
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        cnt: dict[str, int] = {}
        for char in s: cnt[char] = (cnt.get(char) or 0) + 1
        char_list = list(cnt.keys())

        pair = list(cnt.items())
        pair.sort(key = lambda x: x[1])

        if pair[0][1] >= k: return len(s)

        parts: list[str] = [s]
        for char, count in pair:
            if count >= k: break

            temp = []
            for part in parts:
                cut = part.split(char)
                for c in cut:
                    if c: temp.append(c)

            parts = temp

        r = list(map(lambda x: self.longestSubstring(x, k), parts))
        return max(r or [0])

# @lc code=end


#
# @lc app=leetcode.cn id=291 lang=python3
#
# [291] 单词规律 II
#
# https://leetcode-cn.com/problems/word-pattern-ii/description/
#
# algorithms
# Medium (53.30%)
# Likes:    61
# Dislikes: 0
# Total Accepted:    2.5K
# Total Submissions: 4.6K
# Testcase Example:  '"abab"\n"redblueredblue"'
#
# 给你一种规律 pattern 和一个字符串 str，请你判断 str 是否遵循其相同的规律。
# 
# 这里我们指的是 完全遵循，例如 pattern 里的每个字母和字符串 str 中每个 非空 单词之间，存在着 双射 的对应规律。双射
# 意味着映射双方一一对应，不会存在两个字符映射到同一个字符串，也不会存在一个字符分别映射到两个不同的字符串。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：pattern = "abab", s = "redblueredblue"
# 输出：true
# 解释：一种可能的映射如下：
# 'a' -> "red"
# 'b' -> "blue"
# 
# 示例 2：
# 
# 
# 输入：pattern = "aaaa", s = "asdasdasdasd"
# 输出：true
# 解释：一种可能的映射如下：
# 'a' -> "asd"
# 
# 
# 示例 3：
# 
# 
# 输入：pattern = "abab", s = "asdasdasdasd"
# 输出：true
# 解释：一种可能的映射如下：
# 'a' -> "a"
# 'b' -> "sdasd"
# 注意 'a' 和 'b' 不能同时映射到 "asd"，因为这里的映射是一种双射。
# 
# 
# 示例 4：
# 
# 
# 输入：pattern = "aabb", s = "xyzabcxzyabc"
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# 0 
# pattern 和 s 由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def helper(pattern_matched: int, s_matched: int, s_curr: int, d1: dict[str, str], d2: dict[str, str]):
            # exit
            if pattern_matched >= len(pattern) - 1 or s_curr >= len(s):
                return s_matched == len(s) - 1 and pattern_matched == len(pattern) - 1

            # skip current
            if helper(pattern_matched, s_matched, s_curr + 1, d1, d2):
                return True

            # match current
            curr_pattern_char = pattern[pattern_matched + 1]
            curr_str = s[s_matched + 1:s_curr + 1]

            d1_ok = curr_pattern_char not in d1 or d1[curr_pattern_char] == curr_str
            d2_ok = curr_str not in d2 or d2[curr_str] == curr_pattern_char

            if d1_ok and d2_ok:
                need_pop = curr_pattern_char not in d1
                d1[curr_pattern_char] = curr_str
                d2[curr_str] = curr_pattern_char

                if helper(pattern_matched + 1, s_curr, s_curr + 1, d1, d2):
                    return True

                if need_pop:
                    d1.pop(curr_pattern_char)
                    d2.pop(curr_str)

            return False

        return helper(-1, -1, 0, {}, {})
# @lc code=end

s = Solution()
print(s.wordPatternMatch(pattern = "abab", s = "redblueredblue"))
print(s.wordPatternMatch(pattern = "aaaa", s = "asdasdasdasd"))
print(s.wordPatternMatch(pattern = "abab", s = "asdasdasdasd"))
print(s.wordPatternMatch(pattern = "aabb", s = "xyzabcxzyabc"))
print(s.wordPatternMatch(pattern = "abcd", s = "aaaa"))
print(s.wordPatternMatch("sucks", "teezmmmmteez"))

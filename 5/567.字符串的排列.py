#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#
# https://leetcode.cn/problems/permutation-in-string/description/
#
# algorithms
# Medium (43.92%)
# Likes:    689
# Dislikes: 0
# Total Accepted:    193.4K
# Total Submissions: 440.2K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。
# 
# 换句话说，s1 的排列之一是 s2 的 子串 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s1 = "ab" s2 = "eidbaooo"
# 输出：true
# 解释：s2 包含 s1 的排列之一 ("ba").
# 
# 
# 示例 2：
# 
# 
# 输入：s1= "ab" s2 = "eidboaoo"
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s1.length, s2.length <= 10^4
# s1 和 s2 仅包含小写字母
# 
# 
#

# @lc code=start
def get_index(char: str):
    return ord(char) - ord('a')


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counter = [0 for _ in range(26)]
        diff_count = 0
        for char in s1:
            diff_count += self.update_counter(counter, char, 1)

        for i in range(len(s1)):
            diff_count += self.update_counter(counter, s2[i], -1)

        if diff_count == 0:
            return True

        for i in range(len(s1), len(s2)):
            diff_count += self.update_counter(counter, s2[i - len(s1)], 1)
            diff_count += self.update_counter(counter, s2[i], -1)

            if diff_count == 0:
                return True

        return False

    def update_counter(self, counter: list[int], char: str, delta: int):
        index = get_index(char)
        counter[index] += delta

        if counter[index] == delta:
            return 1
        elif counter[index] == 0:
            return -1
        return 0
# @lc code=end

# print(Solution().checkInclusion("ab", "eidboaooo"))
print(Solution().checkInclusion("ab", "eidbaooo"))

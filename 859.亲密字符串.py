#
# @lc app=leetcode.cn id=859 lang=python3
#
# [859] 亲密字符串
#
# https://leetcode-cn.com/problems/buddy-strings/description/
#
# algorithms
# Easy (29.90%)
# Likes:    150
# Dislikes: 0
# Total Accepted:    26.2K
# Total Submissions: 87.5K
# Testcase Example:  '"ab"\n"ba"'
#
# 给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回 true ；否则返回 false 。
# 
# 交换字母的定义是取两个下标 i 和 j （下标从 0 开始），只要 i!=j 就交换 A[i] 和 A[j] 处的字符。例如，在 "abcd" 中交换下标
# 0 和下标 2 的元素可以生成 "cbad" 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入： A = "ab", B = "ba"
# 输出： true
# 解释： 你可以交换 A[0] = 'a' 和 A[1] = 'b' 生成 "ba"，此时 A 和 B 相等。
# 
# 示例 2：
# 
# 
# 输入： A = "ab", B = "ab"
# 输出： false
# 解释： 你只能交换 A[0] = 'a' 和 A[1] = 'b' 生成 "ba"，此时 A 和 B 不相等。
# 
# 
# 示例 3:
# 
# 
# 输入： A = "aa", B = "aa"
# 输出： true
# 解释： 你可以交换 A[0] = 'a' 和 A[1] = 'a' 生成 "aa"，此时 A 和 B 相等。
# 
# 示例 4：
# 
# 
# 输入： A = "aaaaaaabc", B = "aaaaaaacb"
# 输出： true
# 
# 
# 示例 5：
# 
# 
# 输入： A = "", B = "aa"
# 输出： false
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# 0 
# A 和 B 仅由小写字母构成。
# 
# 
#

# @lc code=start
from collections import Counter


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return max(Counter(s).values()) >= 2

        char_s, char_g, replaced = None, None, False
        for i in range(len(s)):
            if s[i] == goal[i]:
                continue

            if not char_s:
                char_s = s[i]
                char_g = goal[i]
            elif not replaced:
                if s[i] != char_g or goal[i] != char_s:
                    return False
                replaced = True
            else:
                return False

        if replaced:
            return True
        return not char_s
# @lc code=end


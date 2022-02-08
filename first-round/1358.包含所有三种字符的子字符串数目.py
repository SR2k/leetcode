#
# @lc app=leetcode.cn id=1358 lang=python3
#
# [1358] 包含所有三种字符的子字符串数目
#
# https://leetcode-cn.com/problems/number-of-substrings-containing-all-three-characters/description/
#
# algorithms
# Medium (48.08%)
# Likes:    48
# Dislikes: 0
# Total Accepted:    4.9K
# Total Submissions: 10.3K
# Testcase Example:  '"abcabc"'
#
# 给你一个字符串 s ，它只包含三种字符 a, b 和 c 。
# 
# 请你返回 a，b 和 c 都 至少 出现过一次的子字符串数目。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "abcabc"
# 输出：10
# 解释：包含 a，b 和 c 各至少一次的子字符串为 "abc", "abca", "abcab", "abcabc", "bca", "bcab",
# "bcabc", "cab", "cabc" 和 "abc" (相同字符串算多次)。
# 
# 
# 示例 2：
# 
# 输入：s = "aaacb"
# 输出：3
# 解释：包含 a，b 和 c 各至少一次的子字符串为 "aaacb", "aacb" 和 "acb" 。
# 
# 
# 示例 3：
# 
# 输入：s = "abc"
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 3 <= s.length <= 5 x 10^4
# s 只包含字符 a，b 和 c 。
# 
# 
#

# @lc code=start
# def b_find(arr: list[int], n: int, left: int) -> int:
#     right = len(arr) - 1
#     while left + 1 < right:
#         middle = (left + right) // 2
#         nm = arr[middle]

#         if nm <= n:
#             left = middle
#         else:
#             right = middle

#     if arr[left] > n:
#         return left
#     if arr[right] > n:
#         return right
#     return -1


# class Solution:
#     def numberOfSubstrings(self, s: str) -> int:
#         ca, cb, cc = [0], [0], [0]
#         len_s = len(s)

#         for char in s:
#             ca.append((ca[-1] + 1) if char == 'a' else ca[-1])
#             cb.append((cb[-1] + 1) if char == 'b' else cb[-1])
#             cc.append((cc[-1] + 1) if char == 'c' else cc[-1])

#         ret = 0
#         for i in range(len(ca)):
#             a, b, c = ca[i], cb[i], cc[i]
#             na, nb, nc = b_find(ca, a, i), b_find(cb, b, i), b_find(cc, c, i)
#             if na < i or nb < i or nc < i:
#                 return ret
#             ret += len_s - max(na, nb, nc) + 1

#         return ret


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        right = -1
        count = { 'a': 0,  'b': 0,  'c': 0 }

        ret, len_s = 0, len(s)

        for left in range(len_s):
            while count['a'] <= 0 or count['b'] <= 0 or count['c'] <= 0:
                right += 1
                if right >= len_s: return ret
                count[s[right]] += 1
            
            ret += len_s - right
            count[s[left]] -= 1

        return ret
# @lc code=end

print(Solution().numberOfSubstrings("abcabc"))

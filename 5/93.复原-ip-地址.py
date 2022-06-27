#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#
# https://leetcode.cn/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (56.19%)
# Likes:    915
# Dislikes: 0
# Total Accepted:    225.4K
# Total Submissions: 400.4K
# Testcase Example:  '"25525511135"'
#
# 有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
# 
# 
# 例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312"
# 和 "192.168@1.1" 是 无效 IP 地址。
# 
# 
# 给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。你 不能
# 重新排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "25525511135"
# 输出：["255.255.11.135","255.255.111.35"]
# 
# 
# 示例 2：
# 
# 
# 输入：s = "0000"
# 输出：["0.0.0.0"]
# 
# 
# 示例 3：
# 
# 
# 输入：s = "101023"
# 输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 20
# s 仅由数字组成
# 
# 
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        s: list[int] = [int(c) for c in s]

        def helper(curr: list[int], i: int, result: list[str]):
            if i == len(s):
                if len(curr) == 4:
                    result.append(".".join([str(x) for x in curr]))
                return

            if len(curr) > 4:
                return

            if len(curr) < 4:
                curr.append(s[i])
                helper(curr, i + 1, result)
                curr.pop()

            if curr and (curr[-1] != 0) and curr[-1] * 10 + s[i] <= 255:
                original = curr[-1]
                curr[-1] = curr[-1] * 10 + s[i]
                helper(curr, i + 1, result)
                curr[-1] = original

        result = []
        helper([], 0, result)
        return result
# @lc code=end

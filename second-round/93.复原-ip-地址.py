#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#
# https://leetcode-cn.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (54.90%)
# Likes:    771
# Dislikes: 0
# Total Accepted:    178.1K
# Total Submissions: 324.2K
# Testcase Example:  '"25525511135"'
#
# 有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
# 
# 
# 例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312"
# 和 "192.168@1.1" 是 无效 IP 地址。
# 
# 
# 给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.'
# 来形成。你不能重新排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。
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
# 输入：s = "1111"
# 输出：["1.1.1.1"]
# 
# 
# 示例 4：
# 
# 
# 输入：s = "010010"
# 输出：["0.10.0.10","0.100.1.0"]
# 
# 
# 示例 5：
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
# 0 <= s.length <= 20
# s 仅由数字组成
# 
# 
#

# @lc code=start
class Solution:
    @staticmethod
    def check_add(a: int, b: int):
        if a == 0:
            return -1
        add_result = a * 10 + b
        if not 0 <  add_result <= 255:
            return -1
        return add_result


    def restoreIpAddresses(self, s: str) -> list[str]:
        result = []

        def helper(curr: list[int], i: int):
            if i == len(s):
                if len(curr) == 4:
                    result.append(".".join(str(d) for d in curr))
                return

            digit = int(s[i])

            # add a new part
            if len(curr) < 4:
                curr.append(digit)
                helper(curr, i + 1)
                curr.pop()

            # add to prev part
            if curr:
                tail = curr[-1]
                add_result = Solution.check_add(tail, digit)
                if add_result > 0:
                    curr[-1] = add_result
                    helper(curr, i + 1)
                    curr[-1] = tail

        helper([], 0)
        return result
# @lc code=end

s = Solution()
print(s.restoreIpAddresses(s = "25525511135"))
print(s.restoreIpAddresses(s = "0000"))
print(s.restoreIpAddresses(s = "1111"))
print(s.restoreIpAddresses(s = "010010"))
print(s.restoreIpAddresses(s = "101023"))

#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#
# https://leetcode-cn.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (55.81%)
# Likes:    864
# Dislikes: 0
# Total Accepted:    209.9K
# Total Submissions: 375.8K
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
        result = []

        def helper(prev: int, i: int, mapped: list[str]):
            if i >= len(s):
                if prev == len(s) - 1 and len(mapped) == 4:
                    result.append(".".join(mapped))
                return

            if len(mapped) == 4:
                return

            part = s[prev + 1:i + 1]
            if int(part) > 255:
                return
            if part[0] == '0' and part != '0':
                return

            # append
            helper(prev, i + 1, mapped)

            # new segment
            mapped.append(s[prev + 1:i + 1])
            helper(i, i + 1, mapped)
            mapped.pop()

        helper(-1, 0, [])
        return result
# @lc code=end

s = Solution()
print(s.restoreIpAddresses( "25525511135"))
print(s.restoreIpAddresses( "0000"))
print(s.restoreIpAddresses("101023"))

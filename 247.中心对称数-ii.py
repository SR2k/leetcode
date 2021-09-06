#
# @lc app=leetcode.cn id=247 lang=python3
#
# [247] 中心对称数 II
#
# https://leetcode-cn.com/problems/strobogrammatic-number-ii/description/
#
# algorithms
# Medium (52.19%)
# Likes:    62
# Dislikes: 0
# Total Accepted:    5K
# Total Submissions: 9.6K
# Testcase Example:  '2'
#
# 中心对称数是指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。
# 
# 找到所有长度为 n 的中心对称数。
# 
# 示例 :
# 
# 输入:  n = 2
# 输出: ["11","69","88","96"]
# 
# 
#

# @lc code=start
DIGIT_MAP = {
    '0': '0',
    '1': '1',
    '6': '9',
    '8': '8',
    '9': '6',
}


def map_half_str(s: str):
    t = ''
    for c in s:
        t += DIGIT_MAP[c]
    return t[::-1]

class Solution:
    def findStrobogrammatic(self, n: int) -> list[str]:
        digits = ['0', '1', '6', '8', '9']
        non_zero_digits = ['1', '6',  '8', '9']
        self_to_self = ['0', '1', '8']

        if n == 1:
            return self_to_self

        temp = []
        for i in range(n // 2):
            if i == 0:
                for d in non_zero_digits:
                    temp.append(d)
            else:
                inner_temp = []
                for t in temp:
                    for d in digits:
                        inner_temp.append(t + d)
                temp = inner_temp

        if n % 2 == 0:
            return [t + map_half_str(t) for t in temp]

        ret = []
        for t in temp:
            r = map_half_str(t)
            for d in self_to_self:
                ret.append(t + d + r)

        return ret
# @lc code=end


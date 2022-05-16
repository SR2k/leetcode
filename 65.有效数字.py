#
# @lc app=leetcode.cn id=65 lang=python3
#
# [65] 有效数字
#
# https://leetcode.cn/problems/valid-number/description/
#
# algorithms
# Hard (27.36%)
# Likes:    310
# Dislikes: 0
# Total Accepted:    54.3K
# Total Submissions: 198.4K
# Testcase Example:  '"0"'
#
# 有效数字（按顺序）可以分成以下几个部分：
# 
# 
# 一个 小数 或者 整数
# （可选）一个 'e' 或 'E' ，后面跟着一个 整数
# 
# 
# 小数（按顺序）可以分成以下几个部分：
# 
# 
# （可选）一个符号字符（'+' 或 '-'）
# 下述格式之一：
# 
# 至少一位数字，后面跟着一个点 '.'
# 至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
# 一个点 '.' ，后面跟着至少一位数字
# 
# 
# 
# 
# 整数（按顺序）可以分成以下几个部分：
# 
# 
# （可选）一个符号字符（'+' 或 '-'）
# 至少一位数字
# 
# 
# 部分有效数字列举如下：["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3",
# "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
# 
# 部分无效数字列举如下：["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
# 
# 给你一个字符串 s ，如果 s 是一个 有效数字 ，请返回 true 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "0"
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：s = "e"
# 输出：false
# 
# 
# 示例 3：
# 
# 
# 输入：s = "."
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 20
# s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，或者点 '.' 。
# 
# 
#

# @lc code=start
from enum import Enum


class Status(Enum):
    START = 'START'
    SIGN = 'SIGN'
    WHOLE = 'WHOLE'
    POINT = 'POINT'
    POINT_NO_WHOLE = 'POINT_NO_WHOLE'
    DECIMAL = 'DECIMAL'
    E = 'E'
    INDEX_SIGN = 'INDEX_SIGN'
    INDEX = 'INDEX'


class Solution:
    def isNumber(self, s: str) -> bool:
        status = Status.START

        for char in s:
            if '0' <= char <= '9':
                if status in [Status.START, Status.SIGN, status.WHOLE]:
                    status = Status.WHOLE
                elif status in [Status.POINT, Status.POINT_NO_WHOLE, Status.DECIMAL]:
                    status = Status.DECIMAL
                elif status in [Status.E, status.INDEX_SIGN, Status.INDEX]:
                    status = status.INDEX

            elif char in ['+', '-']:
                if status == Status.START:
                    status = Status.SIGN
                elif status == Status.E:
                    status = Status.INDEX_SIGN
                else:
                    # print('    >> returned for +/-', status)
                    return False

            elif char == '.':
                if status in [Status.START, Status.SIGN]:
                    status = Status.POINT_NO_WHOLE
                elif status == Status.WHOLE:
                    status = Status.POINT
                else:
                    # print('    >> returned for .', status)
                    return False

            elif char in ['e', 'E']:
                if status in [Status.WHOLE, Status.POINT, Status.DECIMAL]:
                    status = Status.E
                else:
                    # print('    >> returned for e/E', status)
                    return False

            else:
                # print('    >> returned for other char', status)
                return False

        # print('    >> ', s, status)
        return status in [Status.WHOLE, Status.POINT, Status.DECIMAL, Status.INDEX]
# @lc code=end

s = Solution()
falsy = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
for f in falsy:
    print('falsy', f, s.isNumber(f))

truthy = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
for t in truthy:
    print('truthy', t, s.isNumber(t))


# "-53.5e-93"
#        START          SIGN           WHOLE POINT   POINT_NO_WHOLE DECIMAL E           INDEX_SIGN INDEX
# 0-9    WHOLE          WHOLE          WHOLE DECIMAL DECIMAL        DECIMAL INDEX       INDEX      INDEX
# +/-    SIGN           false          false false   false          false   INDEX_SIGN  false      false
# .      POINT_NO_WHOLE POINT_NO_WHOLE POINT false   false          false   false       false      false
# e/E    false          false          E     E       false          E       false       false      false
# other  -------------------- all false ---------------------------------------- 

# 有效数字（按顺序）可以分成以下几个部分：
# 
# 
# 一个 小数 或者 整数
# （可选）一个 'e' 或 'E' ，后面跟着一个 整数
# 
# 
# 小数（按顺序）可以分成以下几个部分：
# 
# 
# （可选）一个符号字符（'+' 或 '-'）
# 下述格式之一：
# 
# 至少一位数字，后面跟着一个点 '.'
# 至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
# 一个点 '.' ，后面跟着至少一位数字
# 
# 
# 
# 
# 整数（按顺序）可以分成以下几个部分：
# 
# 
# （可选）一个符号字符（'+' 或 '-'）
# 至少一位数字
# 
# 
# 部分有效数字列举如下：["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3",
# "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
# 
# 部分无效数字列举如下：["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
# 
# 给你一个字符串 s ，如果 s 是一个 有效数字 ，请返回 true 。

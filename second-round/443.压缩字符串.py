#
# @lc app=leetcode.cn id=443 lang=python3
#
# [443] 压缩字符串
#
# https://leetcode-cn.com/problems/string-compression/description/
#
# algorithms
# Medium (47.79%)
# Likes:    283
# Dislikes: 0
# Total Accepted:    60K
# Total Submissions: 125.6K
# Testcase Example:  '["a","a","b","b","c","c","c"]'
#
# 给你一个字符数组 chars ，请使用下述算法压缩：
# 
# 从一个空字符串 s 开始。对于 chars 中的每组 连续重复字符 ：
# 
# 
# 如果这一组长度为 1 ，则将字符追加到 s 中。
# 否则，需要向 s 追加字符，后跟这一组的长度。
# 
# 
# 压缩后得到的字符串 s 不应该直接返回 ，需要转储到字符数组 chars 中。需要注意的是，如果组长度为 10 或 10 以上，则在 chars
# 数组中会被拆分为多个字符。
# 
# 请在 修改完输入数组后 ，返回该数组的新长度。
# 
# 你必须设计并实现一个只使用常量额外空间的算法来解决此问题。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：chars = ["a","a","b","b","c","c","c"]
# 输出：返回 6 ，输入数组的前 6 个字符应该是：["a","2","b","2","c","3"]
# 解释：
# "aa" 被 "a2" 替代。"bb" 被 "b2" 替代。"ccc" 被 "c3" 替代。
# 
# 
# 示例 2：
# 
# 
# 输入：chars = ["a"]
# 输出：返回 1 ，输入数组的前 1 个字符应该是：["a"]
# 解释：
# 没有任何字符串被替代。
# 
# 
# 示例 3：
# 
# 
# 输入：chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# 输出：返回 4 ，输入数组的前 4 个字符应该是：["a","b","1","2"]。
# 解释：
# 由于字符 "a" 不重复，所以不会被压缩。"bbbbbbbbbbbb" 被 “b12” 替代。
# 注意每个数字在数组中都有它自己的位置。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= chars.length <= 2000
# chars[i] 可以是小写英文字母、大写英文字母、数字或符号
# 
# 
#

# @lc code=start
class Solution:
    def compress(self, chars: list[str]) -> int:
        p, cnt, char = 0, 1, chars[0]

        def write():
            nonlocal p
            str = f"{char}{cnt}" if cnt > 1 else char
            for c in str:
                chars[p] = c
                p += 1

        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                cnt += 1
            else:
                write()
                char = chars[i]
                cnt = 1

        write()
        return p
# @lc code=end

s = Solution()
chars = chars = ["a","a","b","b","c","c","c"]
p = s.compress(chars)
print(p, chars, chars[:p])

chars = chars = ["a"]
p = s.compress(chars)
print(p, chars, chars[:p])

chars = chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
p = s.compress(chars)
print(p, chars, chars[:p])


#
# @lc app=leetcode.cn id=925 lang=python3
#
# [925] 长按键入
#
# https://leetcode-cn.com/problems/long-pressed-name/description/
#
# algorithms
# Easy (38.94%)
# Likes:    209
# Dislikes: 0
# Total Accepted:    48.7K
# Total Submissions: 125.1K
# Testcase Example:  '"alex"\n"aaleex"'
#
# 你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。
# 
# 你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。
# 
# 
# 
# 示例 1：
# 
# 输入：name = "alex", typed = "aaleex"
# 输出：true
# 解释：'alex' 中的 'a' 和 'e' 被长按。
# 
# 
# 示例 2：
# 
# 输入：name = "saeed", typed = "ssaaedd"
# 输出：false
# 解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。
# 
# 
# 示例 3：
# 
# 输入：name = "leelee", typed = "lleeelee"
# 输出：true
# 
# 
# 示例 4：
# 
# 输入：name = "laiden", typed = "laiden"
# 输出：true
# 解释：长按名字中的字符并不是必要的。
# 
# 
# 
# 
# 提示：
# 
# 
# name.length <= 1000
# typed.length <= 1000
# name 和 typed 的字符都是小写字母。
# 
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        p1, p2 = 0, 0
        count1, count2 = 0, 0
        len_name, len_typed = len(name), len(typed)

        if len_typed < len_name:
            return False

        while p1 < len_name and p2 < len_typed:
            count1, count2 = p1, p2
            while p1 < len_name - 1 and name[p1] == name[p1 + 1]:
                p1 += 1
            count1 = p1 - count1 + 1

            while p2 < len_typed - 1 and typed[p2] == typed[p2 + 1]:
                p2 += 1
            count2 = p2 - count2 + 1

            if name[p1] != typed[p2] or count1 > count2:
                return False

            p1 += 1
            p2 += 1

        return p1 == len_name - 1 and p2 == len_typed - 1
# @lc code=end

print(Solution().isLongPressedName("xnhtq", "xhhttqq"))

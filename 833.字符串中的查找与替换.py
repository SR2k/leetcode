#
# @lc app=leetcode.cn id=833 lang=python3
#
# [833] 字符串中的查找与替换
#
# https://leetcode-cn.com/problems/find-and-replace-in-string/description/
#
# algorithms
# Medium (42.36%)
# Likes:    49
# Dislikes: 0
# Total Accepted:    4.6K
# Total Submissions: 10.9K
# Testcase Example:  '"abcd"\n[0, 2]\n["a", "cd"]\n["eee", "ffff"]'
#
# 某个字符串 S 需要执行一些替换操作，用新的字母组替换原有的字母组（不一定大小相同）。
# 
# 每个替换操作具有 3 个参数：起始索引 i，源字 x 和目标字 y。规则是：如果 x 从原始字符串 S 中的位置 i 开始，那么就用 y 替换出现的
# x。如果没有，则什么都不做。
# 
# 举个例子，如果 S = “abcd” 并且替换操作 i = 2，x = “cd”，y = “ffff”，那么因为 “cd” 从原始字符串 S 中的位置 2
# 开始，所以用 “ffff” 替换它。
# 
# 再来看 S = “abcd” 上的另一个例子，如果一个替换操作 i = 0，x = “ab”，y = “eee”，以及另一个替换操作 i = 2，x =
# “ec”，y = “ffff”，那么第二个操作将不会执行，因为原始字符串中 S[2] = 'c'，与 x[0] = 'e' 不匹配。
# 
# 所有这些操作同时发生。保证在替换时不会有任何重叠： S = "abc", indexes = [0, 1], sources = ["ab","bc"]
# 不是有效的测试用例。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：S = "abcd", indexes = [0,2], sources = ["a","cd"], targets =
# ["eee","ffff"]
# 输出："eeebffff"
# 解释：
# "a" 从 S 中的索引 0 开始，所以它被替换为 "eee"。
# "cd" 从 S 中的索引 2 开始，所以它被替换为 "ffff"。
# 
# 
# 示例 2：
# 
# 
# 输入：S = "abcd", indexes = [0,2], sources = ["ab","ec"], targets =
# ["eee","ffff"]
# 输出："eeecd"
# 解释：
# "ab" 从 S 中的索引 0 开始，所以它被替换为 "eee"。
# "ec" 没有从原始的 S 中的索引 2 开始，所以它没有被替换。
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# S 仅由小写英文字母组成
# 0 
# 0 
# sources.length == indexes.length
# targets.length == indexes.length
# 1 
# sources[i] 和 targets[i] 仅由小写英文字母组成
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def findReplaceString(self, s: str, indices: list[int], sources: list[str], targets: list[str]) -> str:
        ptr, ret = 0, ''
        operations = [(indices[i], sources[i], targets[i]) for i in range(len(indices))]
        operations.sort(key=lambda x: x[0])

        for o in operations:
            i, source, target = o
            ret += s[ptr:i]
            original = s[i:i + len(source)]

            if original == source:
                ret += target
            else:
                ret += original

            ptr = i + len(source)

        if ptr < len(s):
            ret += s[ptr:]

        return ret
# @lc code=end


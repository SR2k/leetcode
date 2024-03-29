#
# @lc app=leetcode.cn id=839 lang=python3
#
# [839] 相似字符串组
#
# https://leetcode-cn.com/problems/similar-string-groups/description/
#
# algorithms
# Hard (57.32%)
# Likes:    124
# Dislikes: 0
# Total Accepted:    18.5K
# Total Submissions: 32.3K
# Testcase Example:  '["tars","rats","arts","star"]'
#
# 如果交换字符串 X 中的两个不同位置的字母，使得它和字符串 Y 相等，那么称 X 和 Y
# 两个字符串相似。如果这两个字符串本身是相等的，那它们也是相似的。
# 
# 例如，"tars" 和 "rats" 是相似的 (交换 0 与 2 的位置)； "rats" 和 "arts" 也是相似的，但是 "star" 不与
# "tars"，"rats"，或 "arts" 相似。
# 
# 总之，它们通过相似性形成了两个关联组：{"tars", "rats", "arts"} 和 {"star"}。注意，"tars" 和 "arts"
# 是在同一组中，即使它们并不相似。形式上，对每个组而言，要确定一个单词在组中，只需要这个词和该组中至少一个单词相似。
# 
# 给你一个字符串列表 strs。列表中的每个字符串都是 strs 中其它所有字符串的一个字母异位词。请问 strs 中有多少个相似字符串组？
# 
# 
# 
# 示例 1：
# 
# 
# 输入：strs = ["tars","rats","arts","star"]
# 输出：2
# 
# 
# 示例 2：
# 
# 
# 输入：strs = ["omv","ovm"]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# strs[i] 只包含小写字母。
# strs 中的所有单词都具有相同的长度，且是彼此的字母异位词。
# 
# 
# 
# 
# 备注：
# 
# 字母异位词（anagram），一种把某个字符串的字母的位置（顺序）加以改换所形成的新词。
# 
#

# @lc code=start
def check(a: str, b: str) -> int:
    diff_count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff_count += 1
        if diff_count > 2:
            return False
    return True


def find_root(parents: list[int], i: int) -> int:
    while parents[i] != i:
        i = parents[i]
    return i


class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int:
        count = len(strs)
        parents = [i for i in range(count)]
        ret = count

        for i in range(count - 1):
            for j in range(1, count):
                if check(strs[i], strs[j]):
                    root_i, root_j = find_root(parents, i), find_root(parents, j)
                    if root_i != root_j:
                        ret -= 1
                    parents[root_i] = root_j

        return ret
# @lc code=end


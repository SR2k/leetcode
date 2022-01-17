#
# @lc app=leetcode.cn id=288 lang=python3
#
# [288] 单词的唯一缩写
#
# https://leetcode-cn.com/problems/unique-word-abbreviation/description/
#
# algorithms
# Medium (42.73%)
# Likes:    13
# Dislikes: 0
# Total Accepted:    3.3K
# Total Submissions: 7.8K
# Testcase Example:  '["ValidWordAbbr","isUnique","isUnique","isUnique","isUnique","isUnique"]\n' +
#  '[[["deer","door","cake","card"]],["dear"],["cart"],["cane"],["make"],["cake"]]'
#
# 单词的 缩写 需要遵循  这样的格式。如果单词只有两个字符，那么它就是它自身的 缩写 。
# 
# 以下是一些单词缩写的范例：
# 
# 
# dog --> d1g 因为第一个字母 'd' 和最后一个字母 'g' 之间有 1 个字母
# internationalization --> i18n 因为第一个字母 'i' 和最后一个字母 'n' 之间有 18 个字母
# it --> it 单词只有两个字符，它就是它自身的 缩写
# 
# 
# 
# 
# 实现 ValidWordAbbr 类：
# 
# 
# ValidWordAbbr(String[] dictionary) 使用单词字典 dictionary 初始化对象
# boolean isUnique(string word) 如果满足下述任意一个条件，返回 true ；否则，返回 false
# ：
# 
# 字典 dictionary 中没有任何其他单词的 缩写 与该单词 word 的 缩写 相同。
# 字典 dictionary 中的所有 缩写 与该单词 word 的 缩写 相同的单词都与 word 相同 。
# 
# 
# 
# 
# 
# 
# 示例：
# 
# 
# 输入
# ["ValidWordAbbr", "isUnique", "isUnique", "isUnique", "isUnique", "isUnique"]
# [[["deer", "door", "cake", "card"]], ["dear"], ["cart"], ["cane"], ["make"],
# ["cake"]]
# 输出
# [null, false, true, false, true, true]
# 
# 解释
# ValidWordAbbr validWordAbbr = new ValidWordAbbr(["deer", "door", "cake",
# "card"]);
# validWordAbbr.isUnique("dear"); // 返回 false，字典中的 "deer" 与输入 "dear" 的缩写都是
# "d2r"，但这两个单词不相同
# validWordAbbr.isUnique("cart"); // 返回 true，字典中不存在缩写为 "c2t" 的单词
# validWordAbbr.isUnique("cane"); // 返回 false，字典中的 "cake" 与输入 "cane" 的缩写都是
# "c2e"，但这两个单词不相同
# validWordAbbr.isUnique("make"); // 返回 true，字典中不存在缩写为 "m2e" 的单词
# validWordAbbr.isUnique("cake"); // 返回 true，因为 "cake" 已经存在于字典中，并且字典中没有其他缩写为
# "c2e" 的单词
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# dictionary[i] 由小写英文字母组成
# 1 
# word 由小写英文字母组成
# 最多调用 5000 次 isUnique
# 
# 
#

# @lc code=start
from collections import defaultdict


def zip_it(s: str):
    if len(s) <= 2:
        return s
    return s[0] + str(len(s) - 2) + s[-1]


class ValidWordAbbr:
    def __init__(self, dictionary: list[str]):
        self.zipped_to_word = defaultdict(set)

        for word in dictionary:
            zipped = zip_it(word)
            self.zipped_to_word[zipped].add(word)

    def isUnique(self, word: str) -> bool:
        s = self.zipped_to_word[zip_it(word)]
        return (len(s) == 1 and word in s) or len(s) == 0

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
# @lc code=end

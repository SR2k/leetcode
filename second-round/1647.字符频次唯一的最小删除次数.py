#
# @lc app=leetcode.cn id=1647 lang=python3
#
# [1647] 字符频次唯一的最小删除次数
#
# https://leetcode-cn.com/problems/minimum-deletions-to-make-character-frequencies-unique/description/
#
# algorithms
# Medium (52.07%)
# Likes:    34
# Dislikes: 0
# Total Accepted:    8.2K
# Total Submissions: 15.7K
# Testcase Example:  '"aab"'
#
# 如果字符串 s 中 不存在 两个不同字符 频次 相同的情况，就称 s 是 优质字符串 。
# 
# 给你一个字符串 s，返回使 s 成为 优质字符串 需要删除的 最小 字符数。
# 
# 字符串中字符的 频次 是该字符在字符串中的出现次数。例如，在字符串 "aab" 中，'a' 的频次是 2，而 'b' 的频次是 1 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "aab"
# 输出：0
# 解释：s 已经是优质字符串。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "aaabbbcc"
# 输出：2
# 解释：可以删除两个 'b' , 得到优质字符串 "aaabcc" 。
# 另一种方式是删除一个 'b' 和一个 'c' ，得到优质字符串 "aaabbc" 。
# 
# 示例 3：
# 
# 
# 输入：s = "ceabaacb"
# 输出：2
# 解释：可以删除两个 'c' 得到优质字符串 "eabaab" 。
# 注意，只需要关注结果字符串中仍然存在的字符。（即，频次为 0 的字符会忽略不计。）
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 仅含小写英文字母
# 
# 
#

# @lc code=start
from collections import Counter, deque


class Solution:
    def minDeletions(self, s: str) -> int:
        counts = Counter(s).values()
        counter_of_count = Counter(counts)
        counts = deque(sorted(counter_of_count.keys(), key=lambda x: -x))
        result = 0

        while counts:
            count = counts.popleft()
            if not count or not counter_of_count[count]:
                continue

            reduced = counter_of_count[count] - 1
            result += reduced

            if not counts or counts[0] != count - 1:
                counts.appendleft(count - 1)
            counter_of_count[count - 1] += reduced

        return result
# @lc code=end

s = Solution()
print(s.minDeletions("aab"))
print(s.minDeletions("aaabbbcc"))
print(s.minDeletions("ceabaacb"))
print(s.minDeletions("aaaabbbbcccc"))
print(s.minDeletions("bbcebab")) # 2

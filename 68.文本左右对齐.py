#
# @lc app=leetcode.cn id=68 lang=python3
#
# [68] 文本左右对齐
#
# https://leetcode-cn.com/problems/text-justification/description/
#
# algorithms
# Hard (47.05%)
# Likes:    172
# Dislikes: 0
# Total Accepted:    22.3K
# Total Submissions: 45.5K
# Testcase Example:  '["This", "is", "an", "example", "of", "text", "justification."]\n16'
#
# 给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。
# 
# 你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。
# 
# 要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
# 
# 文本的最后一行应为左对齐，且单词之间不插入额外的空格。
# 
# 说明:
# 
# 
# 单词是指由非空格字符组成的字符序列。
# 每个单词的长度大于 0，小于等于 maxWidth。
# 输入单词数组 words 至少包含一个单词。
# 
# 
# 示例:
# 
# 输入:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# 输出:
# [
# "This    is    an",
# "example  of text",
# "justification.  "
# ]
# 
# 
# 示例 2:
# 
# 输入:
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# 输出:
# [
# "What   must   be",
# "acknowledgment  ",
# "shall be        "
# ]
# 解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
# 因为最后一行应为左对齐，而不是左右两端对齐。       
# ⁠    第二行同样为左对齐，这是因为这行只包含一个单词。
# 
# 
# 示例 3:
# 
# 输入:
# words =
# ["Science","is","what","we","understand","well","enough","to","explain",
# "to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
# 输出:
# [
# "Science  is  what we",
# ⁠ "understand      well",
# "enough to explain to",
# "a  computer.  Art is",
# "everything  else  we",
# "do                  "
# ]
# 
# 
#

# @lc code=start
from collections import deque


class Solution:
    def fullJustify(self, w: list[str], maxWidth: int) -> list[str]:
        words = deque(w)
        result = []

        while words:
            first_word = words.popleft()
            level_length = len(first_word)
            level_words = [first_word]

            while words and len(words[0]) + level_length + 1 <= maxWidth:
                word = words.popleft()
                level_length += len(word) + 1
                level_words.append(word)

            extra_spaces = maxWidth - level_length

            gap_count = len(level_words) - 1
            if gap_count != 0:
                base_spaces_count = extra_spaces // gap_count + 1
                extra_single_space_count = extra_spaces % gap_count
            else:
                base_spaces_count = 0
                extra_single_space_count = 0

            level_result = ""
            for i, word in enumerate(level_words):
                level_result += word

                if i + 1 <= extra_single_space_count:
                    space_count = base_spaces_count + 1
                elif i == len(level_words) - 1:
                    space_count = maxWidth - len(level_result)
                else:
                    space_count = base_spaces_count

                level_result += (' ' * space_count)

            result.append(level_result)

        result.pop()
        last_row = " ".join(level_words)
        last_row += ' ' * (maxWidth - len(last_row))
        result.append(last_row)

        return result
# @lc code=end

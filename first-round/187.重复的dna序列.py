#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#
# https://leetcode-cn.com/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (47.57%)
# Likes:    175
# Dislikes: 0
# Total Accepted:    34.9K
# Total Submissions: 73.2K
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
# 所有 DNA 都由一系列缩写为 'A'，'C'，'G' 和 'T' 的核苷酸组成，例如："ACGAATTCCG"。在研究 DNA 时，识别 DNA
# 中的重复序列有时会对研究非常有帮助。
# 
# 编写一个函数来找出所有目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 输出：["AAAAACCCCC","CCCCCAAAAA"]
# 
# 
# 示例 2：
# 
# 
# 输入：s = "AAAAAAAAAAAAA"
# 输出：["AAAAAAAAAA"]
# 
# 
# 
# 
# 提示：
# 
# 
# 0
# s[i] 为 'A'、'C'、'G' 或 'T'
# 
# 
#

# @lc code=start
H, L = 10, 10
CHAR_CODE = { 'A': 1, 'C': 2, 'G': 3, 'T': 4 }


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        if len(s) <= 10:
            return []

        seen, result = {}, set()
        i, hash = 0, 0
        while i < L:
            hash = hash * H + CHAR_CODE[s[i]]
            i += 1
        seen[hash] = s[:i]

        while i < len(s):
            hash -= CHAR_CODE[s[i - 10]] * (H ** (L - 1))
            hash *= H
            hash += CHAR_CODE[s[i]]

            if hash in seen:
                result.add(hash)
            else:
                seen[hash] = s[i - L + 1:i + 1]

            i += 1

        return list(map(lambda hash: seen[hash], result))
# @lc code=end

class Solution1:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        ret, len_s = [], len(s)
        if len_s < 10:
            return ret

        left, right = 0, 9
        freq: dict[str, int] = {}
        while right < len_s:
            sub_str = s[left:right + 1]
            freq[sub_str] = 1 + (freq.get(sub_str) or 0)
            left += 1
            right += 1

        for k in freq.keys():
            if freq[k] > 1:
                ret.append(k)
        return ret

s = Solution()
s1 = Solution1()

print(s.findRepeatedDnaSequences('AAAAAAAGGGTTTAAACCCCCAAAAACCCCCCAAAAAGGGTTT'))
print(s1.findRepeatedDnaSequences('AAAAAAAGGGTTTAAACCCCCAAAAACCCCCCAAAAAGGGTTT'))

print(s.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'))
print(s1.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'))

print(s.findRepeatedDnaSequences('AAAAAAAAAAAAAAAAAAAAAAACCCCCCCCCCCAAAAAAAAAAAA'))
print(s1.findRepeatedDnaSequences('AAAAAAAAAAAAAAAAAAAAAAACCCCCCCCCCCAAAAAAAAAAAA'))


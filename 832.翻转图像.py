#
# @lc app=leetcode.cn id=832 lang=python3
#
# [832] 翻转图像
#
# https://leetcode-cn.com/problems/flipping-an-image/description/
#
# algorithms
# Easy (79.52%)
# Likes:    257
# Dislikes: 0
# Total Accepted:    83.3K
# Total Submissions: 104.7K
# Testcase Example:  '[[1,1,0],[1,0,1],[0,0,0]]'
#
# 给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。
# 
# 水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。
# 
# 反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：[[1,1,0],[1,0,1],[0,0,0]]
# 输出：[[1,0,0],[0,1,0],[1,1,1]]
# 解释：首先翻转每一行: [[0,1,1],[1,0,1],[0,0,0]]；
# ⁠    然后反转图片: [[1,0,0],[0,1,0],[1,1,1]]
# 
# 
# 示例 2：
# 
# 
# 输入：[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# 输出：[[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# 解释：首先翻转每一行: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]；
# ⁠    然后反转图片: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 
# 
#

# @lc code=start
import math

class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        n = len(image[0])
        half = math.floor((n + 1) / 2)

        for row in image:
            for i in range(half):
                reversed_index = n - i - 1
                row[i], row[reversed_index] = 1 - row[reversed_index], 1 - row[i]

        return image

# @lc code=end


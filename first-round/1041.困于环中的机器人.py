#
# @lc app=leetcode.cn id=1041 lang=python3
#
# [1041] 困于环中的机器人
#
# https://leetcode-cn.com/problems/robot-bounded-in-circle/description/
#
# algorithms
# Medium (47.76%)
# Likes:    81
# Dislikes: 0
# Total Accepted:    6.2K
# Total Submissions: 12.8K
# Testcase Example:  '"GGLLGG"'
#
# 在无限的平面上，机器人最初位于 (0, 0) 处，面朝北方。机器人可以接受下列三条指令之一：
# 
# 
# "G"：直走 1 个单位
# "L"：左转 90 度
# "R"：右转 90 度
# 
# 
# 机器人按顺序执行指令 instructions，并一直重复它们。
# 
# 只有在平面中存在环使得机器人永远无法离开时，返回 true。否则，返回 false。
# 
# 
# 
# 示例 1：
# 
# 输入："GGLLGG"
# 输出：true
# 解释：
# 机器人从 (0,0) 移动到 (0,2)，转 180 度，然后回到 (0,0)。
# 重复这些指令，机器人将保持在以原点为中心，2 为半径的环中进行移动。
# 
# 
# 示例 2：
# 
# 输入："GG"
# 输出：false
# 解释：
# 机器人无限向北移动。
# 
# 
# 示例 3：
# 
# 输入："GL"
# 输出：true
# 解释：
# 机器人按 (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ... 进行移动。
# 
# 
# 
# 提示：
# 
# 
# 1 <= instructions.length <= 100
# instructions[i] 在 {'G', 'L', 'R'} 中
# 
# 
#

"GLRLLGLL"


# @lc code=start
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        left_count = 0
        for instruction in instructions:
            if instruction == 'L':
                left_count += 1
            elif instruction == 'R':
                left_count -= 1
        return left_count % 4 != 0
# @lc code=end

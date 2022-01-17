#
# @lc app=leetcode.cn id=1610 lang=python3
#
# [1610] 可见点的最大数目
#
# https://leetcode-cn.com/problems/maximum-number-of-visible-points/description/
#
# algorithms
# Hard (27.38%)
# Likes:    51
# Dislikes: 0
# Total Accepted:    5.1K
# Total Submissions: 13.1K
# Testcase Example:  '[[2,1],[2,2],[3,3]]\n90\n[1,1]'
#
# 给你一个点数组 points 和一个表示角度的整数 angle ，你的位置是 location ，其中 location = [posx, posy] 且
# points[i] = [xi, yi] 都表示 X-Y 平面上的整数坐标。
# 
# 最开始，你面向东方进行观测。你 不能 进行移动改变位置，但可以通过 自转 调整观测角度。换句话说，posx 和 posy 不能改变。你的视野范围的角度用
# angle 表示， 这决定了你观测任意方向时可以多宽。设 d 为你逆时针自转旋转的度数，那么你的视野就是角度范围 [d - angle/2, d +
# angle/2] 所指示的那片区域。
# 
# Your browser does not support the video tag or this video format.
# 
# 对于每个点，如果由该点、你的位置以及从你的位置直接向东的方向形成的角度 位于你的视野中 ，那么你就可以看到它。
# 
# 同一个坐标上可以有多个点。你所在的位置也可能存在一些点，但不管你的怎么旋转，总是可以看到这些点。同时，点不会阻碍你看到其他点。
# 
# 返回你能看到的点的最大数目。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]
# 输出：3
# 解释：阴影区域代表你的视野。在你的视野中，所有的点都清晰可见，尽管 [2,2] 和 [3,3]在同一条直线上，你仍然可以看到 [3,3] 。
# 
# 示例 2：
# 
# 
# 输入：points = [[2,1],[2,2],[3,4],[1,1]], angle = 90, location = [1,1]
# 输出：4
# 解释：在你的视野中，所有的点都清晰可见，包括你所在位置的那个点。
# 
# 示例 3：
# 
# 
# 
# 
# 输入：points = [[1,0],[2,1]], angle = 13, location = [1,1]
# 输出：1
# 解释：如图所示，你只能看到两点之一。
# 
# 
# 
# 提示：
# 
# 
# 1 
# points[i].length == 2
# location.length == 2
# 0 
# 0 x, posy, xi, yi 
# 
# 
#

# @lc code=start
from math import degrees, atan


class Solution:
    @staticmethod
    def get_angle(p: list[int], o: list[int]):
        x, y = p[0] - o[0], p[1] - o[1]

        if x == 0:
            return 90 if y > 0 else 270

        base = degrees(atan(abs(y) / abs(x)))
        if x <= 0 and y <= 0:
            return 180 + base
        if x < 0 and y > 0:
            return 180 - base
        if x > 0 and y < 0:
            return 360 - base
        return base


    def visiblePoints(self, points: list[list[int]], angle: int, location: list[int]) -> int:
        must_seen = 0
        angle_of_points: list[int] = []

        for p in points:
            if p[0] == location[0] and p[1] == location[1]:
                must_seen += 1
            else:
                angle_of_points.append(Solution.get_angle(p, location))

        result = must_seen
        angle_of_points.sort()

        l = len(angle_of_points)
        for a in range(l):
            angle_of_points.append(angle_of_points[a] + 360)

        end = 0
        for begin in range(len(angle_of_points) // 2):
            while angle_of_points[begin] + angle >= angle_of_points[end + 1]:
                end += 1

            length = end - begin + 1
            result = max(result, length + must_seen)

        return result
# @lc code=end

s = Solution()
print(s.visiblePoints(points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]))
print(s.visiblePoints(points = [[2,1],[2,2],[3,4],[1,1]], angle = 90, location = [1,1]))
print(s.visiblePoints(points = [[1,0],[2,1]], angle = 13, location = [1,1]))
print(s.visiblePoints([[45,26],[82,12],[33,83],[58,50],[55,92],[66,42],[25,74],[74,74],[36,87],[7,41],[89,36],[44,22],[84,9],[96,90],[75,51],[87,15],[50,75],[90,84],[56,18],[43,48],[23,27],[100,34]], 12, [32,37])) # 4
print(s.visiblePoints([[70,66],[97,39],[79,45],[74,40],[27,31],[62,79],[77,13],[93,97],[67,1],[99,40],[12,50],[57,5],[87,15],[24,33],[44,98],[7,28],[40,94],[36,29],[51,28],[38,93],[54,88],[53,71],[98,99],[3,13],[90,38],[22,92],[30,10],[30,43],[54,50],[65,89],[57,23],[43,10],[47,2],[76,0],[90,95],[5,77],[9,49],[79,38],[77,68],[26,52],[97,1],[35,40],[60,76],[77,19],[21,33],[94,83],[64,29],[3,26],[36,83],[16,74],[17,94],[69,3],[95,98],[44,81],[65,99],[21,19],[99,91],[96,41],[48,0],[28,28],[70,93],[80,12],[15,40],[28,60],[42,19],[25,77],[34,57],[24,30],[83,40],[81,42],[80,76],[74,48],[66,66],[98,84],[48,52],[90,63],[6,29],[16,17],[64,93],[83,26],[93,2],[14,97],[87,38],[87,51],[14,23],[3,56],[48,3],[71,33],[63,70],[46,73],[97,23],[60,60],[98,56],[92,92],[73,38],[6,23],[70,82],[33,70],[29,71],[3,29],[61,31],[11,37],[91,8],[28,93],[21,18],[73,32],[21,36],[11,10],[79,85],[57,44],[19,47],[26,71],[58,73],[16,91],[1,10],[83,88],[36,65],[42,20],[21,57],[6,4],[68,44],[66,99],[51,77],[29,9],[78,6],[15,69],[86,63],[91,32],[65,23],[87,63],[55,61],[25,12],[4,96],[10,86],[72,74],[36,71],[56,70],[6,24],[13,52],[90,21],[60,18],[85,47],[11,36],[73,29],[21,9],[66,87],[92,98],[40,31],[45,81],[8,21],[33,71],[6,9],[31,29],[61,70],[86,18],[82,29],[68,94],[97,98],[53,50],[71,22],[71,4],[36,45],[38,28],[32,37],[52,49],[91,43],[79,79],[84,81],[64,47],[23,48],[72,49],[78,61],[34,48],[83,39],[32,36],[18,27],[91,72]], 86, [43,45])) # 67

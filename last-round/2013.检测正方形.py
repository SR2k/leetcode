#
# @lc app=leetcode.cn id=2013 lang=python3
#
# [2013] 检测正方形
#
# https://leetcode-cn.com/problems/detect-squares/description/
#
# algorithms
# Medium (32.62%)
# Likes:    5
# Dislikes: 0
# Total Accepted:    2.7K
# Total Submissions: 8.2K
# Testcase Example:  '["DetectSquares","add","add","add","count","count","add","count"]\n' +
#  '[[],[[3,10]],[[11,2]],[[3,2]],[[11,10]],[[14,8]],[[11,2]],[[11,10]]]'
#
# 给你一个在 X-Y 平面上的点构成的数据流。设计一个满足下述要求的算法：
# 
# 
# 添加 一个在数据流中的新点到某个数据结构中。可以添加 重复 的点，并会视作不同的点进行处理。
# 给你一个查询点，请你从数据结构中选出三个点，使这三个点和查询点一同构成一个 面积为正 的 轴对齐正方形 ，统计 满足该要求的方案数目。
# 
# 
# 轴对齐正方形 是一个正方形，除四条边长度相同外，还满足每条边都与 x-轴 或 y-轴 平行或垂直。
# 
# 实现 DetectSquares 类：
# 
# 
# DetectSquares() 使用空数据结构初始化对象
# void add(int[] point) 向数据结构添加一个新的点 point = [x, y]
# int count(int[] point) 统计按上述方式与点 point = [x, y] 共同构造 轴对齐正方形 的方案数。
# 
# 
# 
# 
# 示例：
# 
# 
# 输入：
# ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
# [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11,
# 10]]]
# 输出：
# [null, null, null, null, 1, 0, null, 2]
# 
# 解释：
# DetectSquares detectSquares = new DetectSquares();
# detectSquares.add([3, 10]);
# detectSquares.add([11, 2]);
# detectSquares.add([3, 2]);
# detectSquares.count([11, 10]); // 返回 1 。你可以选择：
# ⁠                              //   - 第一个，第二个，和第三个点
# detectSquares.count([14, 8]);  // 返回 0 。查询点无法与数据结构中的这些点构成正方形。
# detectSquares.add([11, 2]);    // 允许添加重复的点。
# detectSquares.count([11, 10]); // 返回 2 。你可以选择：
# ⁠                              //   - 第一个，第二个，和第三个点
# ⁠                              //   - 第一个，第三个，和第四个点
# 
# 
# 
# 
# 提示：
# 
# 
# point.length == 2
# 0 <= x, y <= 1000
# 调用 add 和 count 的 总次数 最多为 5000
# 
# 
#

# @lc code=start
from collections import defaultdict


class DetectSquares:
    def __init__(self):
        self.x: defaultdict[int, set[int]] = defaultdict(set)
        self.point_count: defaultdict[tuple[int, int], int] = defaultdict(int)


    def add(self, point: list[int]) -> None:
        x, y = point
        self.x[x].add(y)
        self.point_count[(x, y)] += 1


    def count(self, point: list[int]) -> int:
        p_x, p_y = point
        result = 0

        for y in self.x[p_x]:
            edge = abs(y - p_y)
            if edge == 0:
                continue
            # left
            result += self.point_count[(p_x, y)] * self.point_count[(p_x - edge, p_y)] * self.point_count[(p_x - edge, y)]
            # right
            result += self.point_count[(p_x, y)] * self.point_count[(p_x + edge, p_y)] * self.point_count[(p_x + edge, y)]

        return result

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
# @lc code=end

ds = DetectSquares()
cmd = ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
q = [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11,
10]]]

for i, c in enumerate(cmd):
    if c == 'DetectSquares':
        continue
    elif c == 'add':
        ds.add(q[i][0])
    else:
        print(ds.count(q[i][0]))

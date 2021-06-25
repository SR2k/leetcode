#
# @lc app=leetcode.cn id=149 lang=python3
#
# [149] 直线上最多的点数
#
# https://leetcode-cn.com/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (25.80%)
# Likes:    269
# Dislikes: 0
# Total Accepted:    27K
# Total Submissions: 98.6K
# Testcase Example:  '[[1,1],[2,2],[3,3]]'
#
# 给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：points = [[1,1],[2,2],[3,3]]
# 输出：3
# 
# 
# 示例 2：
# 
# 
# 输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# 输出：4
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# points[i].length == 2
# -10^4 i, yi 
# points 中的所有点 互不相同
# 
# 
#

# @lc code=start
INF = float('inf')

def get_line(a: list[int], b: list[int]) -> tuple[float, float, float]:
    # TODO: 小数精度问题
    x1, y1 = a if a[0] < b[0] else b
    x2, y2 = a if a[0] >= b[0] else b

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    cx = -C / A if A != 0 else INF
    cy = - C / B if B != 0 else INF
    k = -A / B if  B != 0 else INF

    return (cx, cy, k)

def b_find(ret: int, right: int) -> int:
    left = 0

    while left + 1 < right:
        middle = (left + right) // 2
        curr_ret = middle * (middle - 1) // 2

        if curr_ret == ret:
            return middle
        elif curr_ret > ret:
            right = middle
        else:
            left = middle

    if left * (left - 1) // 2 == ret:
        return left
    return right

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        count = len(points)
        if count <= 2: return count

        slope_freq: dict[tuple[float, float, float], int] = {}
        for i in range(count - 1):
            for j in range(i + 1, count):
                line = get_line(points[i], points[j])
                prev = slope_freq.get(line) or 0
                slope_freq[line] = prev + 1

        ret = max(slope_freq.values())
        # print(slope_freq)
        return b_find(ret, count)

# @lc code=end

# print(Solution().maxPoints([[7,3],[19,19],[-16,3],[13,17],[-18,1],[-18,-17],[13,-3],[3,7],[-11,12],[7,19],[19,-12],[20,-18],[-16,-15],[-10,-15],[-16,-18],[-14,-1],[18,10],[-13,8],[7,-5],[-4,-9],[-11,2],[-9,-9],[-5,-16],[10,14],[-3,4],[1,-20],[2,16],[0,14],[-14,5],[15,-11],[3,11],[11,-10],[-1,-7],[16,7],[1,-11],[-8,-3],[1,-6],[19,7],[3,6],[-1,-2],[7,-3],[-6,-8],[7,1],[-15,12],[-17,9],[19,-9],[1,0],[9,-10],[6,20],[-12,-4],[-16,-17],[14,3],[0,-1],[-18,9],[-15,15],[-3,-15],[-5,20],[15,-14],[9,-17],[10,-14],[-7,-11],[14,9],[1,-1],[15,12],[-5,-1],[-17,-5],[15,-2],[-12,11],[19,-18],[8,7],[-5,-3],[-17,-1],[-18,13],[15,-3],[4,18],[-14,-15],[15,8],[-18,-12],[-15,19],[-9,16],[-9,14],[-12,-14],[-2,-20],[-3,-13],[10,-7],[-2,-10],[9,10],[-1,7],[-17,-6],[-15,20],[5,-17],[6,-6],[-11,-8]]))
# print(Solution().maxPoints([[0,0],[1,-1],[1,1]]))

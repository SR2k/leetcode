#
# @lc app=leetcode.cn id=1101 lang=python3
#
# [1101] 彼此熟识的最早时间
#
# https://leetcode-cn.com/problems/the-earliest-moment-when-everyone-become-friends/description/
#
# algorithms
# Medium (66.76%)
# Likes:    17
# Dislikes: 0
# Total Accepted:    2.3K
# Total Submissions: 3.4K
# Testcase Example:  '[[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]]\n' +
#  '6'
#
# 在一个社交圈子当中，有 N 个人。每个人都有一个从 0 到 N-1 唯一的 id 编号。
# 
# 我们有一份日志列表 logs，其中每条记录都包含一个非负整数的时间戳，以及分属两个人的不同 id，logs[i] = [timestamp, id_A,
# id_B]。
# 
# 每条日志标识出两个人成为好友的时间，友谊是相互的：如果 A 和 B 是好友，那么 B 和 A 也是好友。
# 
# 如果 A 是 B 的好友，或者 A 是 B 的好友的好友，那么就可以认为 A 也与 B 熟识。
# 
# 返回圈子里所有人之间都熟识的最早时间。如果找不到最早时间，就返回 -1 。
# 
# 
# 
# 示例：
# 
# 输入：logs =
# [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]],
# N = 6
# 输出：20190301
# 解释：
# 第一次结交发生在 timestamp = 20190101，0 和 1 成为好友，社交朋友圈如下 [0,1], [2], [3], [4], [5]。
# 第二次结交发生在 timestamp = 20190104，3 和 4 成为好友，社交朋友圈如下 [0,1], [2], [3,4], [5].
# 第三次结交发生在 timestamp = 20190107，2 和 3 成为好友，社交朋友圈如下 [0,1], [2,3,4], [5].
# 第四次结交发生在 timestamp = 20190211，1 和 5 成为好友，社交朋友圈如下 [0,1,5], [2,3,4].
# 第五次结交发生在 timestamp = 20190224，2 和 4 已经是好友了。
# 第六次结交发生在 timestamp = 20190301，0 和 3 成为好友，大家都互相熟识了。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= N <= 100
# 1 <= logs.length <= 10^4
# 0 <= logs[i][0] <= 10^9
# 0 <= logs[i][1], logs[i][2] <= N - 1
# 保证 logs[i][0] 中的所有时间戳都不同
# Logs 不一定按某一标准排序
# logs[i][1] != logs[i][2]
# 
# 
#

# @lc code=start
def find_root(parents: list[int], n: int) -> int:
    while parents[n] != n:
        n = parents[n]
    return n


class Solution:
    def earliestAcq(self, logs: list[list[int]], n: int) -> int:
        if len(logs) < n - 1:
            return -1
        logs.sort(key=lambda x: x[0])

        parents = list(range(n))
        set_count = n

        for time, a, b in logs:
            root_a, root_b = find_root(parents, a), find_root(parents, b)
            if parents[root_a] == root_a and parents[root_a] != root_b:
                set_count -= 1
            parents[root_a] = root_b

            if set_count == 1:
                return time

        return -1
# @lc code=end

print(Solution().earliestAcq([[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], 6))

#
# @lc app=leetcode.cn id=1311 lang=python3
#
# [1311] 获取你好友已观看的视频
#
# https://leetcode-cn.com/problems/get-watched-videos-by-your-friends/description/
#
# algorithms
# Medium (38.28%)
# Likes:    34
# Dislikes: 0
# Total Accepted:    5.9K
# Total Submissions: 15.3K
# Testcase Example:  '[["A","B"],["C"],["B","C"],["D"]]\n[[1,2],[0,3],[0,3],[1,2]]\n0\n1'
#
# 有 n 个人，每个人都有一个  0 到 n-1 的唯一 id 。
# 
# 给你数组 watchedVideos  和 friends ，其中 watchedVideos[i]  和 friends[i] 分别表示 id = i
# 的人观看过的视频列表和他的好友列表。
# 
# Level 1 的视频包含所有你好友观看过的视频，level 2 的视频包含所有你好友的好友观看过的视频，以此类推。一般的，Level 为 k
# 的视频包含所有从你出发，最短距离为 k 的好友观看过的视频。
# 
# 给定你的 id  和一个 level 值，请你找出所有指定 level
# 的视频，并将它们按观看频率升序返回。如果有频率相同的视频，请将它们按字母顺序从小到大排列。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends =
# [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1
# 输出：["B","C"] 
# 解释：
# 你的 id 为 0（绿色），你的朋友包括（黄色）：
# id 为 1 -> watchedVideos = ["C"] 
# id 为 2 -> watchedVideos = ["B","C"] 
# 你朋友观看过视频的频率为：
# B -> 1 
# C -> 2
# 
# 
# 示例 2：
# 
# 
# 
# 输入：watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends =
# [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 2
# 输出：["D"]
# 解释：
# 你的 id 为 0（绿色），你朋友的朋友只有一个人，他的 id 为 3（黄色）。
# 
# 
# 
# 
# 提示：
# 
# 
# n == watchedVideos.length == friends.length
# 2 <= n <= 100
# 1 <= watchedVideos[i].length <= 100
# 1 <= watchedVideos[i][j].length <= 8
# 0 <= friends[i].length < n
# 0 <= friends[i][j] < n
# 0 <= id < n
# 1 <= level < n
# 如果 friends[i] 包含 j ，那么 friends[j] 包含 i
#


# @lc code=start
from collections import Counter, deque
from functools import cmp_to_key


class Solution:
    def watchedVideosByFriends(self, watchedVideos: list[list[str]], friends: list[list[int]], id: int, level: int) -> list[str]:
        queue, visited, prev_level = deque([id]), set([id]), None

        while level:
            curr_len = len(queue)
            level -= 1
            curr_level = []

            for _ in range(curr_len):
                curr = queue.popleft()

                for n in friends[curr]:
                    if n in visited:
                        continue
                    visited.add(n)
                    curr_level.append(n)
                    queue.append(n)

            prev_level = curr_level

        movies = Counter()
        for n in prev_level:
            for m in watchedVideos[n]:
                movies[m] += 1

        def cmp(a, b):
            if movies[a] != movies[b]:
                return movies[a] - movies[b]
            return 1 if a > b else -1

        return sorted(movies.keys(), key=cmp_to_key(cmp))
# @lc code=end

s = Solution()
print(s.watchedVideosByFriends(watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1))
print(s.watchedVideosByFriends([["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 2))

print(s.watchedVideosByFriends([["xk","qvgjjsp","sbphxzm"],["rwyvxl","ov"]], [[1],[0]], 0, 1)) # ["ov","rwyvxl"]

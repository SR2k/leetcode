#
# @lc app=leetcode.cn id=911 lang=python3
#
# [911] 在线选举
#
# https://leetcode-cn.com/problems/online-election/description/
#
# algorithms
# Medium (44.11%)
# Likes:    39
# Dislikes: 0
# Total Accepted:    3.6K
# Total Submissions: 8.2K
# Testcase Example:  '["TopVotedCandidate","q","q","q","q","q","q"]\n' +
#  '[[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]'
#
# 在选举中，第 i 张票是在时间为 times[i] 时投给 persons[i] 的。
# 
# 现在，我们想要实现下面的查询函数： TopVotedCandidate.q(int t) 将返回在 t 时刻主导选举的候选人的编号。
# 
# 在 t 时刻投出的选票也将被计入我们的查询之中。在平局的情况下，最近获得投票的候选人将会获胜。
# 
# 示例：
# 
# 输入：["TopVotedCandidate","q","q","q","q","q","q"],
# [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
# 输出：[null,0,1,1,0,0,1]
# 解释：
# 时间为 3，票数分布情况是 [0]，编号为 0 的候选人领先。
# 时间为 12，票数分布情况是 [0,1,1]，编号为 1 的候选人领先。
# 时间为 25，票数分布情况是 [0,1,1,0,0,1]，编号为 1 的候选人领先（因为最近的投票结果是平局）。
# 在时间 15、24 和 8 处继续执行 3 个查询。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= persons.length = times.length <= 5000
# 0 <= persons[i] <= persons.length
# times 是严格递增的数组，所有元素都在 [0, 10^9] 范围中。
# 每个测试用例最多调用 10000 次 TopVotedCandidate.q。
# TopVotedCandidate.q(int t) 被调用时总是满足 t >= times[0]。
# 
# 
#

# @lc code=start
from collections import defaultdict


class TopVotedCandidate:
    def __init__(self, persons: list[int], times: list[int]):
        curr_max = -1
        votes: defaultdict[int, int] = defaultdict(int)
        winners: list[int] = []

        for person in persons:
            votes[person] = votes[person] + 1

            if votes[person] >= votes[curr_max]:
                winners.append(person)
                curr_max = person
            else:
                winners.append(curr_max)

        self.winners = winners
        self.times = times

    def q(self, t: int) -> int:
        left, right = 0, len(self.times) - 1

        while left + 1 < right:
            middle = (left + right) // 2
            tm = self.times[middle]

            if tm == t:
                return self.winners[middle]
            elif tm > t:
                right = middle
            else:
                left = middle

        if self.times[right] <= t:
            return self.winners[right]
        return self.winners[left]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
# @lc code=end

o = ["TopVotedCandidate","q","q","q","q","q","q","q","q","q","q"]
p = [[[0,0,0,0,1],[0,6,39,52,75]],[45],[49],[59],[68],[42],[37],[99],[26],[78],[43]]
obj = None

for i, operation in enumerate(o):
    if operation == "TopVotedCandidate":
        obj = TopVotedCandidate(p[i][0], p[i][1])
    elif operation == "q":
        print("q", p[i], '-->', obj.q(p[i][0]))


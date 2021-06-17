#
# @lc app=leetcode.cn id=721 lang=python3
#
# [721] 账户合并
#
# https://leetcode-cn.com/problems/accounts-merge/description/
#
# algorithms
# Medium (46.91%)
# Likes:    268
# Dislikes: 0
# Total Accepted:    26.7K
# Total Submissions: 56.7K
# Testcase Example:  '[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]'
#
# 给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是 名称
# (name)，其余元素是 emails 表示该账户的邮箱地址。
# 
# 
# 现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。
# 
# 合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是按字符 ASCII 顺序排列的邮箱地址。账户本身可以以任意顺序返回。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John",
# "johnnybravo@mail.com"], ["John", "johnsmith@mail.com",
# "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# 输出：
# [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
# ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
# 解释：
# 第一个和第三个 John 是同一个人，因为他们有共同的邮箱地址 "johnsmith@mail.com"。 
# 第二个 John 和 Mary 是不同的人，因为他们的邮箱地址没有被其他帐户使用。
# 可以以任何顺序返回这些列表，例如答案 [['Mary'，'mary@mail.com']，['John'，'johnnybravo@mail.com']，
# ['John'，'john00@mail.com'，'john_newyork@mail.com'，'johnsmith@mail.com']]
# 也是正确的。
# 
# 
# 
# 
# 提示：
# 
# 
# accounts的长度将在[1，1000]的范围内。
# accounts[i]的长度将在[1，10]的范围内。
# accounts[i][j]的长度将在[1，30]的范围内。
# 
# 
#

# @lc code=start
class Solution:
    def __init__(self):
        self.sets: dict[str, int] = {}
        self.partents: dict[int, int] = {}
        self.lengths: dict[int, int] = {}

    def getRoot(self, i: int) -> int:
        while self.partents.get(i) != None:
            i = self.partents[i]
        return i

    def union(self, i1: str, i2: str) -> None:
        r1, r2 = self.getRoot(i1), self.getRoot(i2)
        if r1 == r2: return

        if self.lengths[r1] < self.lengths[r2]:
            self.lengths[r2] += self.lengths[r1]
            self.partents[r1] = r2
        else:
            self.lengths[r1] += self.lengths[r2]
            self.partents[r2] = r1

    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        ret = []

        for i in range(len(accounts)):
            account = accounts[i]

            if not i in self.lengths: self.lengths[i] = 1

            if len(account) == 1:
                ret.append(account)
                continue

            for j in range(1, len(account)):
                email = account[j]
                if email in self.sets:
                    self.union(self.sets[email], i)
                else:
                    self.sets[email] = i

        setToListMap: dict[int, list[str]] = {}
        emails = list(self.sets.keys())
        emails.sort()
        for email in emails:
            setIndex = self.getRoot(self.sets[email])
            if not setIndex in setToListMap:
                l = [accounts[setIndex][0]]
                setToListMap[setIndex] = l
                ret.append(l)
            setToListMap[setIndex].append(email)

        return ret

# @lc code=end

# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# print(Solution().accountsMerge(accounts))

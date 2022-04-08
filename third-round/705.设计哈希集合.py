#
# @lc app=leetcode.cn id=705 lang=python3
#
# [705] 设计哈希集合
#
# https://leetcode-cn.com/problems/design-hashset/description/
#
# algorithms
# Easy (63.98%)
# Likes:    220
# Dislikes: 0
# Total Accepted:    77.8K
# Total Submissions: 121.6K
# Testcase Example:  '["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]\n' +
# '[[],[1],[2],[1],[3],[2],[2],[2],[2]]'
#
# 不使用任何内建的哈希表库设计一个哈希集合（HashSet）。
# 
# 实现 MyHashSet 类：
# 
# 
# void add(key) 向哈希集合中插入值 key 。
# bool contains(key) 返回哈希集合中是否存在这个值 key 。
# void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。
# 
# 
# 
# 示例：
# 
# 
# 输入：
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains",
# "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# 输出：
# [null, null, null, true, false, null, true, null, false]
# 
# 解释：
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // 返回 True
# myHashSet.contains(3); // 返回 False ，（未找到）
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // 返回 True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // 返回 False ，（已移除）
# 
# 
# 
# 提示：
# 
# 
# 0 <= key <= 10^6
# 最多调用 10^4 次 add、remove 和 contains
# 
# 
#

# @lc code=start
class MyHashSet:
    def __init__(self):
        self.size = 769
        self.p = [[] for _ in range(self.size)]


    def add(self, key: int) -> None:
        hash = self.hash(key)
        if key not in self.p[hash]:
            self.p[hash].append(key)


    def remove(self, key: int) -> None:
        hash = self.hash(key)
        if key in self.p[hash]:
            self.p[hash].remove(key)


    def contains(self, key: int) -> bool:
        return key in self.p[self.hash(key)]


    def hash(self, k: int):
        return k % self.size

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end

#
# @lc app=leetcode.cn id=706 lang=python3
#
# [706] 设计哈希映射
#
# https://leetcode-cn.com/problems/design-hashmap/description/
#
# algorithms
# Easy (64.04%)
# Likes:    277
# Dislikes: 0
# Total Accepted:    69.9K
# Total Submissions: 109.2K
# Testcase Example:  '["MyHashMap","put","put","get","get","put","get","remove","get"]\n' +
#  '[[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]'
#
# 不使用任何内建的哈希表库设计一个哈希映射（HashMap）。
# 
# 实现 MyHashMap 类：
# 
# 
# MyHashMap() 用空映射初始化对象
# void put(int key, int value) 向 HashMap 插入一个键值对 (key, value) 。如果 key
# 已经存在于映射中，则更新其对应的值 value 。
# int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 -1 。
# void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。
# 
# 
# 
# 
# 示例：
# 
# 
# 输入：
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# 输出：
# [null, null, null, 1, -1, null, 1, null, -1]
# 
# 解释：
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // myHashMap 现在为 [[1,1]]
# myHashMap.put(2, 2); // myHashMap 现在为 [[1,1], [2,2]]
# myHashMap.get(1);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,2]]
# myHashMap.get(3);    // 返回 -1（未找到），myHashMap 现在为 [[1,1], [2,2]]
# myHashMap.put(2, 1); // myHashMap 现在为 [[1,1], [2,1]]（更新已有的值）
# myHashMap.get(2);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,1]]
# myHashMap.remove(2); // 删除键为 2 的数据，myHashMap 现在为 [[1,1]]
# myHashMap.get(2);    // 返回 -1（未找到），myHashMap 现在为 [[1,1]]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= key, value <= 10^6
# 最多调用 10^4 次 put、get 和 remove 方法
# 
# 
#

# @lc code=start
from collections import defaultdict


class Node:
    def __init__(self, key: int, val: int, next: 'Node' = None) -> None:
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:
    def __init__(self):
        self.size = 769
        self.store = [Node(-1, -1) for _ in range(self.size)]


    def put(self, key: int, value: int) -> None:
        self.remove(key)

        hash = key % self.size
        prev = self.store[hash]
        node = Node(key, value)

        while prev.next:
            prev = prev.next

        prev.next = node


    def _find(self, key: int):
        prev = None
        curr = self.store[key % self.size]

        while curr:
            if curr.key == key:
                return prev, curr

            prev, curr = curr, curr.next


    def get(self, key: int) -> int:
        find_result = self._find(key)
        if find_result:
            return find_result[1].val
        return -1


    def remove(self, key: int) -> None:
        find_result = self._find(key)
        if not find_result:
            return
        prev, node = find_result
        prev.next = node.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

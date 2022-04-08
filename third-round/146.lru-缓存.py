#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#
# https://leetcode-cn.com/problems/lru-cache/description/
#
# algorithms
# Medium (52.53%)
# Likes:    2017
# Dislikes: 0
# Total Accepted:    305.8K
# Total Submissions: 581.9K
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
# '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
# 
# 实现 LRUCache 类：
# 
# 
# 
# 
# LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组
# key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
# 
# 
# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
# 
# 
# 
# 
# 
# 示例：
# 
# 
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= capacity <= 3000
# 0 <= key <= 10000
# 0 <= value <= 10^5
# 最多调用 2 * 10^5 次 get 和 put
# 
# 
#

# @lc code=start
from typing import Optional


class CacheNode:
    def __init__(self, key = -1, value = -1, prev: Optional['CacheNode'] = None, next: Optional['CacheNode'] = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0

        self.head = CacheNode()
        self.tail = CacheNode()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.map: dict[int, CacheNode] = {}


    def _append(self, node: CacheNode):
        self.size += 1
        self.map[node.key] = node

        node.next = next = self.tail
        node.prev = prev = next.prev
        prev.next = next.prev = node


    def _delete(self, node: CacheNode):
        if node.key not in self.map:
            return

        self.size -= 1
        self.map.pop(node.key)

        prev = node.prev
        next = node.next
        node.prev = node.next = None
        prev.next = next
        next.prev = prev


    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]
        self._delete(node)
        self._append(node)

        return node.value


    def put(self, key: int, value: int) -> None:
        node = self.map[key] if key in self.map else CacheNode(key, value)
        node.value = value

        self._delete(node)
        self._append(node)

        if self.size > self.capacity:
            self._delete(self.head.next)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

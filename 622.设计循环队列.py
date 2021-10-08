#
# @lc app=leetcode.cn id=622 lang=python3
#
# [622] 设计循环队列
#
# https://leetcode-cn.com/problems/design-circular-queue/description/
#
# algorithms
# Medium (43.67%)
# Likes:    217
# Dislikes: 0
# Total Accepted:    65.2K
# Total Submissions: 149.3K
# Testcase Example:  '["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","Rear","isFull","deQueue","enQueue","Rear"]\n' +
#  '[[3],[1],[2],[3],[4],[],[],[],[4],[]]'
#
# 设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于
# FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。
# 
# 
# 循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。
# 
# 你的实现应该支持如下操作：
# 
# 
# MyCircularQueue(k): 构造器，设置队列长度为 k 。
# Front: 从队首获取元素。如果队列为空，返回 -1 。
# Rear: 获取队尾元素。如果队列为空，返回 -1 。
# enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
# deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
# isEmpty(): 检查循环队列是否为空。
# isFull(): 检查循环队列是否已满。
# 
# 
# 
# 
# 示例：
# 
# MyCircularQueue circularQueue = new MyCircularQueue(3); // 设置长度为 3
# circularQueue.enQueue(1);  // 返回 true
# circularQueue.enQueue(2);  // 返回 true
# circularQueue.enQueue(3);  // 返回 true
# circularQueue.enQueue(4);  // 返回 false，队列已满
# circularQueue.Rear();  // 返回 3
# circularQueue.isFull();  // 返回 true
# circularQueue.deQueue();  // 返回 true
# circularQueue.enQueue(4);  // 返回 true
# circularQueue.Rear();  // 返回 4
# 
# 
# 
# 提示：
# 
# 
# 所有的值都在 0 至 1000 的范围内；
# 操作数将在 1 至 1000 的范围内；
# 请不要使用内置的队列库。
# 
# 
#

# @lc code=start
class MyCircularQueue:
    def __init__(self, k: int):
        self.list = [-1 for i in range(k)]
        self.head = 0
        self.tail = 0
        self.insert_point = 0
        self.count = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.count == self.k:
            return False

        self.list[self.insert_point] = value
        self.count += 1
        self.tail = self.insert_point
        self.insert_point += 1
        self.insert_point %= self.k

        return True


    def deQueue(self) -> bool:
        if self.count == 0:
            return False

        self.list[self.head] = -1
        self.head += 1
        self.head %= self.k
        self.count -= 1

        return True


    def Front(self) -> int:
        if not self.count:
            return -1
        return self.list[self.head]


    def Rear(self) -> int:
        if not self.count:
            return -1
        return self.list[self.tail]


    def isEmpty(self) -> bool:
        return self.count == 0


    def isFull(self) -> bool:
        return self.count == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end

mcq = None
cmd = ["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","Rear","isFull","deQueue","enQueue","Rear"]
q = [[3],[1],[2],[3],[4],[],[],[],[4],[]]

for i, c in enumerate(cmd):
    a = q[i]
    if c == 'MyCircularQueue':
        mcq = MyCircularQueue(a[0])
    elif c == 'enQueue':
        print(mcq.enQueue(a[0]))
    elif c == 'deQueue':
        print(mcq.deQueue())
    elif c == 'Rear':
        print(mcq.Rear())
    elif c == 'Front':
        print(mcq.Front())
    elif c == 'isEmpty':
        print(mcq.isEmpty())
    elif c == 'isFull':
        print(mcq.isFull())


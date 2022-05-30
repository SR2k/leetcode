/*
 * @lc app=leetcode.cn id=155 lang=typescript
 *
 * [155] 最小栈
 *
 * https://leetcode.cn/problems/min-stack/description/
 *
 * algorithms
 * Easy (58.15%)
 * Likes:    1312
 * Dislikes: 0
 * Total Accepted:    383K
 * Total Submissions: 658.5K
 * Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n' +
  '[[],[-2],[0],[-3],[],[],[],[]]'
 *
 * 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
 *
 * 实现 MinStack 类:
 *
 *
 * MinStack() 初始化堆栈对象。
 * void push(int val) 将元素val推入堆栈。
 * void pop() 删除堆栈顶部的元素。
 * int top() 获取堆栈顶部的元素。
 * int getMin() 获取堆栈中的最小元素。
 *
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入：
 * ["MinStack","push","push","push","getMin","pop","top","getMin"]
 * [[],[-2],[0],[-3],[],[],[],[]]
 *
 * 输出：
 * [null,null,null,null,-3,null,0,-2]
 *
 * 解释：
 * MinStack minStack = new MinStack();
 * minStack.push(-2);
 * minStack.push(0);
 * minStack.push(-3);
 * minStack.getMin();   --> 返回 -3.
 * minStack.pop();
 * minStack.top();      --> 返回 0.
 * minStack.getMin();   --> 返回 -2.
 *
 *
 *
 *
 * 提示：
 *
 *
 * -2^31 <= val <= 2^31 - 1
 * pop、top 和 getMin 操作总是在 非空栈 上调用
 * push, pop, top, and getMin最多被调用 3 * 10^4 次
 *
 *
 */

export
// @lc code=start
class MinStack {
  private readonly min: number[] = []

  private readonly values: number[] = []

  push(val: number): void {
    this.values.push(val)
    this.min.push(this.min.length ? Math.min(this.min[this.min.length - 1], val) : val)
  }

  pop(): void {
    this.values.pop()
    this.min.pop()
  }

  top(): number {
    return this.values[this.values.length - 1]
  }

  getMin(): number {
    return this.min[this.min.length - 1]
  }
}
// @lc code=end

/*
 * @lc app=leetcode.cn id=155 lang=typescript
 *
 * [155] 最小栈
 *
 * https://leetcode-cn.com/problems/min-stack/description/
 *
 * algorithms
 * Easy (57.62%)
 * Likes:    1147
 * Dislikes: 0
 * Total Accepted:    323.7K
 * Total Submissions: 561.7K
 * Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n' +
  '[[],[-2],[0],[-3],[],[],[],[]]'
 *
 * 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
 *
 *
 * push(x) —— 将元素 x 推入栈中。
 * pop() —— 删除栈顶的元素。
 * top() —— 获取栈顶元素。
 * getMin() —— 检索栈中的最小元素。
 *
 *
 *
 *
 * 示例:
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
 * pop、top 和 getMin 操作总是在 非空栈 上调用。
 *
 *
 */

export
// @lc code=start
class MinStack {
  private readonly nums: number[] = []

  private readonly min: number[] = []

  push(val: number): void {
    this.nums.push(val)
    if (!this.min.length) {
      this.min.push(val)
    } else {
      const prevMin = this.min[this.min.length - 1]
      this.min.push(Math.min(prevMin, val))
    }
  }

  pop(): void {
    this.min.pop()
    this.nums.pop()
  }

  top(): number {
    return this.nums[this.nums.length - 1]
  }

  getMin(): number {
    return this.min[this.min.length - 1]
  }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
// @lc code=end

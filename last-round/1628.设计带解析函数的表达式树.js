/*
 * @lc app=leetcode.cn id=1628 lang=javascript
 *
 * [1628] 设计带解析函数的表达式树
 *
 * https://leetcode-cn.com/problems/design-an-expression-tree-with-evaluate-function/description/
 *
 * algorithms
 * Medium (86.11%)
 * Likes:    6
 * Dislikes: 0
 * Total Accepted:    285
 * Total Submissions: 333
 * Testcase Example:  '["3","4","+","2","*","7","/"]'
 *
 * 给定一个算术表达式的后缀表示法的标记（token） postfix ，构造并返回该表达式对应的二叉表达式树。
 * 
 * 后缀表示法是一种将操作数写在运算符之前的表示法。例如，表达式 4*(5-(2+7)) 的后缀表示法表示为数组 postfix =
 * ["4","5","7","2","+","-","*"] 。
 * 
 * 抽象类 Node 需要用于实现二叉表达式树。我们将通过 evaluate 函数来测试返回的树是否能够解析树中的值。你不可以移除 Node
 * 类，但你可以按需修改此类，也可以定义其他类来实现它。
 * 
 * 二叉表达式树是一种表达算术表达式的二叉树。二叉表达式树中的每一个节点都有零个或两个子节点。 叶节点（有 0 个子节点的节点）表示操作数，非叶节点（有 2
 * 个子节点的节点）表示运算符： '+' （加）、 '-' （减）、 '*' （乘）和 '/' （除）。
 * 
 * 我们保证任何子树对应值的绝对值不超过 10^9 ，且所有操作都是有效的（即没有除以零的操作）
 * 
 * 进阶： 你可以将表达式树设计得更模块化吗？例如，你的设计能够不修改现有的 evaluate 的实现就能支持更多的操作符吗？
 * 
 * 
 * 
 * 示例 1:
 * 
 * 
 * 
 * 输入： s = ["3","4","+","2","*","7","/"]
 * 输出： 2
 * 解释： 此表达式可解析为上述二叉树，其对应表达式为 ((3+4)*2)/7) = 14/7 = 2.
 * 
 * 
 * 示例 2:
 * 
 * 
 * 
 * 输入: s = ["4","5","7","2","+","-","*"]
 * 输出: -16
 * 解释: 此表达式可解析为上述二叉树，其对应表达式为 4*(5-(2+7)) = 4*(-4) = -16.
 * 
 * 
 * 示例 3:
 * 
 * 输入: s = ["4","2","+","3","5","1","-","*","+"]
 * 输出: 18
 * 
 * 
 * 示例 4:
 * 
 * 输入: s = ["100","200","+","2","/","5","*","7","+"]
 * 输出: 757
 * 
 * 
 * 
 * 
 * 提示:
 * 
 * 
 * 1 <= s.length < 100
 * s.length 是奇数。
 * s 包含数字和字符 '+' 、 '-' 、 '*' 以及 '/' 。
 * 如果 s[i] 是数，则对应的整数不超过 10^5 。
 * s 保证是一个有效的表达式。
 * 结果值和所有过程值的绝对值均不超过 10^9 。
 * 保证表达式不包含除以零的操作。
 * 
 * 
 */

// @lc code=start
/**
 * This is the interface for the expression tree Node.
 * You should not remove it, and you can define some classes to implement it.
 */

var Node = function () {
  if (this.constructor === Node) {
    throw new Error('Cannot instanciate abstract class');
  }
};

Node.prototype.evaluate = function () {
  throw new Error('Cannot call abstract method')
};

class TreeNode {
  constructor(val, left, right) {
    this.val = val
    this.left = left
    this.right = right
  }

  evaluate() {
    switch (this.val) {
      case '+':
        return this.left.evaluate() + this.right.evaluate()
      case '-':
        return this.left.evaluate() - this.right.evaluate()
      case '*':
        return this.left.evaluate() * this.right.evaluate()
      case '/':
        return this.left.evaluate() / this.right.evaluate()
      default:
        return +this.val
    }
  }
}

/**
 * This is the TreeBuilder class.
 * You can treat it as the driver code that takes the postinfix input 
 * and returns the expression tree represnting it as a Node.
 */
class TreeBuilder {
	/**
     * @param {string[]} s
     * @return {Node}
     */
	buildTree(postfix) {
    if (!postfix || !postfix.length) return null

    const stack = []

    for (const char of postfix) {
      if (TreeBuilder.isOperator(char)) {
        const right = stack.pop()
        const left = stack.pop()
        stack.push(new TreeNode(char, left, right))
        // console.log('char=' + char, '是操作符', 'left=', left && left.val, 'right=', right && right.val, 'stack=', stack.map(x => x.val))
      } else {
        stack.push(new TreeNode(char))
        // console.log('char=' + char, '不是操作符', 'stack=', stack.map(x => x.val))
      }
    }

    // console.log(JSON.stringify(stack[0], undefined, 2))
    return stack[0]
	}

  static isOperator(char) {
    return '+' === char || '-' === char || '*' === char || '/' === char
  }
}

// const obj = new TreeBuilder();
// obj.buildTree(["3","4","+","2","*","7","/"]);
// obj.buildTree(["4","5","7","2","+","-","*"]);

/**
 * Your TreeBuilder object will be instantiated and called as such:
 * var obj = new TreeBuilder();
 * var expTree = obj.buildTree(postfix);
 * var ans = expTree.evaluate();
 */
// @lc code=end


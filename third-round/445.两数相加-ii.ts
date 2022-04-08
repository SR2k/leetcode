/*
 * @lc app=leetcode.cn id=445 lang=typescript
 *
 * [445] 两数相加 II
 *
 * https://leetcode-cn.com/problems/add-two-numbers-ii/description/
 *
 * algorithms
 * Medium (58.88%)
 * Likes:    436
 * Dislikes: 0
 * Total Accepted:    83.6K
 * Total Submissions: 142K
 * Testcase Example:  '[7,2,4,3]\n[5,6,4]'
 *
 * 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
 *
 * 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
 *
 *
 *
 * 示例1：
 *
 *
 *
 *
 * 输入：l1 = [7,2,4,3], l2 = [5,6,4]
 * 输出：[7,8,0,7]
 *
 *
 * 示例2：
 *
 *
 * 输入：l1 = [2,4,3], l2 = [5,6,4]
 * 输出：[8,0,7]
 *
 *
 * 示例3：
 *
 *
 * 输入：l1 = [0], l2 = [0]
 * 输出：[0]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 链表的长度范围为 [1, 100]
 * 0
 * 输入数据保证链表代表的数字无前导 0
 *
 *
 *
 *
 * 进阶：如果输入链表不能修改该如何处理？换句话说，不能对列表中的节点进行翻转。
 *
 */

import { ListNode } from './commons/list'

export
// @lc code=start
function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
  const stack1 = list2Stack(l1)
  const stack2 = list2Stack(l2)
  let extra = 0
  let next: ListNode | null = null

  while (stack1.length || stack2.length || extra) {
    const n1 = stack1.length ? stack1.pop()!.val : 0
    const n2 = stack2.length ? stack2.pop()!.val : 0
    let val = n1 + n2 + extra

    extra = Math.floor(val / 10)
    val %= 10
    next = new ListNode(val, next)
  }

  return next
}

function list2Stack(head: ListNode | null): ListNode[] {
  const result: ListNode[] = []

  while (head) {
    result.push(head)
    head = head.next
  }

  return result
}
// @lc code=end

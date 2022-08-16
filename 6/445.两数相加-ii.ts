/*
 * @lc app=leetcode.cn id=445 lang=typescript
 *
 * [445] 两数相加 II
 *
 * https://leetcode.cn/problems/add-two-numbers-ii/description/
 *
 * algorithms
 * Medium (59.74%)
 * Likes:    528
 * Dislikes: 0
 * Total Accepted:    104.5K
 * Total Submissions: 174.8K
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
 * 0 <= node.val <= 9
 * 输入数据保证链表代表的数字无前导 0
 *
 *
 *
 *
 * 进阶：如果输入链表不能翻转该如何解决？
 *
 */

import { ListNode } from './commons/list'

export
// @lc code=start
function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
  return reverseList(add(reverseList(l1), reverseList(l2)))
}

function add(l1: ListNode | null, l2: ListNode | null) {
  if (!l1) return l2
  if (!l2) return l1

  const dummy = new ListNode(-1)
  let prev = dummy

  let carry = 0
  while (l1 || l2 || carry) {
    const v1 = l1?.val ?? 0
    const v2 = l2?.val ?? 0
    const value = v1 + v2 + carry
    carry = Math.floor(value / 10)

    const node = new ListNode(value % 10)
    prev.next = node
    prev = node

    l1 = l1?.next || null
    l2 = l2?.next || null
  }

  return dummy.next
}

function reverseList(head: ListNode | null) {
  let prev = null, curr = head
  while (curr) {
    const next = curr.next
    curr.next = prev
    prev = curr
    curr = next
  }
  return prev
}
// @lc code=end

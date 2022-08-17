/*
 * @lc app=leetcode.cn id=445 lang=typescript
 *
 * [445] 两数相加 II
 *
 * https://leetcode.cn/problems/add-two-numbers-ii/description/
 *
 * algorithms
 * Medium (60.02%)
 * Likes:    547
 * Dislikes: 0
 * Total Accepted:    108.7K
 * Total Submissions: 181K
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
  l1 = reverse(l1)
  l2 = reverse(l2)

  const dummy = new ListNode(-1)
  let prev = dummy
  let carry = 0

  while (l1 || l2 || carry) {
    const sum = (l1?.val ?? 0) + (l2?.val ?? 0) + carry
    l1 = l1?.next ?? null
    l2 = l2?.next ?? null
    const val = sum % 10
    const node = new ListNode(val)
    prev.next = node
    prev = node
    carry = Math.floor(sum / 10)
  }

  return reverse(dummy.next)
}

function reverse(list: ListNode | null) {
  let prev = null

  while (list) {
    const { next } = list
    list.next = prev
    prev = list
    list = next
  }

  return prev
}
// @lc code=end

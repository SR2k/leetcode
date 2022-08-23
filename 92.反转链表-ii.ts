/*
 * @lc app=leetcode.cn id=92 lang=typescript
 *
 * [92] 反转链表 II
 *
 * https://leetcode.cn/problems/reverse-linked-list-ii/description/
 *
 * algorithms
 * Medium (55.53%)
 * Likes:    1372
 * Dislikes: 0
 * Total Accepted:    330K
 * Total Submissions: 594.3K
 * Testcase Example:  '[1,2,3,4,5]\n2\n4'
 *
 * 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left  。请你反转从位置 left 到位置 right 的链表节点，返回
 * 反转后的链表 。
 *
 *
 * 示例 1：
 *
 *
 * 输入：head = [1,2,3,4,5], left = 2, right = 4
 * 输出：[1,4,3,2,5]
 *
 *
 * 示例 2：
 *
 *
 * 输入：head = [5], left = 1, right = 1
 * 输出：[5]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 链表中节点数目为 n
 * 1
 * -500
 * 1
 *
 *
 *
 *
 * 进阶： 你可以使用一趟扫描完成反转吗？
 *
 */

import { ListNode } from './commons/list'

export
// @lc code=start
function reverseBetween(head: ListNode | null, left: number, right: number): ListNode | null {
  const dummy = new ListNode(-1, head)
  const [tail, begin] = findAndCutFromN(dummy, left)

  let curr: ListNode | null = begin
  let prev = null
  for (let i = left; i <= right; i++) {
    const { next } = curr!
    curr!.next = prev
    prev = curr
    curr = next
  }

  tail.next = prev
  begin.next = curr
  return dummy.next
}

function findAndCutFromN(head: ListNode, n: number): [ListNode, ListNode] {
  for (let i = 0; i < n - 1; i++) {
    head = head.next
  }
  const result = head.next!
  head.next = null
  return [head, result]
}
// @lc code=end

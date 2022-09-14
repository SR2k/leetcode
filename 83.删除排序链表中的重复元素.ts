/*
 * @lc app=leetcode.cn id=83 lang=typescript
 *
 * [83] 删除排序链表中的重复元素
 *
 * https://leetcode.cn/problems/remove-duplicates-from-sorted-list/description/
 *
 * algorithms
 * Easy (53.46%)
 * Likes:    851
 * Dislikes: 0
 * Total Accepted:    486.1K
 * Total Submissions: 910.2K
 * Testcase Example:  '[1,1,2]'
 *
 * 给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：head = [1,1,2]
 * 输出：[1,2]
 *
 *
 * 示例 2：
 *
 *
 * 输入：head = [1,1,2,3,3]
 * 输出：[1,2,3]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 链表中节点数目在范围 [0, 300] 内
 * -100 <= Node.val <= 100
 * 题目数据保证链表已经按升序 排列
 *
 *
 */

import { ListNode } from './commons/list'

export
// @lc code=start
function deleteDuplicates(head: ListNode | null): ListNode | null {
  const dummy = new ListNode(Number.MAX_SAFE_INTEGER)
  let prev = dummy

  while (head) {
    if (head.val !== prev.val) {
      prev.next = head
      head = head.next
      prev = prev.next
      prev.next = null
    } else {
      head = head.next
    }
  }

  return dummy.next
}
// @lc code=end

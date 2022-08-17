/*
 * @lc app=leetcode.cn id=23 lang=typescript
 *
 * [23] 合并K个升序链表
 *
 * https://leetcode.cn/problems/merge-k-sorted-lists/description/
 *
 * algorithms
 * Hard (57.20%)
 * Likes:    2116
 * Dislikes: 0
 * Total Accepted:    524.9K
 * Total Submissions: 917.6K
 * Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
 *
 * 给你一个链表数组，每个链表都已经按升序排列。
 *
 * 请你将所有链表合并到一个升序链表中，返回合并后的链表。
 *
 *
 *
 * 示例 1：
 *
 * 输入：lists = [[1,4,5],[1,3,4],[2,6]]
 * 输出：[1,1,2,3,4,4,5,6]
 * 解释：链表数组如下：
 * [
 * ⁠ 1->4->5,
 * ⁠ 1->3->4,
 * ⁠ 2->6
 * ]
 * 将它们合并到一个有序链表中得到。
 * 1->1->2->3->4->4->5->6
 *
 *
 * 示例 2：
 *
 * 输入：lists = []
 * 输出：[]
 *
 *
 * 示例 3：
 *
 * 输入：lists = [[]]
 * 输出：[]
 *
 *
 *
 *
 * 提示：
 *
 *
 * k == lists.length
 * 0 <= k <= 10^4
 * 0 <= lists[i].length <= 500
 * -10^4 <= lists[i][j] <= 10^4
 * lists[i] 按 升序 排列
 * lists[i].length 的总和不超过 10^4
 *
 *
 */

import { ListNode } from './commons/list'

export
// @lc code=start
function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
  const result: Array<ListNode | null> = []

  for (let i = 0; i < lists.length; i += 2) {
    result.push(
      mergeTwo(lists[i], lists[i + 1]),
    )
  }

  if (result.length <= 1) {
    return result[0] || null
  }
  return mergeKLists(result)
}

function mergeTwo(l1?: ListNode | null, l2?: ListNode | null) {
  const dummy = new ListNode(-1)
  let prev = dummy

  while (l1 && l2) {
    let node
    if (l1.val <= l2.val) {
      node = l1
      l1 = l1.next
    } else {
      node = l2
      l2 = l2.next
    }

    prev.next = node
    prev = node
    prev.next = null
  }

  prev.next = l1 || l2 || null
  return dummy.next
}
// @lc code=end

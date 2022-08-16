/*
 * @lc app=leetcode.cn id=23 lang=typescript
 *
 * [23] 合并K个升序链表
 *
 * https://leetcode.cn/problems/merge-k-sorted-lists/description/
 *
 * algorithms
 * Hard (56.96%)
 * Likes:    2025
 * Dislikes: 0
 * Total Accepted:    489.5K
 * Total Submissions: 858.7K
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
  return merge(lists, 0, lists.length - 1)
}

function merge(lists: Array<ListNode | null>, left: number, right: number): ListNode | null {
  if (!lists?.length || left > right) return null
  if (left === right) return lists[left]
  const middle = Math.floor((left + right) / 2)
  return merge2Lists(merge(lists, left, middle), merge(lists, middle + 1, right))
}

function merge2Lists(list1?: ListNode | null, list2?: ListNode | null): ListNode | null {
  if (!list1) return list2 || null
  if (!list2) return list1 || null

  const dummy = new ListNode(-1)
  let prev = dummy

  while (list1 && list2) {
    if (list1.val <= list2.val) {
      prev.next = list1
      list1 = list1.next
    } else {
      prev.next = list2
      list2 = list2.next
    }
    prev = prev.next!
  }

  if (list1) prev.next = list1
  if (list2) prev.next = list2

  return dummy.next || null
}
// @lc code=end

// k/(2^i) * (2^i) * n
// k

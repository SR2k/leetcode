/*
 * @lc app=leetcode.cn id=148 lang=typescript
 *
 * [148] 排序链表
 *
 * https://leetcode.cn/problems/sort-list/description/
 *
 * algorithms
 * Medium (66.43%)
 * Likes:    1657
 * Dislikes: 0
 * Total Accepted:    308K
 * Total Submissions: 463.6K
 * Testcase Example:  '[4,2,1,3]'
 *
 * 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
 *
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：head = [4,2,1,3]
 * 输出：[1,2,3,4]
 *
 *
 * 示例 2：
 *
 *
 * 输入：head = [-1,5,3,4,0]
 * 输出：[-1,0,3,4,5]
 *
 *
 * 示例 3：
 *
 *
 * 输入：head = []
 * 输出：[]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 链表中节点的数目在范围 [0, 5 * 10^4] 内
 * -10^5 <= Node.val <= 10^5
 *
 *
 *
 *
 * 进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
 *
 */

import { ListNode } from './commons/list'

export
// @lc code=start
function sortList(head: NullableListNode): NullableListNode {
  let curr = head
  let listLength = 0
  while (curr) {
    curr = curr.next
    listLength++
  }

  const dummy = new ListNode(-1, head)

  for (let segLen = 1; segLen < listLength; segLen *= 2) {
    let prevEnd = dummy
    let nextBegin = dummy.next

    while (nextBegin) {
      const [seg1, seg2, next] = findAndCutSegment(nextBegin, segLen)
      const [mergedHead, mergedTail] = mergeList(seg1, seg2)

      prevEnd.next = mergedHead
      prevEnd = mergedTail!
      nextBegin = next
    }
  }

  return dummy.next
}

type NullableListNode = ListNode | null

function mergeList(l1: NullableListNode, l2: NullableListNode): [NullableListNode, NullableListNode] {
  const dummy = new ListNode(-1)
  let prev = dummy

  while (l1 || l2) {
    const v1 = l1?.val ?? Number.MAX_VALUE
    const v2 = l2?.val ?? Number.MAX_VALUE

    if (v1 <= v2) {
      prev.next = l1
      l1 = l1!.next
    } else {
      prev.next = l2
      l2 = l2!.next
    }

    prev = prev.next!
  }

  return [dummy.next, prev]
}

function findAndCutSegment(head: NullableListNode, k: number) {
  const result: Array<NullableListNode> = [head, null, null]
  let count = 0

  while (head) {
    const next = head.next
    count++

    if (count === k) {
      result[1] = next
      head.next = null
    } else if (count === 2 * k) {
      result[2] = next
      head.next = null
      break
    }

    head = next
  }

  return result
}
// @lc code=end

console.log(sortList(null)?.toString())
console.log(sortList(ListNode.fromArray([1]))?.toString())
console.log(sortList(ListNode.fromArray([2, 1]))?.toString())
console.log(sortList(ListNode.fromArray([2, 3, 1]))?.toString())
console.log(sortList(ListNode.fromArray([4, 2, 1, 3]))?.toString())

// 4 2 1 3

// 2 4 1 3

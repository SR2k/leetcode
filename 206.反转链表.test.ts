import { reverseList } from './206.反转链表'
import { ListNode } from './commons/list'

describe('reverseList', () => {
  it('works', () => {
    expect(reverseList(ListNode.fromArray([1, 2, 3]))?.toString())
      .toBe(ListNode.fromArray([3, 2, 1])?.toString())
    expect(reverseList(ListNode.fromArray([1]))?.toString())
      .toBe(ListNode.fromArray([1])?.toString())
    expect(reverseList(null))
      .toBeNull()
  })
})

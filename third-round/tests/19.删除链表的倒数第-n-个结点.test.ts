import { removeNthFromEnd } from '../19.删除链表的倒数第-n-个结点'
import { ListNode } from '../commons/list'

describe('19.删除链表的倒数第-n-个结点', () => {
  it('should work', () => {
    expect(removeNthFromEnd(ListNode.fromArray([1, 2, 3, 4, 5]), 2)?.toString())
      .toBe(ListNode.fromArray([1, 2, 3, 5])?.toString())
    expect(removeNthFromEnd(ListNode.fromArray([1, 2, 3, 4, 5]), 5)?.toString())
      .toBe(ListNode.fromArray([2, 3, 4, 5])?.toString())
    expect(removeNthFromEnd(ListNode.fromArray([1, 2, 3, 4, 5]), 1)?.toString())
      .toBe(ListNode.fromArray([1, 2, 3, 4])?.toString())
    expect(removeNthFromEnd(ListNode.fromArray([1]), 1))
      .toBe(null)
  })
})

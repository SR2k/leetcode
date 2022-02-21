import { reorderList } from '../143.重排链表'
import { ListNode } from '../commons/list'

describe('143.重排链表', () => {
  it('should work', () => {
    let list: ListNode

    list = ListNode.fromArray([1])!
    reorderList(list)
    expect(list.toString()).toBe(ListNode.fromArray([1])!.toString())

    list = ListNode.fromArray([1, 2])!
    reorderList(list)
    expect(list.toString()).toBe(ListNode.fromArray([1, 2])!.toString())

    list = ListNode.fromArray([1, 2, 3])!
    reorderList(list)
    expect(list.toString()).toBe(ListNode.fromArray([1, 3, 2])!.toString())

    list = ListNode.fromArray([1, 2, 3, 4])!
    reorderList(list)
    expect(list.toString()).toBe(ListNode.fromArray([1, 4, 2, 3])!.toString())

    list = ListNode.fromArray([1, 2, 3, 4, 5])!
    reorderList(list)
    expect(list.toString()).toBe(ListNode.fromArray([1, 5, 2, 4, 3])!.toString())
  })
})

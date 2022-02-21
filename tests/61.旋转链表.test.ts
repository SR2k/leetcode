import { rotateRight } from '../61.旋转链表'
import { ListNode } from '../commons/list'

describe('61.旋转链表', () => {
  it('should work', () => {
    expect(rotateRight(ListNode.fromArray([1, 2, 3, 4, 5]), 2)?.toString())
      .toBe(ListNode.fromArray([4, 5, 1, 2, 3])?.toString())
    expect(rotateRight(ListNode.fromArray([0, 1, 2]), 4)?.toString())
      .toBe(ListNode.fromArray([2, 0, 1])?.toString())
    expect(rotateRight(null, 4))
      .toBeNull()
  })
})

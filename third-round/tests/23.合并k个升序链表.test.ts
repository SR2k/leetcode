import { mergeKLists } from '../23.合并k个升序链表'
import { ListNode } from '../commons/list'

describe('23.合并k个升序链表', () => {
  it('should work', () => {
    let nodes: Array<ListNode | null>

    nodes = [[1, 4, 5], [1, 3, 4], [2, 6]].map((x) => ListNode.fromArray(x))
    mergeKLists(nodes)
    expect(nodes[0]?.toString())
      .toBe(ListNode.fromArray([1, 1, 2, 3, 4, 4, 5, 6])!.toString())

    nodes = []
    expect(() => mergeKLists(nodes)).not.toThrow()

    nodes = [null]
    expect(() => mergeKLists(nodes)).not.toThrow()
  })
})

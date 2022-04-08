import { copyRandomList, Node } from '../138.复制带随机指针的链表'

describe('copyRandomList', () => {
  it('works', () => {
    let s: Array<[number, number | null]>

    s = [[7, null], [13, 0], [11, 4], [10, 2], [1, 0]]
    expect(copyRandomList(Node.parse(s))?.serialize()).toStrictEqual(s)
    s = [[1, 1], [2, 1]]
    expect(copyRandomList(Node.parse(s))?.serialize()).toStrictEqual(s)
    s = [[3, null], [3, 0], [3, null]]
    expect(copyRandomList(Node.parse(s))?.serialize()).toStrictEqual(s)
  })
})

import { Node, connect } from './117.填充每个节点的下一个右侧节点指针-ii'
import { TreeNode } from './commons/Tree'

describe('117. Populating Next Right Pointers in Each Node II', () => {
  it('should work', () => {
    let node: TreeNode

    node = TreeNode.fromArray([1, 2, 3, 4, 5, null, 7]) as any
    connect(node as any)
    expect(Node.prototype.toString.call(node))
      .toStrictEqual([1, '#', 2, 3, '#', 4, 5, 7, '#'].join(','))

    node = TreeNode.fromArray([1, 2, 3, 4, 5, null, 6, 7, null, null, null, null, 8]) as any
    connect(node as any)
    expect(Node.prototype.toString.call(node))
      .toStrictEqual([1, '#', 2, 3, '#', 4, 5, 6, '#', 7, 8, '#'].join(','))

    expect(connect(null))
      .toBeNull()
  })
})

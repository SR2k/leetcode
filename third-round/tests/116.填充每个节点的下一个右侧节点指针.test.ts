import { TreeNode } from '../commons/Tree'
import { connect } from '../116.填充每个节点的下一个右侧节点指针'
import { Node } from '../117.填充每个节点的下一个右侧节点指针-ii'

describe('116. Populating Next Right Pointers in Each Node', () => {
  it('should work', () => {
    let tree

    tree = TreeNode.fromArray([1, 2, 3, 4, 5, 6, 7])
    expect(Node.prototype.toString.call(connect(tree as any)))
      .toBe([1, '#', 2, 3, '#', 4, 5, 6, 7, '#'].join(','))

    tree = TreeNode.fromArray([1, 2, 3])
    expect(Node.prototype.toString.call(connect(tree as any)))
      .toBe([1, '#', 2, 3, '#'].join(','))

    expect(connect(null))
      .toBeNull()
  })
})

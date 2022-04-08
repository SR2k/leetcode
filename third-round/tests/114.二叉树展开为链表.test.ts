import { flatten } from '../114.二叉树展开为链表'
import { serialize, TreeNode } from '../commons/Tree'

describe('114.二叉树展开为链表', () => {
  it('should work', () => {
    let tree: TreeNode | null

    tree = TreeNode.fromArray([1, null, 2, 3])
    flatten(tree)
    expect(serialize(tree)).toStrictEqual([1, null, 2, null, 3])

    tree = TreeNode.fromArray([1, 2, 5, 3, 4, null, 6])
    flatten(tree)
    expect(serialize(tree)).toStrictEqual([1, null, 2, null, 3, null, 4, null, 5, null, 6])

    tree = TreeNode.fromArray([])
    flatten(tree)
    expect(serialize(tree)).toStrictEqual([])

    tree = TreeNode.fromArray([0])
    flatten(tree)
    expect(serialize(tree)).toStrictEqual([0])
  })
})

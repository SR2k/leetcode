/* eslint-disable @typescript-eslint/naming-convention,no-underscore-dangle */
import { d, s } from '../297.二叉树的序列化与反序列化'
import { TreeNode } from '../commons/Tree'

describe('297.二叉树的序列化与反序列化', () => {
  it('should work', () => {
    let tree: TreeNode | null
    let _d: TreeNode | null
    let _s: string

    tree = TreeNode.fromArray([1, 2, 3, null, null, 4, 5])!
    _s = s(tree)
    _d = d(_s)
    expect(_d?.toString())
      .toBe(tree?.toString())

    tree = TreeNode.fromArray([])

    _s = s(tree)
    _d = d(_s)
    expect(_d?.toString())
      .toBe(tree?.toString())

    tree = TreeNode.fromArray([1])!

    _s = s(tree)
    _d = d(_s)
    expect(_d?.toString())
      .toBe(tree?.toString())

    tree = TreeNode.fromArray([1, 2])!

    _s = s(tree)
    _d = d(_s)
    expect(_d?.toString())
      .toBe(tree?.toString())
  })
})

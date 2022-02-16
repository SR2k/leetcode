import { TreeNode } from './commons/Tree'
import { lowestCommonAncestor } from './236.二叉树的最近公共祖先'

describe('236. Lowest Common Ancestor of a Binary Tree', () => {
  it('works', () => {
    let tree: TreeNode; let p: TreeNode; let
      q: TreeNode

    tree = TreeNode.fromArray([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4])!
    p = tree.left!
    q = tree.right!
    expect(lowestCommonAncestor(tree, p, q)).toBe(tree)

    tree = TreeNode.fromArray([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4])!
    p = tree.left!
    q = tree.left!.right!.right!
    expect(lowestCommonAncestor(tree, p, q)).toBe(p)
  })
})

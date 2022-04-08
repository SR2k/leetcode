import { } from '../235.二叉搜索树的最近公共祖先'
import { TreeNode } from '../commons/Tree'
import { lowestCommonAncestor } from '../236.二叉树的最近公共祖先'

describe('235.二叉搜索树的最近公共祖先', () => {
  it('should work', () => {
    let root: TreeNode, p: TreeNode, q: TreeNode, result: TreeNode

    root = TreeNode.fromArray([6, 2, 8, 0, 4, 7, 9, null, null, 3, 5])!
    p = root.left!
    q = root.right!
    result = root
    expect(lowestCommonAncestor(root, p, q)).toBe(result)

    root = TreeNode.fromArray([6, 2, 8, 0, 4, 7, 9, null, null, 3, 5])!
    p = root.left!
    q = root.left!.right!
    result = root.left!
    expect(lowestCommonAncestor(root, p, q)).toBe(result)
  })
})

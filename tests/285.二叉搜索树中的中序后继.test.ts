import { inorderSuccessor } from '../285.二叉搜索树中的中序后继'
import { TreeNode } from '../commons/Tree'

describe('285.二叉搜索树中的中序后继', () => {
  it('should work', () => {
    let root: TreeNode
    let node: TreeNode
    let result: TreeNode

    root = TreeNode.fromArray([41, 37, 44, 24, 39, 42, 48, 1, 35, 38, 40, null, 43, 46, 49, 0, 2, 30, 36, null, null, null, null, null, null, 45, 47, null, null, null, null, null, 4, 29, 32, null, null, null, null, null, null, 3, 9, 26, null, 31, 34, null, null, 7, 11, 25, 27, null, null, 33, null, 6, 8, 10, 16, null, null, null, 28, null, null, 5, null, null, null, null, null, 15, 19, null, null, null, null, 12, null, 18, 20, null, 13, 17, null, null, 22, null, 14, null, null, 21, 23])!
    node = root.left!.right!.right!
    result = root
    expect(inorderSuccessor(root, node)).toBe(result)

    root = TreeNode.fromArray([8, 5, 9, 3, 7])!
    node = root.left!.right!
    result = root
    expect(inorderSuccessor(root, node)).toBe(result)

    root = TreeNode.fromArray([2, 1, 3])!
    node = root.left!
    result = root
    expect(inorderSuccessor(root, node)).toBe(result)

    root = TreeNode.fromArray([5, 3, 6, 2, 4, null, null, 1])!
    node = root.right!
    expect(inorderSuccessor(root, node)).toBeNull()
  })
})

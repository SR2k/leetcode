import { deleteNode } from '../450.删除二叉搜索树中的节点'
import { TreeNode } from '../commons/Tree'
import { isValidBST } from '../98.验证二叉搜索树'
import { inorderTraversal } from '../94.二叉树的中序遍历'

describe('450.删除二叉搜索树中的节点', () => {
  it('should work', () => {
    let tree: TreeNode | null
    let result: TreeNode | null

    tree = TreeNode.fromArray([5, 3, 6, 2, 4, null, 7])
    result = deleteNode(tree, 3)
    expect(inorderTraversal(result))
      .toStrictEqual([2, 4, 5, 6, 7])
    expect(isValidBST(result!))
      .toBeTruthy()

    tree = TreeNode.fromArray([5, 3, 6, 2, 4, null, 7])
    result = deleteNode(tree, 5)
    expect(inorderTraversal(result))
      .toStrictEqual([2, 3, 4, 6, 7])
    expect(isValidBST(result!))
      .toBeTruthy()

    tree = TreeNode.fromArray([5, 3, 6, 2, 4, null, 7])
    result = deleteNode(tree, 0)
    expect(inorderTraversal(result))
      .toStrictEqual([2, 3, 4, 5, 6, 7])
    expect(isValidBST(result!))
      .toBeTruthy()

    expect(deleteNode(null, 0)).toBe(null)
    expect(deleteNode(TreeNode.fromArray([0]), 0)).toBe(null)
  })
})

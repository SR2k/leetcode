import { isValidBST } from './98.验证二叉搜索树'
import { TreeNode } from './commons/Tree'

describe('98. Validate Binary Search Tree', () => {
  it('should work', () => {
    expect(isValidBST(TreeNode.fromArray([5, 1, 4, null, null, 3, 6])!))
      .toBe(false)
    expect(isValidBST(TreeNode.fromArray([2, 1, 3])!))
      .toBe(true)
    expect(isValidBST(TreeNode.fromArray([3, 2, 5, 1, null, 4, 7])!))
      .toBe(true)
    expect(isValidBST(TreeNode.fromArray([3, 2, 5, 1, null, 9, 7])!))
      .toBe(false)
  })
})

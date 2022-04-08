import { buildTree } from '../105.从前序与中序遍历序列构造二叉树'
import { TreeNode } from '../commons/Tree'

describe('105.从前序与中序遍历序列构造二叉树', () => {
  it('should work', () => {
    expect(buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])?.toString())
      .toBe(TreeNode.fromArray([3, 9, 20, null, null, 15, 7])?.toString())
    expect(buildTree([-1], [-1])?.toString())
      .toBe(TreeNode.fromArray([-1])?.toString())
  })
})

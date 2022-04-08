import { isSymmetric } from '../101.对称二叉树'
import { TreeNode } from '../commons/Tree'

describe('101.对称二叉树', () => {
  it('should work', () => {
    expect(isSymmetric(TreeNode.fromArray([1, 2, 2, 3, 4, 4, 3])))
      .toBe(true)
    expect(isSymmetric(TreeNode.fromArray([1, 2, 2, null, 3, null, 3])))
      .toBe(false)
  })
})

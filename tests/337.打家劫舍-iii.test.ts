import { rob } from '../337.打家劫舍-iii'
import { TreeNode } from '../commons/Tree'

describe('337.打家劫舍-iii', () => {
  it('should work', () => {
    expect(rob(TreeNode.fromArray([3, 2, 3, null, 3, null, 1]))).toBe(7)
    expect(rob(TreeNode.fromArray([3, 4, 5, 1, 3, null, 1]))).toBe(9)
  })
})

/*

     3
    / \
   2   3
    \   \
     3   1

 */

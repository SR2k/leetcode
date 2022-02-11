import { goodNodes, goodNodesIteration } from './1448.统计二叉树中好节点的数目'
import { TreeNode } from './commons/Tree'

describe('Count Good Nodes in Binary Tree', () => {
  it('works', () => {
    expect(goodNodes(TreeNode.fromArray([3, 1, 4, 3, null, 1, 5])!)).toBe(4)
    expect(goodNodes(TreeNode.fromArray([3, 3, null, 4, 2])!)).toBe(3)
    expect(goodNodes(TreeNode.fromArray([1])!)).toBe(1)
  })

  test('iteration works', () => {
    expect(goodNodesIteration(TreeNode.fromArray([3, 1, 4, 3, null, 1, 5])!)).toBe(4)
    expect(goodNodesIteration(TreeNode.fromArray([3, 3, null, 4, 2])!)).toBe(3)
    expect(goodNodesIteration(TreeNode.fromArray([1])!)).toBe(1)
  })
})

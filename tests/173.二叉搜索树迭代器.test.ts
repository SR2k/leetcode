import { BSTIterator } from '../173.二叉搜索树迭代器'
import { TreeNode } from '../commons/Tree'

describe('173.二叉搜索树迭代器', () => {
  it('should work', () => {
    const bSTIterator = new BSTIterator(TreeNode.fromArray([7, 3, 15, null, null, 9, 20]))

    expect(bSTIterator.next()).toBe(3)
    expect(bSTIterator.next()).toBe(7)
    expect(bSTIterator.hasNext()).toBe(true)
    expect(bSTIterator.next()).toBe(9)
    expect(bSTIterator.hasNext()).toBe(true)
    expect(bSTIterator.next()).toBe(15)
    expect(bSTIterator.hasNext()).toBe(true)
    expect(bSTIterator.next()).toBe(20)
    expect(bSTIterator.hasNext()).toBe(false)
  })
})

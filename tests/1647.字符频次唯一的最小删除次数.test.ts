import { minDeletions } from '../1647.字符频次唯一的最小删除次数'

describe('1647.字符频次唯一的最小删除次数', () => {
  it('should work', () => {
    // expect(minDeletions('aab')).toBe(0)
    // expect(minDeletions('aaabbbcc')).toBe(2)
    // expect(minDeletions('ceabaacb')).toBe(2)
    expect(minDeletions('aaabbbcccdddeeefff')).toBe(12)
  })
})

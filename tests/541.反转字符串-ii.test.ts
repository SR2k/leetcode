import { reverseStr } from '../541.反转字符串-ii'

describe('541.反转字符串-ii', () => {
  it('should work', () => {
    expect(reverseStr('abcdefg', 2)).toBe('bacdfeg')
    expect(reverseStr('abcd', 2)).toBe('bacd')
  })
})

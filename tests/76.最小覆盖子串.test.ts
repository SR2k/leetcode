import { minWindow } from '../76.最小覆盖子串'

describe('76.最小覆盖子串', () => {
  it('should work', () => {
    expect(minWindow('ADOBECODEBANC', 'ABC')).toBe('BANC')
    expect(minWindow('a', 'a')).toBe('a')
    expect(minWindow('a', 'aa')).toBe('')
    expect(minWindow('ab', 'a')).toBe('a')
    expect(minWindow('ab', 'b')).toBe('b')
  })
})

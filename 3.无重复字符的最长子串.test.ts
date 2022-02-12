import { lengthOfLongestSubstring } from './3.无重复字符的最长子串'

describe('lengthOfLongestSubstring', () => {
  it('works', () => {
    expect(lengthOfLongestSubstring('abcabababababa')).toBe(3)
    expect(lengthOfLongestSubstring('a')).toBe(1)
    expect(lengthOfLongestSubstring('')).toBe(0)
    expect(lengthOfLongestSubstring('ababababababababaabc')).toBe(3)
    expect(lengthOfLongestSubstring('abcabcbb')).toBe(3)
    expect(lengthOfLongestSubstring('bbbbb')).toBe(1)
    expect(lengthOfLongestSubstring('pwwkew')).toBe(3)
  })
})

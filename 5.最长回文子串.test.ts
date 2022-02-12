import { longestPalindrome } from './5.最长回文子串'

describe('longestPalindrome', () => {
  it('works when longest length is odd', () => {
    expect(longestPalindrome('abcaccddd')).toBe('cac')
    expect(longestPalindrome('abcdefg')).toBe('a')
  })

  it('works when longest length is even', () => {
    expect(longestPalindrome('abcaaccddd')).toBe('caac')
    expect(longestPalindrome('abcdeefg')).toBe('ee')
  })

  it('works for leetcode test cases', () => {
    expect(longestPalindrome('babad')).toBe('bab')
    expect(longestPalindrome('cbbd')).toBe('bb')
    expect(longestPalindrome('a')).toBe('a')
    expect(longestPalindrome('ac')).toBe('a')
  })
})

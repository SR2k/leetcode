import { isPalindrome } from '../9.回文数'

describe('9.回文数', () => {
  it('should work', () => {
    expect(isPalindrome(121)).toBe(true)
    expect(isPalindrome(-121)).toBe(false)
    expect(isPalindrome(100000)).toBe(false)
    expect(isPalindrome(99899)).toBe(true)
    expect(isPalindrome(100001)).toBe(true)
  })
})

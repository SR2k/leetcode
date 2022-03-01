import { isPalindrome } from '../125.验证回文串'

describe('125.验证回文串', () => {
  it('should work', () => {
    expect(isPalindrome('A man, a plan, a canal: Panama'))
      .toBe(true)
    expect(isPalindrome('race a car'))
      .toBe(false)
    expect(isPalindrome('aaaa'))
      .toBe(true)
    expect(isPalindrome('a'))
      .toBe(true)
    expect(isPalindrome('     a '))
      .toBe(true)
  })
})

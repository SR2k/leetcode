import { isMatch } from '../10.正则表达式匹配'

describe('10.正则表达式匹配', () => {
  it('should work', () => {
    expect(isMatch('aa', 'a'))
      .toBe(false)
    expect(isMatch('aa', 'a*'))
      .toBe(true)
    expect(isMatch('ab', '.*'))
      .toBe(true)
    expect(isMatch('aaaaabaaaa', 'a*'))
      .toBe(false)
    expect(isMatch('aavaaaaaaaa', 'a..a*'))
      .toBe(true)
    expect(isMatch('', 'a*.*a*b*'))
      .toBe(true)
    expect(isMatch('ab', '.*'))
      .toBe(true)
  })
})

import { isMatch } from '../44.通配符匹配'

describe('44.通配符匹配', () => {
  it('should work', () => {
    expect(isMatch('aa', 'a')).toBe(false)
    expect(isMatch('aa', '*')).toBe(true)
    expect(isMatch('cb', '?a')).toBe(false)

    expect(isMatch('adceb', '*a*b')).toBe(true)
    expect(isMatch('acdcb', 'a*c?b')).toBe(false)
    expect(isMatch('', 'a*c?b')).toBe(false)
    expect(isMatch('', '**')).toBe(true)
  })
})

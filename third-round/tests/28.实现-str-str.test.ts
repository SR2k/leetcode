import { strStr } from '../28.实现-str-str'

describe('28.实现-str-str', () => {
  it('should work', () => {
    expect(strStr('ababaabbbbababbaabaaabaabbaaaabbabaabbbbbbabbaabbabbbabbbbbaaabaababbbaabbbabbbaabbbbaaabbababbabbbabaaabbaabbabababbbaaaaaaababbabaababaabbbbaaabbbabb', 'abbabbbabaa'))
      .toBe(92)
    expect(strStr('mississippi', 'issip'))
      .toBe(4)
    expect(strStr('hello', 'll'))
      .toBe(2)
    expect(strStr('aaaaa', 'bba'))
      .toBe(-1)
    expect(strStr('', ''))
      .toBe(0)
  })
})

import { removeDuplicateLetters } from '../316.去除重复字母'

describe('316.去除重复字母', () => {
  it('should work', () => {
    expect(removeDuplicateLetters('bcabc'))
      .toBe('abc')
    expect(removeDuplicateLetters('cbacdcbc'))
      .toBe('acdb')
  })
})

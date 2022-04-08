import { wordBreak } from '../139.单词拆分'

describe('139.单词拆分', () => {
  it('should work', () => {
    expect(wordBreak('leetcode', ['leet', 'code'])).toBe(true)
    expect(wordBreak('applepenapple', ['apple', 'pen'])).toBe(true)
    expect(wordBreak('catsandog', ['cats', 'dog', 'sand', 'and', 'cat'])).toBe(false)
  })
})

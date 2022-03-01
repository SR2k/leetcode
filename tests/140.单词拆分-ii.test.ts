import { wordBreak } from '../140.单词拆分-ii'

describe('140.单词拆分-ii', () => {
  it('should work', () => {
    expect(wordBreak('catsanddog', ['cat', 'cats', 'and', 'sand', 'dog']).sort())
      .toStrictEqual(['cats and dog', 'cat sand dog'].sort())

    expect(wordBreak('pineapplepenapple', ['apple', 'pen', 'applepen', 'pine', 'pineapple']).sort())
      .toStrictEqual(['pine apple pen apple', 'pineapple pen apple', 'pine applepen apple'].sort())

    expect(wordBreak('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']))
      .toStrictEqual([])
  })
})

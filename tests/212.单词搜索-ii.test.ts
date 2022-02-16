import { findWords } from '../212.单词搜索-ii'

describe('212. Word Search II', () => {
  test('it works', () => {
    expect(
      findWords(
        [['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'], ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']],
        ['oath', 'pea', 'eat', 'rain'],
      ).sort(),
    ).toStrictEqual(['eat', 'oath'].sort())

    expect(findWords([['a', 'b'], ['c', 'd']], ['abcb']))
      .toStrictEqual([])
  })
})

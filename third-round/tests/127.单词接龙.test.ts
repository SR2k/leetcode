import { ladderLength } from '../127.单词接龙'

describe('127.单词接龙', () => {
  it('should work', () => {
    expect(ladderLength('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
      .toBe(5)
    expect(ladderLength('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']))
      .toBe(0)
  })
})

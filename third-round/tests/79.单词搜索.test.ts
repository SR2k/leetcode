import { exist } from '../79.单词搜索'

describe('79. Word Search', () => {
  it('should work', () => {
    expect(exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCCED'))
      .toBe(true)
    expect(exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'SEE'))
      .toBe(true)
    expect(exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCB'))
      .toBe(false)
  })
})

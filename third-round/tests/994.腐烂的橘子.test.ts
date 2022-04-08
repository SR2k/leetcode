import { orangesRotting } from '../994.腐烂的橘子'

describe('994.腐烂的橘子', () => {
  it('should work', () => {
    expect(orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
      .toBe(4)

    expect(orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
      .toBe(-1)

    expect(orangesRotting([[2, 2, 2], [0, 2, 2], [2, 0, 2]]))
      .toBe(0)

    expect(orangesRotting([[0]]))
      .toBe(0)

    expect(orangesRotting([[0, 2]])).toBe(0)
  })
})

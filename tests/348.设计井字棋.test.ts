import { TicTacToe } from '../348.设计井字棋'

describe('348.设计井字棋', () => {
  it('should work', () => {
    const toe = new TicTacToe(3)
    expect(toe.move(0, 0, 1)).toBe(0)
    expect(toe.move(0, 2, 2)).toBe(0)
    expect(toe.move(2, 2, 1)).toBe(0)
    expect(toe.move(1, 1, 2)).toBe(0)
    expect(toe.move(2, 0, 1)).toBe(0)
    expect(toe.move(1, 0, 2)).toBe(0)
    expect(toe.move(2, 1, 1)).toBe(1)
  })
})

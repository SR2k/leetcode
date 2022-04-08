import { calculate } from '../227.基本计算器-ii'

describe('227.基本计算器-ii', () => {
  it('should work', () => {
    expect(calculate('3+2*2')).toBe(7)
    expect(calculate("14-3/2")).toBe(13)
    expect(calculate(' 3/2 ')).toBe(1)
    expect(calculate(' 3+5 / 2 ')).toBe(5)
  })
})

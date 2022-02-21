import { arraySign } from '../1822.数组元素积的符号'

describe('1822.数组元素积的符号', () => {
  it('should work', () => {
    expect(arraySign([-1, -2, -3, -4, 3, 2, 1])).toBe(1)
    expect(arraySign([1, 5, 0, 2, -3])).toBe(0)
    expect(arraySign([-1, 1, -1, 1, -1])).toBe(-1)
  })
})

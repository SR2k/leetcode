import { removeKdigits } from '../402.移掉-k-位数字'

describe('402.移掉-k-位数字', () => {
  it('should work', () => {
    expect(removeKdigits('1432219', 3))
      .toBe('1219')
    expect(removeKdigits('10200', 1))
      .toBe('200')
    expect(removeKdigits('10', 2))
      .toBe('0')
  })
})

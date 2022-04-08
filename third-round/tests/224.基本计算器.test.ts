/* eslint-disable no-eval */
import { calculate } from '../224.基本计算器'

describe('224.基本计算器', () => {
  it('should work', () => {
    let q: string

    q = '1 + 1'
    expect(calculate(q)).toBe(eval(q))

    q = ' 2-1 + 2 '
    expect(calculate(q)).toBe(eval(q))

    q = '(1+(4+5+2)-3)+(6+8)'
    expect(calculate(q)).toBe(eval(q))

    q = '-(1+(4+5+2)-3)+(6+8)'
    expect(calculate(q)).toBe(eval(q))

    q = '-(1-(4+5+2)-3)+(6+8)'
    expect(calculate(q)).toBe(eval(q))

    q = '-(2 + 3)'
    expect(calculate(q)).toBe(eval(q))
  })
})

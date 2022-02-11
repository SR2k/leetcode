import { isValid } from './20.有效的括号'

describe('validateParentheses', () => {
  it('works', () => {
    expect(isValid("()")).toBe(true)
    expect(isValid("()[]{}")).toBe(true)
    expect(isValid("(]")).toBe(false)
    expect(isValid("([)]")).toBe(false)
    expect(isValid("{[]}")).toBe(true)
    expect(isValid("{")).toBe(false)
    expect(isValid("}")).toBe(false)
  })
})

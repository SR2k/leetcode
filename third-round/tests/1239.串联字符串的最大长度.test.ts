import { maxLength } from '../1239.串联字符串的最大长度'

describe('1239.串联字符串的最大长度', () => {
  it('should work', () => {
    expect(maxLength(['un', 'iq', 'ue'])).toBe(4)
    expect(maxLength(['cha', 'r', 'act', 'ers'])).toBe(6)
    expect(maxLength(['abcdefghijklmnopqrstuvwxyz'])).toBe(26)
  })
})

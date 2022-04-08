import { decodeString } from '../394.字符串解码'

describe('394.字符串解码', () => {
  it('should work', () => {
    expect(decodeString('3[z]2[2[y]pq4[2[jk]e1[f]]]ef'))
      .toBe('zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef')

    expect(decodeString('3[a]2[bc]'))
      .toBe('aaabcbc')
    expect(decodeString('3[a2[c]]'))
      .toBe('accaccacc')
    expect(decodeString('3[a2[c10[dd]]]'))
      .toBe('acddddddddddddddddddddcddddddddddddddddddddacddddddddddddddddddddcddddddddddddddddddddacddddddddddddddddddddcdddddddddddddddddddd')
    expect(decodeString('2[abc]3[cd]ef'))
      .toBe('abcabccdcdcdef')
  })
})

import { reverseWords } from '../151.翻转字符串里的单词'

describe('', () => {
  it('works', () => {
    expect(reverseWords('the sky is blue')).toBe('blue is sky the')
    expect(reverseWords('  hello world  ')).toBe('world hello')
    expect(reverseWords('    a       ')).toBe('a')
    expect(reverseWords('    a')).toBe('a')
    expect(reverseWords('a    ')).toBe('a')
    expect(reverseWords('    a       good   example')).toBe('example good a')
    expect(reverseWords('  Bob    Loves  Alice   ')).toBe('Alice Loves Bob')
    expect(reverseWords('  Bob    Loves  Alice')).toBe('Alice Loves Bob')
    expect(reverseWords('Bob    Loves  Alice')).toBe('Alice Loves Bob')
    expect(reverseWords('Alice does not even like bob')).toBe('bob like even not does Alice')
  })
})

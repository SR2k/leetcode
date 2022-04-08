import { Trie } from '../208.实现-trie-前缀树'

describe('208.实现-trie-前缀树', () => {
  it('should work', () => {
    const trie = new Trie()
    trie.insert('apple')
    expect(trie.search('apple')).toBe(true)
    expect(trie.search('app')).toBe(false)
    expect(trie.startsWith('app')).toBe(true)
    expect(trie.search('app')).toBe(false)
    trie.insert('app')
    expect(trie.search('app')).toBe(true)
  })
})

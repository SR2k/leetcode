/*
 * @lc app=leetcode.cn id=208 lang=typescript
 *
 * [208] 实现 Trie (前缀树)
 *
 * https://leetcode.cn/problems/implement-trie-prefix-tree/description/
 *
 * algorithms
 * Medium (72.00%)
 * Likes:    1263
 * Dislikes: 0
 * Total Accepted:    221.4K
 * Total Submissions: 307.6K
 * Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n' +
  '[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
 *
 * Trie（发音类似 "try"）或者说 前缀树
 * 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。
 *
 * 请你实现 Trie 类：
 *
 *
 * Trie() 初始化前缀树对象。
 * void insert(String word) 向前缀树中插入字符串 word 。
 * boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回
 * false 。
 * boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true
 * ；否则，返回 false 。
 *
 *
 *
 *
 * 示例：
 *
 *
 * 输入
 * ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
 * [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
 * 输出
 * [null, null, true, false, true, null, true]
 *
 * 解释
 * Trie trie = new Trie();
 * trie.insert("apple");
 * trie.search("apple");   // 返回 True
 * trie.search("app");     // 返回 False
 * trie.startsWith("app"); // 返回 True
 * trie.insert("app");
 * trie.search("app");     // 返回 True
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1
 * word 和 prefix 仅由小写英文字母组成
 * insert、search 和 startsWith 调用次数 总计 不超过 3 * 10^4 次
 *
 *
 */

export
// @lc code=start
class Trie {
  private readonly root: TrieNode = {}

  insert(word: string): void {
    this.get(word, true)
  }

  search(word: string): boolean {
    const n = this.get(word, false)
    return !!(n?.ending)
  }

  startsWith(prefix: string): boolean {
    const n = this.get(prefix, false)
    return !!n
  }

  private get(word: string, isInsert: boolean) {
    let curr = this.root
    for (const char of word) {
      if (!curr[char]) {
        if (!isInsert) {
          return undefined
        } else {
          curr[char] = {}
        }
      }

      curr = curr[char]
    }
    if (isInsert) {
      curr.ending = word
    }
    return curr
  }
}

type TrieNode = {
  [key: string]: TrieNode
} & {
  ending?: string
}
// @lc code=end

/*
 * @lc app=leetcode.cn id=212 lang=typescript
 *
 * [212] 单词搜索 II
 *
 * https://leetcode.cn/problems/word-search-ii/description/
 *
 * algorithms
 * Hard (45.50%)
 * Likes:    672
 * Dislikes: 0
 * Total Accepted:    77.6K
 * Total Submissions: 170.6K
 * Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
  '["oath","pea","eat","rain"]'
 *
 * 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words， 返回所有二维网格上的单词 。
 *
 * 单词必须按照字母顺序，通过 相邻的单元格
 * 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：board =
 * [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
 * words = ["oath","pea","eat","rain"]
 * 输出：["eat","oath"]
 *
 *
 * 示例 2：
 *
 *
 * 输入：board = [["a","b"],["c","d"]], words = ["abcb"]
 * 输出：[]
 *
 *
 *
 *
 * 提示：
 *
 *
 * m == board.length
 * n == board[i].length
 * 1 <= m, n <= 12
 * board[i][j] 是一个小写英文字母
 * 1 <= words.length <= 3 * 10^4
 * 1 <= words[i].length <= 10
 * words[i] 由小写英文字母组成
 * words 中的所有字符串互不相同
 *
 *
 */

export
// @lc code=start
function findWords(board: string[][], words: string[]): string[] {
  const rootTrie: TrieNode = {}
  for (const word of words) {
    let curr = rootTrie
    for (const char of word) {
      if (!curr[char]) curr[char] = {}
      curr = curr[char]
    }
    curr.ending = word
  }

  const m = board.length, n = board[0].length
  const seen = new Set<string>()

  function find(i: number, j: number, trie: TrieNode) {
    const char = board[i][j]
    if (!trie[char]) return

    const resp = `${i},${j}`
    if (seen.has(resp)) return
    seen.add(resp)

    trie = trie[char]
    if (trie.ending) {
      result.push(trie.ending)
      delete trie.ending
    }

    for (const [ni, nj] of getDirections(i, j, m, n)) {
      find(ni, nj, trie)
    }

    seen.delete(resp)
  }

  const result: string[] = []

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      find(i, j, rootTrie)
    }
  }

  return result
}

const DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

function* getDirections(i: number, j: number, m: number, n: number) {
  for (const [di, dj] of DIRECTIONS) {
    const ni = i + di, nj = j + dj
    if (ni < 0 || ni >= m || nj < 0 || nj >= n) {
      continue
    }
    yield [ni, nj]
  }
}

type TrieNode = {
  [key: string]: TrieNode
} & {
  ending?: string
}
// @lc code=end

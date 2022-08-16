/*
 * @lc app=leetcode.cn id=17 lang=typescript
 *
 * [17] 电话号码的字母组合
 *
 * https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/
 *
 * algorithms
 * Medium (57.80%)
 * Likes:    1973
 * Dislikes: 0
 * Total Accepted:    511.1K
 * Total Submissions: 884K
 * Testcase Example:  '"23"'
 *
 * 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
 *
 * 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：digits = "23"
 * 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
 *
 *
 * 示例 2：
 *
 *
 * 输入：digits = ""
 * 输出：[]
 *
 *
 * 示例 3：
 *
 *
 * 输入：digits = "2"
 * 输出：["a","b","c"]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0 <= digits.length <= 4
 * digits[i] 是范围 ['2', '9'] 的一个数字。
 *
 *
 */

export
// @lc code=start
function letterCombinations(digits: string): string[] {
  const result: string[] = []

  function helper(i: number, temp: string[]) {
    if (i >= digits.length) {
      if (temp.length) {
        result.push(temp.join(''))
      }
      return
    }

    const d = digits[i]
    if (!LETTERS_MAP[d]) {
      throw new Error(`Illegal character '${d}'`)
    }

    for (const letter of LETTERS_MAP[d]) {
      temp.push(letter)
      helper(i + 1, temp)
      temp.pop()
    }
  }

  helper(0, [])
  return result
}

const LETTERS_MAP: Record<string, string[]> = {
  2: ['a', 'b', 'c'],
  3: ['d', 'e', 'f'],
  4: ['g', 'h', 'i'],
  5: ['j', 'k', 'l'],
  6: ['m', 'n', 'o'],
  7: ['p', 'q', 'r', 's'],
  8: ['t', 'u', 'v'],
  9: ['w', 'x', 'y', 'z'],
}
// @lc code=end

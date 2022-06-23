/*
 * @lc app=leetcode.cn id=679 lang=typescript
 *
 * [679] 24 点游戏
 *
 * https://leetcode.cn/problems/24-game/description/
 *
 * algorithms
 * Hard (53.80%)
 * Likes:    376
 * Dislikes: 0
 * Total Accepted:    33.1K
 * Total Submissions: 61.5K
 * Testcase Example:  '[4,1,8,7]'
 *
 * 给定一个长度为4的整数数组 cards 。你有 4 张卡片，每张卡片上都包含一个范围在 [1,9] 的数字。您应该使用运算符 ['+', '-',
 * '*', '/'] 和括号 '(' 和 ')' 将这些卡片上的数字排列成数学表达式，以获得值24。
 *
 * 你须遵守以下规则:
 *
 *
 * 除法运算符 '/' 表示实数除法，而不是整数除法。
 *
 *
 * 例如， 4 /(1 - 2 / 3)= 4 /(1 / 3)= 12 。
 *
 *
 * 每个运算都在两个数字之间。特别是，不能使用 “-” 作为一元运算符。
 *
 * 例如，如果 cards =[1,1,1,1] ，则表达式 “-1 -1 -1 -1” 是 不允许 的。
 *
 *
 * 你不能把数字串在一起
 *
 * 例如，如果 cards =[1,2,1,2] ，则表达式 “12 + 12” 无效。
 *
 *
 *
 *
 * 如果可以得到这样的表达式，其计算结果为 24 ，则返回 true ，否则返回 false 。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: cards = [4, 1, 8, 7]
 * 输出: true
 * 解释: (8-4) * (7-1) = 24
 *
 *
 * 示例 2:
 *
 *
 * 输入: cards = [1, 2, 1, 2]
 * 输出: false
 *
 *
 *
 *
 * 提示:
 *
 *
 * cards.length == 4
 * 1 <= cards[i] <= 9
 *
 *
 */

export
// @lc code=start
function judgePoint24(_cards: number[]): boolean {
  const cards: Array<[number, string]> = _cards.map(x => [x, String(x)])

  const enumerateTwo = (i: number) => {
    if (cards.length === 1) {
      // if (equals(cards[0][0], 24)) {
      //   console.log(cards)
      // }
      return equals(cards[0][0], 24)
    }

    if (i >= 2) {
      const n1 = cards.shift()!, n2 = cards.shift()!

      for (const op of operations) {
        const result = op(n1, n2)
        cards.push(result)
        if (enumerateTwo(0)) {
          return true
        }
        cards.pop()
      }

      cards.unshift(n2)
      cards.unshift(n1)
      return false
    }

    for (let j = i; j < cards.length; j++) {
      swap(cards, i, j)
      if (enumerateTwo(i + 1)) {
        return true
      }
      swap(cards, i, j)
    }

    return false
  }

  return enumerateTwo(0)
}

interface OperationFunc {
  (a: [number, string], b: [number, string]): [number, string]
}

const operations: OperationFunc[] = [
  ([a, aResp], [b, bResp]) => [a + b, `(${aResp} + ${bResp})`],
  ([a, aResp], [b, bResp]) => [a - b, `(${aResp} - ${bResp})`],
  ([a, aResp], [b, bResp]) => [a * b, `(${aResp} * ${bResp})`],
  ([a, aResp], [b, bResp]) => [a / b, `(${aResp} / ${bResp})`],
]

const equals = (n: number, target: number) => Math.abs(n - target) <= 1e-6

const swap = (arr: any[], i: number, j: number) => {
  const temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp
}
// @lc code=end

// [1,3,4,6]

// console.log(judgePoint24([1, 9, 1, 2]))

// ((1 + 2) * (9 - 1))

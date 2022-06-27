/*
 * @lc app=leetcode.cn id=986 lang=typescript
 *
 * [986] 区间列表的交集
 *
 * https://leetcode.cn/problems/interval-list-intersections/description/
 *
 * algorithms
 * Medium (68.44%)
 * Likes:    292
 * Dislikes: 0
 * Total Accepted:    45.4K
 * Total Submissions: 66.3K
 * Testcase Example:  '[[0,2],[5,10],[13,23],[24,25]]\n[[1,5],[8,12],[15,24],[25,26]]'
 *
 * 给定两个由一些 闭区间 组成的列表，firstList 和 secondList ，其中 firstList[i] = [starti, endi] 而
 * secondList[j] = [startj, endj] 。每个区间列表都是成对 不相交 的，并且 已经排序 。
 *
 * 返回这 两个区间列表的交集 。
 *
 * 形式上，闭区间 [a, b]（其中 a ）表示实数 x 的集合，而 a  。
 *
 * 两个闭区间的 交集 是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3] 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：firstList = [[0,2],[5,10],[13,23],[24,25]], secondList =
 * [[1,5],[8,12],[15,24],[25,26]]
 * 输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
 *
 *
 * 示例 2：
 *
 *
 * 输入：firstList = [[1,3],[5,9]], secondList = []
 * 输出：[]
 *
 *
 * 示例 3：
 *
 *
 * 输入：firstList = [], secondList = [[4,8],[10,12]]
 * 输出：[]
 *
 *
 * 示例 4：
 *
 *
 * 输入：firstList = [[1,7]], secondList = [[3,10]]
 * 输出：[[3,7]]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0
 * firstList.length + secondList.length >= 1
 * 0 i < endi
 * endi < starti+1
 * 0 j < endj
 * endj < startj+1
 *
 *
 */

export
// @lc code=start
function intervalIntersection(firstList: number[][], secondList: number[][]): number[][] {
  const actions: Action[] = [];
  [firstList, secondList].forEach((list, i) => list.forEach(([begin, end]) => {
    actions.push([begin, ActionType.Open, i === 0 ? ListName.List1 : ListName.List2])
    actions.push([end, ActionType.Close, i === 0 ? ListName.List1 : ListName.List2])
  }))

  actions.sort((a, b) => {
    if (a[0] !== b[0]) {
      return a[0] - b[0]
    }
    return a[1] - b[1]
  })

  let l1Status = -1, l2Status = -1

  const result: number[][] = []
  for (let i = 0; i < actions.length; i++) {
    const [time, actionType, listName] = actions[i]
    const status = actionType | listName

    if (status === (ListName.List1 | ActionType.Open)) {
      l1Status = time
    } else if (status === (ListName.List2 | ActionType.Open)) {
      l2Status = time
    } else if (status === (ListName.List1 | ActionType.Close)) {
      if (l2Status >= 0) {
        result.push([Math.max(l2Status, l1Status), time])
      }
      l1Status = -1
    } else if (status === (ListName.List2 | ActionType.Close)) {
      if (l1Status >= 0) {
        result.push([Math.max(l2Status, l1Status), time])
      }
      l2Status = -1
    }
  }

  return result
}

const enum ActionType {
  Open = 0b00,
  Close = 0b01,
}

const enum ListName {
  List1 = 0b10,
  List2 = 0b00,
}

type Action = [number, ActionType, ListName]
// @lc code=end

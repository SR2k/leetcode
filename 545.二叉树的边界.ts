/*
 * @lc app=leetcode.cn id=545 lang=typescript
 *
 * [545] 二叉树的边界
 *
 * https://leetcode.cn/problems/boundary-of-binary-tree/description/
 *
 * algorithms
 * Medium (43.96%)
 * Likes:    94
 * Dislikes: 0
 * Total Accepted:    4.9K
 * Total Submissions: 11.3K
 * Testcase Example:  '[1,null,2,3,4]'
 *
 * 二叉树的 边界 是由 根节点 、左边界 、按从左到右顺序的 叶节点 和 逆序的右边界 ，按顺序依次连接组成。
 *
 * 左边界 是满足下述定义的节点集合：
 *
 *
 * 根节点的左子节点在左边界中。如果根节点不含左子节点，那么左边界就为 空 。
 * 如果一个节点在左边界中，并且该节点有左子节点，那么它的左子节点也在左边界中。
 * 如果一个节点在左边界中，并且该节点 不含 左子节点，那么它的右子节点就在左边界中。
 * 最左侧的叶节点 不在 左边界中。
 *
 *
 * 右边界 定义方式与 左边界 相同，只是将左替换成右。即，右边界是根节点右子树的右侧部分；叶节点 不是
 * 右边界的组成部分；如果根节点不含右子节点，那么右边界为 空 。
 *
 * 叶节点 是没有任何子节点的节点。对于此问题，根节点 不是 叶节点。
 *
 * 给你一棵二叉树的根节点 root ，按顺序返回组成二叉树 边界 的这些值。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：root = [1,null,2,3,4]
 * 输出：[1,3,4,2]
 * 解释：
 * - 左边界为空，因为二叉树不含左子节点。
 * - 右边界是 [2] 。从根节点的右子节点开始的路径为 2 -> 4 ，但 4 是叶节点，所以右边界只有 2 。
 * - 叶节点从左到右是 [3,4] 。
 * 按题目要求依序连接得到结果 [1] + [] + [3,4] + [2] = [1,3,4,2] 。
 *
 * 示例 2：
 *
 *
 * 输入：root = [1,2,3,4,5,6,null,null,null,7,8,9,10]
 * 输出：[1,2,4,7,8,9,10,6,3]
 * 解释：
 * - 左边界为 [2] 。从根节点的左子节点开始的路径为 2 -> 4 ，但 4 是叶节点，所以左边界只有 2 。
 * - 右边界是 [3,6] ，逆序为 [6,3] 。从根节点的右子节点开始的路径为 3 -> 6 -> 10 ，但 10 是叶节点。
 * - 叶节点从左到右是 [4,7,8,9,10]
 * 按题目要求依序连接得到结果 [1] + [2] + [4,7,8,9,10] + [6,3] = [1,2,4,7,8,9,10,6,3] 。
 *
 *
 *
 * 提示：
 *
 *
 * 树中节点的数目在范围 [1, 10^4] 内
 * -1000
 *
 *
 */

import { TreeNode } from './commons/Tree'

export
// @lc code=start
function boundaryOfBinaryTree(root: TreeNode | null): number[] {
  if (!root) return []

  const left: TreeNode[] = [root.left!].filter(Boolean)
  const right: TreeNode[] = [root.right!].filter(Boolean)
  const leaf: TreeNode[] = []

  let curr: TreeNode | null = root
  const stack: TreeNode[] = []

  while (curr || stack.length) {
    while (curr) {
      if (!curr.left && !curr.right) {
        leaf.push(curr)
      } else {
        if (left.at(-1) === curr) {
          left.push((curr.left || curr.right)!)
        }
        if (right.at(-1) === curr) {
          right.push((curr.right || curr.left)!)
        }
      }

      stack.push(curr)
      curr = curr.left
    }

    curr = stack.pop()!.right
  }

  const result = [root]
  pushHelper(result, left, 0, left.length - 1, 1)
  pushHelper(result, leaf, 0, leaf.length - 1, 1)
  pushHelper(result, right, right.length - 1, 0, -1)

  return result.map((x) => x.val)
}

function pushHelper<T>(arr: T[], another: T[], i: number, j: number, delta: number) {
  for (let k = i; k !== j + delta; k += delta) {
    const value = another[k]

    if (!value || arr.at(-1) === value) {
      continue
    }

    arr.push(value)
  }
}
// @lc code=end

console.log(boundaryOfBinaryTree(
  TreeNode.fromArray([1, 2, 3, 4, 5, 6, null, null, null, 7, 8, 9, 10]),
))

console.log(boundaryOfBinaryTree(
  TreeNode.fromArray([1, null, 2, 3, 4]),
))

console.log(boundaryOfBinaryTree(null))

console.log(boundaryOfBinaryTree(
  TreeNode.fromArray([1, 2, 7, 3, 5, null, 6, 4]),
))

// [1,2,3,4,5,6,null,null,null,7,8,9,10]
//          1
//     2       3
//  4   5    6   x
// x x 7 8 9 10

// [1,2,7,3,5,null,6,4]
// [1,2,3,4,5,6,7]

//           1
//      2          7
//    3   5      x   6
//   4


// [1, 2, 3, 4]
// [4, 5, 6]
// [1, 7, 6]

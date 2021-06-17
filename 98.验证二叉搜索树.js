/*
 * @lc app=leetcode.cn id=98 lang=javascript
 *
 * [98] 验证二叉搜索树
 *
 * https://leetcode-cn.com/problems/validate-binary-search-tree/description/
 *
 * algorithms
 * Medium (34.19%)
 * Likes:    1056
 * Dislikes: 0
 * Total Accepted:    269.2K
 * Total Submissions: 787.1K
 * Testcase Example:  '[2,1,3]'
 *
 * 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
 * 
 * 假设一个二叉搜索树具有如下特征：
 * 
 * 
 * 节点的左子树只包含小于当前节点的数。
 * 节点的右子树只包含大于当前节点的数。
 * 所有左子树和右子树自身必须也是二叉搜索树。
 * 
 * 
 * 示例 1:
 * 
 * 输入:
 * ⁠   2
 * ⁠  / \
 * ⁠ 1   3
 * 输出: true
 * 
 * 
 * 示例 2:
 * 
 * 输入:
 * ⁠   5
 * ⁠  / \
 * ⁠ 1   4
 * / \
 * 3   6
 * 输出: false
 * 解释: 输入为: [5,1,4,null,null,3,6]。
 * 根节点的值为 5 ，但是其右子节点值为 4 。
 * 
 * 
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function(root) { 
  const recurse = (root) => {
    if (!root) return

    const left = recurse(root.left)
    const right = recurse(root.right)

    let isValid = true
    if (left) isValid = isValid && left[0] && left[2] < root.val
    if (right) isValid = isValid && right[0] && right[1] > root.val

    return [
      isValid,
      Math.min(left ? left[1] : Infinity, right ? right[1] : Infinity, root.val),
      Math.max(right ? right[2] : -Infinity, left ? left[2] : -Infinity, root.val),
    ]
  }

  // console.log(recurse(root))
  return recurse(root)[0]
};
// @lc code=end


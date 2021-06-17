/*
 * @lc app=leetcode.cn id=105 lang=javascript
 *
 * [105] 从前序与中序遍历序列构造二叉树
 *
 * https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
 *
 * algorithms
 * Medium (69.68%)
 * Likes:    1032
 * Dislikes: 0
 * Total Accepted:    192.8K
 * Total Submissions: 276.8K
 * Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
 *
 * 根据一棵树的前序遍历与中序遍历构造二叉树。
 * 
 * 注意:
 * 你可以假设树中没有重复的元素。
 * 
 * 例如，给出
 * 
 * 前序遍历 preorder = [3,9,20,15,7]
 * 中序遍历 inorder = [9,3,15,20,7]
 * 
 * 返回如下的二叉树：
 * 
 * ⁠   3
 * ⁠  / \
 * ⁠ 9  20
 * ⁠   /  \
 * ⁠  15   7
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
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
 var buildTree = function(preorder, inorder) {
  if (!preorder || !preorder.length) return null

  const root = new TreeNode(preorder[0])
  if (preorder.length === 1) return root

  const rootInOrderIndex = inorder.indexOf(preorder[0])

  const leftPreOrder = preorder.slice(1, rootInOrderIndex + 1)
  const leftInOrder = inorder.slice(0, rootInOrderIndex)
  root.left = buildTree(leftPreOrder, leftInOrder)

  const rightPreOrder = preorder.slice(rootInOrderIndex + 1, preorder.length)
  const rightInOrder = inorder.slice(rootInOrderIndex + 1, inorder.length)
  root.right = buildTree(rightPreOrder, rightInOrder)

  return root
}
// @lc code=end


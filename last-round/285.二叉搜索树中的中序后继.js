/*
 * @lc app=leetcode.cn id=285 lang=javascript
 *
 * [285] 二叉搜索树中的中序后继
 *
 * https://leetcode-cn.com/problems/inorder-successor-in-bst/description/
 *
 * algorithms
 * Medium (63.33%)
 * Likes:    104
 * Dislikes: 0
 * Total Accepted:    6.4K
 * Total Submissions: 10K
 * Testcase Example:  '[2,1,3]\n1'
 *
 * 给定一棵二叉搜索树和其中的一个节点 p ，找到该节点在树中的中序后继。如果节点没有中序后继，请返回 null 。
 * 
 * 节点 p 的后继是值比 p.val 大的节点中键值最小的节点。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 
 * 
 * 输入：root = [2,1,3], p = 1
 * 输出：2
 * 解释：这里 1 的中序后继是 2。请注意 p 和返回值都应是 TreeNode 类型。
 * 
 * 
 * 示例 2：
 * 
 * 
 * 
 * 
 * 输入：root = [5,3,6,2,4,null,null,1], p = 6
 * 输出：null
 * 解释：因为给出的节点没有中序后继，所以答案就返回 null 了。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 树中节点的数目在范围 [1, 10^4] 内。
 * -10^5 
 * 树中各节点的值均保证唯一。
 * 
 * 
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @return {TreeNode}
 */
var inorderSuccessor = function(root, p) {
  let prev
  let result

  const traverse = (node) => {
    if (!node) return

    traverse(node.left)

    if (prev && prev.val === p.val) {
      // console.log(prev, p)
      result = node
      // return
    }
    prev = node

    traverse(node.right)
  }
  traverse(root)

  return result || null
};
// @lc code=end


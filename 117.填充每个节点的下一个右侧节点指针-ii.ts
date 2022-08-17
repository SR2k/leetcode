/*
 * @lc app=leetcode.cn id=117 lang=typescript
 *
 * [117] 填充每个节点的下一个右侧节点指针 II
 *
 * https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/description/
 *
 * algorithms
 * Medium (64.58%)
 * Likes:    621
 * Dislikes: 0
 * Total Accepted:    150.6K
 * Total Submissions: 233.2K
 * Testcase Example:  '[1,2,3,4,5,null,7]'
 *
 * 给定一个二叉树
 *
 *
 * struct Node {
 * ⁠ int val;
 * ⁠ Node *left;
 * ⁠ Node *right;
 * ⁠ Node *next;
 * }
 *
 * 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
 *
 * 初始状态下，所有 next 指针都被设置为 NULL。
 *
 *
 *
 * 进阶：
 *
 *
 * 你只能使用常量级额外空间。
 * 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
 *
 *
 *
 *
 * 示例：
 *
 *
 *
 *
 * 输入：root = [1,2,3,4,5,null,7]
 * 输出：[1,#,2,3,#,4,5,7,#]
 * 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化输出按层序遍历顺序（由 next
 * 指针连接），'#' 表示每层的末尾。
 *
 *
 *
 * 提示：
 *
 *
 * 树中的节点数小于 6000
 * -100
 *
 *
 *
 *
 *
 *
 *
 */

export
// @lc code=start
function connect(root: Node | null): Node | null {
  let currLevelFirstNode = root

  while (currLevelFirstNode) {
    let curr: Node | null = currLevelFirstNode
    let prevChild: Node | null = null
    let nextLevelFirstNode: Node | null = null

    while (curr) {
      nextLevelFirstNode = nextLevelFirstNode || curr.left || curr.right
      prevChild = connectTwo(prevChild, curr.left)
      prevChild = connectTwo(prevChild, curr.right)

      curr = curr.next
    }

    currLevelFirstNode = nextLevelFirstNode
  }

  return root
}

function connectTwo(prev: Node | null, curr: Node | null) {
  if (!curr) {
    return prev
  }
  if (!prev) {
    return curr
  }
  prev.next = curr
  return curr
}
// @lc code=end

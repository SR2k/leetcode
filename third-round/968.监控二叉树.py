#
# @lc app=leetcode.cn id=968 lang=python3
#
# [968] 监控二叉树
#
# https://leetcode-cn.com/problems/binary-tree-cameras/description/
#
# algorithms
# Hard (50.67%)
# Likes:    368
# Dislikes: 0
# Total Accepted:    31.5K
# Total Submissions: 62K
# Testcase Example:  '[0,0,null,0,0]'
#
# 给定一个二叉树，我们在树的节点上安装摄像头。
# 
# 节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。
# 
# 计算监控树的所有节点所需的最小摄像头数量。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：[0,0,null,0,0]
# 输出：1
# 解释：如图所示，一台摄像头足以监控所有节点。
# 
# 
# 示例 2：
# 
# 
# 
# 输入：[0,0,null,0,null,0,null,null,0]
# 输出：2
# 解释：需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。
# 
# 
# 
# 提示：
# 
# 
# 给定树的节点数的范围是 [1, 1000]。
# 每个节点的值都是 0。
# 
# 
#


from commons.Tree import TreeNode


# @lc code=start
inf = float('inf')


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def helper(node: TreeNode):
            if not node:
                return None

            pl, pr = helper(node.left), helper(node.right)

            if not pl and not pr:
                return [1, inf, 0]
            if not pl or not pr:
                p = pl or pr
                return [min(p) + 1, p[0], min(p[0], p[1])]

            dp = [0, 0, 0]
            # put a cam
            dp[0] = min(pl) + min(pr) + 1
            # no putting and curr node is covered by its children
            dp[1] = min(pl[0] + min(pr[0], pr[1]), pr[0] + min(pl[0], pl[1]))
            # inf, no child
            # p[0], single child
            dp[2] = pl[1] + pr[1]

            return dp

        result = helper(root)
        # print(result)
        return min(result[0], result[1]) if result else None
# @lc code=end

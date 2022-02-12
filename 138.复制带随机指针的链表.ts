/*
 * @lc app=leetcode.cn id=138 lang=typescript
 *
 * [138] 复制带随机指针的链表
 *
 * https://leetcode-cn.com/problems/copy-list-with-random-pointer/description/
 *
 * algorithms
 * Medium (66.45%)
 * Likes:    802
 * Dislikes: 0
 * Total Accepted:    126.5K
 * Total Submissions: 190.4K
 * Testcase Example:  '[[7,null],[13,0],[11,4],[10,2],[1,0]]'
 *
 * 给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。
 *
 * 构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random
 * 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。
 *
 * 例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random
 * --> y 。
 *
 * 返回复制链表的头节点。
 *
 * 用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：
 *
 *
 * val：一个表示 Node.val 的整数。
 * random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
 *
 *
 * 你的代码 只 接受原链表的头节点 head 作为传入参数。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 *
 * 输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
 * 输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
 *
 *
 * 示例 2：
 *
 *
 *
 *
 * 输入：head = [[1,1],[2,1]]
 * 输出：[[1,1],[2,1]]
 *
 *
 * 示例 3：
 *
 *
 *
 *
 * 输入：head = [[3,null],[3,0],[3,null]]
 * 输出：[[3,null],[3,0],[3,null]]
 *
 *
 * 示例 4：
 *
 *
 * 输入：head = []
 * 输出：[]
 * 解释：给定的链表为空（空指针），因此返回 null。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0
 * -10000
 * Node.random 为空（null）或指向链表中的节点。
 *
 *
 */

export class Node {
  val: number

  next: Node | null

  random: Node | null

  constructor(val?: number, next?: Node, random?: Node) {
    this.val = val === undefined ? 0 : val
    this.next = next === undefined ? null : next
    this.random = random === undefined ? null : random
  }

  static parse(s: Array<[number, number | null]>) {
    // [[3,null],[3,0],[3,null]]
    const dummyHead = new Node()
    const indexToNode: Node[] = []
    let prev = dummyHead

    for (const [value] of s) {
      const node = new Node(value)
      prev.next = node
      prev = prev.next
      indexToNode.push(node)
    }

    let curr = dummyHead
    for (const [, randomIndex] of s) {
      curr = curr.next!
      if (randomIndex !== null) {
        curr.random = indexToNode[randomIndex]
      }
    }

    return dummyHead.next
  }

  serialize() {
    const nodes: Array<[number, Node | null]> = []
    const orders = new Map<Node, number>()

    let i = 0
    let curr: Node | null = this

    while (curr) {
      orders.set(curr, i)
      i += 1
      nodes.push([curr.val, curr.random])
      curr = curr.next
    }

    return nodes.map(([value, random]) => [value, random && orders.get(random)])
  }
}

export
// @lc code=start
function copyRandomList(head: Node | null): Node | null {
  const map: Map<Node, Node> = new Map()
  const dummyHead = new Node(-1)
  let prev = dummyHead

  function getNode(originalNode: Node | null) {
    if (!originalNode) return originalNode

    if (!map.has(originalNode)) {
      map.set(originalNode, new Node(originalNode.val))
    }
    return map.get(originalNode)!
  }

  while (head) {
    const node = getNode(head)!
    node.random = getNode(head.random)
    prev.next = node
    head = head.next
    prev = node
  }

  return dummyHead.next
}
// @lc code=end

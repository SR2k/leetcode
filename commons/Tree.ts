// from collections import deque
// from typing import Optional

const serialize = <T>(root: TreeNode<T> | null): Array<T | null> => {
  const queue = [root]
  const result = []

  while (queue) {
    const curr = queue.shift()

    if (!curr) {
      result.push(null)
    } else {
      result.push(curr.val)
      queue.push(curr.left)
      queue.push(curr.right)
    }
  }

  return result
}

const parse = <T>(serialized: Array<T | null>): TreeNode<T> | null => {
  if (!serialized.length) return null

  const values = [...serialized]
  const head = new TreeNode(values.shift()!)
  const nodes = [head]

  while (values.length) {
    const currNode = nodes.shift()!

    const leftVal = values.shift()
    if (leftVal !== null && typeof leftVal !== 'undefined') {
      currNode.left = new TreeNode(leftVal)
      nodes.push(currNode.left)
    }

    const rightVal = values.shift()
    if (rightVal !== null && typeof rightVal !== 'undefined') {
      currNode.right = new TreeNode(rightVal)
      nodes.push(currNode.right)
    }
  }

  return head
}

export class TreeNode<T = any> {
  static fromArray<T>(serialized: Array<T | null>) {
    return parse(serialized)
  }

  constructor(
    public val: T,
    public left: TreeNode | null = null,
    public right: TreeNode | null = null,
  ) {
  }

  toString(): string {
    return serialize(this).join(',')
  }
}

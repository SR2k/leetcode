export const serializeGraph = <T>(nodes: GraphNode<T>[]) => {
  const queue: Array<GraphNode<T>> = []
  const seen = new Set<GraphNode<T>>()
  for (const n of nodes) {
    queue.push(n)
    seen.add(n)
  }

  const children = new Map<T, T[]>()
  while (queue.length) {
    const curr = queue.shift()!
    const c: T[] = []

    for (const n of curr.neighbors) {
      c.push(n.val)

      if (!seen.has(n)) {
        seen.add(n)
        queue.push(n)
      }
    }

    children.set(curr.val, c)
  }

  const result: Array<T | null> = [];
  [...children.keys()]
    .sort((a, b) => (a as any) - (b as any))
    .forEach((key) => {
      result.push(key)
      const c = children.get(key)!
      c.sort()
      result.push(...c)
      result.push(null)
    })

  return result
}

export class GraphNode<T> {
  constructor(
    public val: T,
    public neighbors: GraphNode<T>[] = [],
  ) {
  }

  static fromNeighbourArray(neighbours: number[][]): GraphNode<number> {
    const nodes = new Array(neighbours.length)
      .fill(0)
      .map((x, i) => new GraphNode(i + 1))

    neighbours.forEach((n, i) => {
      n.forEach((x) => {
        nodes[i].neighbors.push(nodes[x - 1])
      })
    })

    return nodes[0]
  }

  toString(): string {
    return serializeGraph([this]).join(',')
  }
}

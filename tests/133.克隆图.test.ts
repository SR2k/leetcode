import { cloneGraph } from '../133.克隆图'
import { GraphNode } from '../commons/GraphNode'

describe('133.克隆图', () => {
  it('should work', () => {
    let source: GraphNode<number>
    let target: GraphNode<number>

    source = GraphNode.fromNeighbourArray([[2, 4], [1, 3], [2, 4], [1, 3]])
    target = cloneGraph(source)!
    expect(source.toString()).toBe(target.toString())

    source = GraphNode.fromNeighbourArray([[]])
    target = cloneGraph(source)!
    expect(source.toString()).toBe(target.toString())

    source = GraphNode.fromNeighbourArray([[2], [1]])
    target = cloneGraph(source)!
    expect(source.toString()).toBe(target.toString())

    expect(cloneGraph(null)).toBeNull()
  })
})

class Heap {
  public values: number[] = []

  constructor(
    private readonly cmp: (a: number, b: number) => number = (a, b) => a - b,
  ) {
  }

  public static fromHeapify(values: number[]) {
    const h = new Heap()
    h.values = values

    for (let i = 0; i < values.length; i++) {
      h.shiftUp(i)
    }

    return h
  }

  public push(value: number) {
    this.values.push(value)
    this.shiftUp(this.values.length - 1)
  }

  public pop() {
    const value = this.values[0]
    this.values[0] = this.values[this.values.length - 1]
    this.values.pop()
    this.shiftDown(0)
    return value
  }

  private shiftUp(i: number) {
    let curr = i
    while (curr) {
      const parent = Heap.parent(curr)
      if (this.shouldSwap(parent, curr)) {
        Heap.swap(this.values, curr, parent)
      }
      curr = parent
    }
  }

  private shiftDown(i: number) {
    let parentIndex = i
    let childIndex = this.compareChildrenOf(parentIndex)

    while (this.shouldSwap(parentIndex, childIndex)) {
      Heap.swap(this.values, parentIndex, childIndex)
      parentIndex = childIndex
      childIndex = this.compareChildrenOf(parentIndex)
    }
  }

  private compareChildrenOf(i: number) {
    const left = Heap.leftChild(i)
    const right = Heap.rightChild(i)

    if (left >= this.values.length && right >= this.values.length) {
      return -1
    }

    if (left >= this.values.length) {
      return right
    }

    if (right >= this.values.length) {
      return left
    }

    const compare = this.cmp(this.values[left], this.values[right])
    return compare > 0 ? right : left
  }

  private shouldSwap(parent: number, child: number) {
    if (parent < 0 || parent >= this.values.length) {
      return false
    }
    if (child < 0 || child >= this.values.length) {
      return false
    }

    return this.cmp(this.values[parent], this.values[child]) > 0
  }

  private static swap(arr: any[], i: number, j: number) {
    [arr[i], arr[j]] = [arr[j], arr[i]]
  }

  private static parent(i: number) {
    return Math.floor(i - 1)
  }

  private static leftChild(i: number) {
    return this.rightChild(i) - 1
  }

  private static rightChild(i: number) {
    return 2 * (i + 1)
  }
}

const heap = Heap.fromHeapify([
  62, 52, 41, 30, 28,
  16, 22, 13, 18, 17,
  15,
])

console.log(heap.values)

while (heap.values.length) {
  console.log(heap.pop())
  console.log(heap.values)
}

//           13
//       15     16
//   17    18  22 28
// 30 41 52 62 22

//     0
//   1   2
// 3  4 5 6

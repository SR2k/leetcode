export class ListNode<T = any> {
  static fromArray<T>(arr: T[]): ListNode<T> | null {
    const dummy: ListNode<T> = new ListNode(null as any);
    let curr = dummy;

    for (const n of arr) {
      curr.next = new ListNode(n);
      curr = curr.next;
    }

    return dummy.next;
  }

  constructor(public val: T, public next: ListNode<T> | null = null) {}

  public toString(): string {
    const result: T[] = [];
    const seen = new Set();

    let curr: ListNode<T>|null = this;

    while (curr) {
      if (seen.has(curr)) {
        throw new Error("Circular linked list");
      }
      seen.add(curr)
      result.push(curr.val);
      curr = curr.next;
    }

    return result.join(" -> ");
  }
}

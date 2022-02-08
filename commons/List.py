class ListNode:
    @staticmethod
    def from_arr(l: list[int]):
        dummy = ListNode(-1)
        curr = dummy

        for n in l:
            curr.next = ListNode(n)
            curr = curr.next

        return dummy.next


    def __init__(self, val=0, next:'ListNode'=None):
        self.val = val
        self.next = next


    def __str__(self) -> str:
        result = []
        curr = self

        while curr:
            result.append(curr.val)
            curr = curr.next

        return ",".join(str(x) for x in result)

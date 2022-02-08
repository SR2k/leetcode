from collections import deque
from typing import Optional


def serialize(root: 'TreeNode') -> list[Optional[int]]:
    queue = deque([root])
    result = []

    while queue:
        curr = queue.popleft()

        if not curr:
            result.append(None)
        else:
            result.append(curr.val)
            queue.append(curr.left)
            queue.append(curr.right)

    return result


def parse(serialized: list[Optional[int]]):
    if not serialized:
        return None

    values = deque(serialized)
    head = TreeNode(values.popleft())
    nodes = deque([head])

    while values:
        curr_node = nodes.popleft()

        left_val = values.popleft()
        if left_val is not None:
            curr_node.left = TreeNode(int(left_val))
            nodes.append(curr_node.left)

        right_val = values.popleft()
        if right_val is not None:
            curr_node.right = TreeNode(int(right_val))
            nodes.append(curr_node.right)

    return head


class TreeNode:
    def __init__(self, val: int, left:Optional['TreeNode']=None, right:Optional['TreeNode']=None) -> None:
        self.val = val
        self.left = left
        self.right = right


    def __str__(self):
        temp = ['null' if x is None else str(x) for x in serialize(self)]
        return ','.join(temp)


    @staticmethod
    def deserialize(serialized: str):
        return parse(serialized)

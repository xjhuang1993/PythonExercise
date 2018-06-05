"""
Accepted
两个指针跟踪
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def func(head: ListNode, n: int):
    tmp_head = ListNode(0)
    tmp_head.next = head
    q = head
    p = head
    for i in range(n):
        q = q.next
    while q.next:
        q = q.next
        p = p.next
    p.next = p.next.next
    return tmp_head.next


def out(head: ListNode):
    while head:
        print(head.val)
        head = head.next


if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5]
    head = ListNode(nodes[0])
    tmp_head = head
    for i in range(1, len(nodes)):
        tmp_node = ListNode(nodes[i])
        tmp_head.next = tmp_node
        tmp_head = tmp_head.next
    n = 2
    print(out(func(head, 2)))

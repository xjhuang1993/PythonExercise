"""
Accepted
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def func(head: ListNode):
    if not head:
        return []
    if not head.next:
        return head
    result = ListNode(0)
    result.next = head
    tmp = result
    p = head
    q = head.next
    while True:
        tmp.next = q
        p.next = q.next
        q.next = p
        tmp = p
        if p.next:
            p = p.next
        else:
            break
        if p.next:
            q = p.next
        else:
            break
    return result.next


def out(head: ListNode):
    while head:
        print(head.val)
        head = head.next


if __name__ == "__main__":
    nodes = [1, 2]
    head = ListNode(nodes[0])
    tmp_head = head
    for i in range(1, len(nodes)):
        tmp_node = ListNode(nodes[i])
        tmp_head.next = tmp_node
        tmp_head = tmp_head.next
    print(out(func(head)))

"""
Accepted
先计数，然后找到对应节点
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def func(head: ListNode, n: int):
    tmp_head = ListNode(0)
    tmp_head.next = head
    num = 0
    tmp_node = head
    while tmp_node:
        num += 1
        tmp_node = tmp_node.next
    num = num - n
    tmp_node = tmp_head
    while num > 0:
        num -= 1
        tmp_node = tmp_node.next
    tmp_node.next = tmp_node.next.next
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

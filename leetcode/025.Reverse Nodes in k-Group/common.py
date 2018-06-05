"""
Accepted
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def func(head: ListNode, k):
    if not head:
        return []
    if not head.next:
        return head
    val_list = []
    tmp_head = head
    while tmp_head:
        val_list.append(tmp_head.val)
        tmp_head = tmp_head.next
    index = 0
    m = 0
    tmp_list = []
    result_list = []
    for vl in val_list:
        tmp_list.append(vl)
        if (index + 1) % k == 0:
            tmp_list.reverse()
            result_list += tmp_list
            tmp_list.clear()
            m += k
        index += 1
    if m != len(val_list):
        result_list += val_list[m:]
    result_head = ListNode(0)
    result_tmp_head = result_head
    for rl in result_list:
        tmp_node = ListNode(rl)
        result_tmp_head.next = tmp_node
        result_tmp_head = result_tmp_head.next
    return result_head.next


def out(head: ListNode):
    while head:
        print(head.val)
        head = head.next


if __name__ == "__main__":
    nodes = [1, 2, 3, 4]
    head = ListNode(nodes[0])
    tmp_head = head
    for i in range(1, len(nodes)):
        tmp_node = ListNode(nodes[i])
        tmp_head.next = tmp_node
        tmp_head = tmp_head.next
    k = 2
    print(out(func(head, k)))

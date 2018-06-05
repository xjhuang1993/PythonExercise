"""
Accepted
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def func(head):
    if not head:
        return []
    if not head.next:
        return head
    val_list = []
    tmp_head = head
    while tmp_head:
        val_list.append(tmp_head.val)
        tmp_head = tmp_head.next
    i = 1
    while i < len(val_list):
        if val_list[i - 1] == val_list[i]:
            tmp_val = val_list[i]
            while True:
                try:
                    val_list.remove(tmp_val)
                except ValueError:
                    break
        else:
            i += 1
    result_head = ListNode(0)
    result_tmp_head = result_head
    for vl in val_list:
        tmp_node = ListNode(vl)
        result_tmp_head.next = tmp_node
        result_tmp_head = result_tmp_head.next
    return result_head.next


def out(head: ListNode):
    while head:
        print(head.val)
        head = head.next


if __name__ == "__main__":
    nodes = [1, 2, 3, 3, 4, 4, 5]
    head = ListNode(nodes[0])
    tmp_head = head
    for i in range(1, len(nodes)):
        tmp_node = ListNode(nodes[i])
        tmp_head.next = tmp_node
        tmp_head = tmp_head.next
    print(out(func(head)))

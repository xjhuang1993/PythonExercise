"""
Accepted
先把链表val值按序存入列表中，然后按题目要求将列表改变
最后取列表元素构造链表
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def func(head, k):
    if not head:
        return None
    if not head.next:
        return head
    result_list = []
    tmp_head = head
    while tmp_head:
        result_list.append(tmp_head.val)
        tmp_head = tmp_head.next
    length_result_list = len(result_list)
    k = k % length_result_list  # 右旋转k次，只用在原基础上旋转k mod length_of_ListNodes次
    result_list = result_list[length_result_list - k:] + result_list[:length_result_list - k]
    result = ListNode(0)
    tmp = result
    for rl in result_list:
        tmp.next = ListNode(rl)
        tmp = tmp.next
    return result.next


def out(head: ListNode):
    while head:
        print(head.val)
        head = head.next


if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5]
    k = 2
    head = ListNode(nodes[0])
    tmp_head = head
    for i in range(1, len(nodes)):
        tmp_node = ListNode(nodes[i])
        tmp_head.next = tmp_node
        tmp_head = tmp_head.next
    print(out(func(head, k)))

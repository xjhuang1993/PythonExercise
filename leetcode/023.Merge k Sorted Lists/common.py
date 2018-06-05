"""
Time Limit Exceeded
这个方法太笨了。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def sub_func(l1: ListNode, l2: ListNode):
    p = l1
    q = l2
    r = ListNode(0)
    tmp = r
    while p and q:
        if p.val > q.val:
            tmp.next = q
            tmp = tmp.next
            q = q.next
        else:
            tmp.next = p
            tmp = tmp.next
            p = p.next
    if p:
        tmp.next = p
    if q:
        tmp.next = q
    return r.next


def func(lists):
    if len(lists) == 0:
        return []
    if len(lists) == 1:
        return lists[0]
    l1 = lists[0]
    l2 = lists[1]
    tmp = sub_func(l1, l2)
    for i in range(2, len(lists)):
        tmp = sub_func(tmp, lists[i])
    return tmp


def out(head: ListNode):
    while head:
        print(head.val)
        head = head.next


if __name__ == "__main__":
    nums1 = [1, 2, 4]
    nums2 = [1, 3, 4]
    l1 = ListNode(nums1[0])
    l2 = ListNode(nums2[0])
    tmp_l1 = l1
    tmp_l2 = l2
    for i in range(1, len(nums1)):
        tmp = ListNode(nums1[i])
        tmp_l1.next = tmp
        tmp_l1 = tmp_l1.next
    for i in range(1, len(nums2)):
        tmp = ListNode(nums2[i])
        tmp_l2.next = tmp
        tmp_l2 = tmp_l2.next
    lists = [l1, l2]
    print(out(func(lists)))

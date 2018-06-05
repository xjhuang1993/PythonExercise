"""
Accepted
先将k个链表的value取出来，然后将这些values排序，再按照排序构建节点组成链表
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def func(lists):
    head = p = ListNode(0)
    nums = list()
    for l in lists:
        while l:
            nums.append(l.val)
            l = l.next
    nums.sort()
    for num in nums:
        p.next = ListNode(num)
        p = p.next
    return head.next


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

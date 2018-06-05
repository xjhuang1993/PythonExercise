"""
Accepted
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):
    head = ListNode(0)
    p, q, ln = l1, l2, head
    carry = 0
    while p or q:
        x = p.val if p else 0
        y = q.val if q else 0
        sum = carry + x + y
        carry = sum // 10   # py3后的"/"和"//"的改动
        sum = sum % 10
        ln.next = ListNode(sum)
        ln = ln.next
        p = p.next if p else p
        q = q.next if q else q
    if carry:
        ln.next = ListNode(carry)
    return head.next


if __name__ == "__main__":
    list1 = [2, 4, 3]
    list2 = [5, 6, 4]
    l1 = ListNode(0)
    l2 = ListNode(0)
    p, q = l1, l2
    for i in range(3):
        p.next = ListNode(list1[i])
        q.next = ListNode(list2[i])
        p = p.next
        q = q.next
    ln = add_two_numbers(l1.next, l2.next)
    result = list()
    while ln:
        result.append(ln.val)
        ln = ln.next
    print(result)


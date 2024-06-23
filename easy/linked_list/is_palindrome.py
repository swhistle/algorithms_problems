class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome(head: ListNode) -> bool:
    reversed_values_stack = []

    l_list = head

    while l_list is not None:
        reversed_values_stack.append(l_list.val)
        l_list = l_list.next

    reversed_list = tail = ListNode(reversed_values_stack.pop())

    while len(reversed_values_stack) > 0:
        tail.next = ListNode(reversed_values_stack.pop())
        tail = tail.next

    while head is not None and reversed_list is not None:
        if head.val != reversed_list.val:
            return False

        head = head.next
        reversed_list = reversed_list.next

    return True


head_1 = ListNode(1, ListNode(2, ListNode(2, ListNode(1, ))))
res_1 = is_palindrome(head_1)
print(res_1)

head_2 = ListNode(1, ListNode(2))
res_2 = is_palindrome(head_2)
print(res_2)
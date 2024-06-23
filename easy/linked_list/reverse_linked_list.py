class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next

def reverse_linked_list(head: ListNode) -> ListNode:
    if head is None:
        return None

    reversed_values_stack = []

    while head is not None:
        reversed_values_stack.append(head.val)
        head = head.next

    reversed_list = tail = ListNode(reversed_values_stack.pop())

    for i in range(0, len(reversed_values_stack)):
        tail.next = ListNode(reversed_values_stack.pop())
        tail = tail.next

    return reversed_list


list_1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

list_2 = ListNode(1, ListNode(3, ListNode(10)))

reversed_list_1 = reverse_linked_list(list_1)
reversed_list_2 = reverse_linked_list(list_2)
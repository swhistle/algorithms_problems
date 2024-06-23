# Definition for singly-linked list.
class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next


def merge_two_linked_lists(list1, list2):
    if list1 is None and list2 is None:
        return None

    if list1 is None:
        return list2

    if list2 is None:
        return list1

    if list1.val < list2.val:
        next_merged = head = ListNode(list1.val)
        list1 = list1.next
    else:
        next_merged = head = ListNode(list2.val)
        list2 = list2.next

    while list1 is not None and list2 is not None:
        if list1.val < list2.val:
            next_merged.next = ListNode(list1.val)
            list1 = list1.next
        else:
            next_merged.next = ListNode(list2.val)
            list2 = list2.next
        next_merged = next_merged.next

    while list1 is not None:
        next_merged.next = ListNode(list1.val)
        list1 = list1.next
        next_merged = next_merged.next

    while list2 is not None:
        next_merged.next = ListNode(list2.val)
        list2 = list2.next
        next_merged = next_merged.next

    return head

list_1 = ListNode(1, ListNode(2, ListNode(4)))
list_2 = ListNode(1, ListNode(3, ListNode(4)))

merged = merge_two_linked_lists(list_1, list_2)
print(merged.val)
print(merged.next.val)
print(merged.next.next.val)
print(merged.next.next.next.val)
print(merged.next.next.next.next.val)
print(merged.next.next.next.next.next.val)
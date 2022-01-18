class Node:

    def __init__(self, data=None, next_node=None):
        """ data     : de gegevens die je wil opslaan in deze `Node`.
            next_node: de volgende `Node` in de lineair gelinkte lijst.
        """
        self.data = data
        self.next = next_node


def print_list(head):
    items = []  # aan te passen

    # BEGIN JOUW CODE
    while head is not None:
        items.append(head.data)
        head = head.next

    # EINDE JOUW CODE

    print("[" + ",".join(str(_) for _ in items) + "]")


def merge(head_1, head_2):
    head = Node("")
    if head_1 is None:
        return head_2
    elif head_2 is None:
        return head_1

    if head_1.data < head_2.data:
        hulp = head_1
        head.next = head_1
        head_1 = head_1.next

    else:
        hulp = head_2
        head.next = head_2
        head_2 = head_2.next

    while head_1 is not None and head_2 is not None:
        if head_1.data < head_2.data:
            hulp.next = head_1
            head_1 = head_1.next

        else:
            hulp.next = head_2
            head_2 = head_2.next

        hulp = hulp.next

    if head_1 is None:
        while head_2 is not None:
            hulp.next = head_2
            head_2 = head_2.next
            hulp = hulp.next

    else:
        while head_1 is not None:
            hulp.next = head_1
            head_1 = head_1.next
            hulp = hulp.next
    return head.next


def split(head):
    fast = head
    slow = head
    hulp = slow
    while fast.next is not None:
        if fast.next.next is None:
            break
        hulp = slow.next
        fast = fast.next.next
        slow = slow.next
    if fast.next is not None:
        if fast.next.next is None:
            second = slow.next
    else:
        second = slow.next
    hulp.next = None

    return head, second


def merge_sort(head):
    if head.next is None:
        return head

    first, second = split(head)

    merge(merge_sort(first), merge_sort(second))


head = Node(5, Node(4, Node(3, Node(2, Node(1)))))
print_list(head)
head = merge_sort(head)
print_list(head)

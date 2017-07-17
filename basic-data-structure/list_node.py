class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)


def reverse_iter(head):
    """

    :param head: ListNode, head node on the single way ListNode
    :return: ListNode, the new head node when ListNode reversed
    """
    current_index = None
    while head:
        temp_node = head.next
        head.next = current_index
        current_index = head
        head = temp_node
    return current_index


def reverse_recur(head):
    """

    :param head: ListNode, head node on the single way ListNode
    :return: ListNode, the new head node when ListNode reversed
    """
    if head is None or head.next is None:
        return head
    next_node = head.next
    new_head = reverse_recur(next_node)
    next_node.next = head
    head.next = None
    return new_head

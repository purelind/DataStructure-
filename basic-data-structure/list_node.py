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



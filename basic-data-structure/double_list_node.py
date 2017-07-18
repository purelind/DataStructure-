class DListNode:
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None


def reverse_iter(head):
    """

    :param head: DListNode, head double list node
    :return: DListNode, the new head double list node when reversed
    """
    current = None
    while head:
        current = head
        head = current.next
        current.next = current.prev
        current.prev = head
    return current



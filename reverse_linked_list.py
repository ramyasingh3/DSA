class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    # Initialize prev as None since the last node will point to None
    prev = None
    # Start with the head node
    current = head
    
    # Traverse the linked list
    while current:
        # Store the next node before we change the current node's next pointer
        next_temp = current.next
        # Reverse the link
        current.next = prev
        # Move prev and current one step forward
        prev = current
        current = next_temp
    
    # Return the new head (prev will be the new head)
    return prev

# Helper function to create a linked list from a list of values
def createLinkedList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print the linked list
def printLinkedList(head):
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    return " -> ".join(values)

# Test the solution
if __name__ == "__main__":
    # Create a test linked list: 1 -> 2 -> 3 -> 4 -> 5
    test_values = [1, 2, 3, 4, 5]
    head = createLinkedList(test_values)
    
    print("Original linked list:")
    print(printLinkedList(head))
    
    # Reverse the linked list
    reversed_head = reverseList(head)
    
    print("\nReversed linked list:")
    print(printLinkedList(reversed_head)) 
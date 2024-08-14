class Node:  
    def __init__(self, data):  
        self.data = data  
        self.next = None
      
def reverse(node): 
    if node is None or node.next is None: 
        return node 
          
    # Recursively reverse the rest of the list
    new_head = reverse(node.next) 
    
    # Adjust the pointers to reverse the link
    node.next.next = node 
    node.next = None
    
    return new_head 
  
def printList(head): 
    temp = head 
    while temp is not None: 
        print(temp.data, end=" ") 
        temp = temp.next
    print()  # For a newline after the list is printed
          
def push(head_ref, new_data): 
    new_node = Node(new_data) 
    new_node.next = head_ref 
    return new_node
  
if __name__=='__main__':  
      
    # Start with the empty list  
    head = None
    head = push(head, 20) 
    head = push(head, 4) 
    head = push(head, 15) 
    head = push(head, 85) 
  
    print("Given linked list") 
    printList(head) 
  
    head = reverse(head) 
  
    print("Reversed Linked list") 
    printList(head)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return
        
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    break
                current = current.right
    
    def search(self, value):
        """Search for a value in the BST"""
        current = self.root
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False
    
    def inorder_traversal(self, node, result=None):
        """Inorder traversal of the BST (Left-Root-Right)"""
        if result is None:
            result = []
        
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)
        return result
    
    def find_min(self):
        """Find the minimum value in the BST"""
        if not self.root:
            return None
        
        current = self.root
        while current.left:
            current = current.left
        return current.value
    
    def find_max(self):
        """Find the maximum value in the BST"""
        if not self.root:
            return None
        
        current = self.root
        while current.right:
            current = current.right
        return current.value
    
    def is_valid_bst(self, node=None, min_val=float('-inf'), max_val=float('inf')):
        """Check if the tree is a valid BST"""
        if node is None:
            node = self.root
        
        if not node:
            return True
            
        if node.value <= min_val or node.value >= max_val:
            return False
            
        return (self.is_valid_bst(node.left, min_val, node.value) and 
                self.is_valid_bst(node.right, node.value, max_val))

# Example usage and test cases
if __name__ == "__main__":
    bst = BinarySearchTree()
    
    # Insert some values
    values = [50, 30, 70, 20, 40, 60, 80]
    for value in values:
        bst.insert(value)
    
    # Test traversal
    print("Inorder traversal:", bst.inorder_traversal(bst.root))
    
    # Test search
    print("Search 40:", bst.search(40))  # Should return True
    print("Search 90:", bst.search(90))  # Should return False
    
    # Test min and max
    print("Minimum value:", bst.find_min())  # Should return 20
    print("Maximum value:", bst.find_max())  # Should return 80
    
    # Test BST validity
    print("Is valid BST:", bst.is_valid_bst())  # Should return True 
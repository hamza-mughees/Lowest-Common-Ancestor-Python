class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_val:'int'):
        self.root = Node(root_val)
    
    def lca(self, p:'Node', q:'Node'):
        return self._lca(self.root, p, q)
    
    def _lca(self, curr_node:'Node', p:'Node', q:'Node'):
        if curr_node is None:
            return None
        
        if curr_node.value == p.value or curr_node.value == q.value:
            return curr_node
        
        left_subtree = self._lca(curr_node.left, p, q)
        right_subtree = self._lca(curr_node.right, p, q)
        
        if left_subtree is None: return right_subtree
        if right_subtree is None: return left_subtree
        
        return curr_node

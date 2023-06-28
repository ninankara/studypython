'''
solve 함수를 구현하세요.
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def addNode(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = addNode(root.left, value)
    else:
        root.right = addNode(root.right, value)
    return root

def level_order_traversal(root):
    if root is None:
        return[]
        
    result = []
    queue = []
    queue.append(root)

    while queue:
        node = queue.pop(0)
        result.append(node.value)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

def solve(nodes) :
    
    root = None
    for node in nodes:
        root = addNode(root, node)
    
    result = level_order_traversal(root)

    return result

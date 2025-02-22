from typing import Iterable, List, Optional

class Node:
    def __init__(self, value: int):
        self.value = value
        self.count = 1
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, elements: Iterable[int] = None):
        self.root = None

        def binary_constructor(l: int, r: int):
            if l > r:
                return
            m = (l + r) // 2
            self.insert(elements[m])
            binary_constructor(l, m-1)
            binary_constructor(m+1, r)

        if elements:
            binary_constructor(0, len(elements)-1)

    def insert(self, el: int):
        def dfs(node: Node):
            if el < node.value:
                if node.left: dfs(node.left)
                else: node.left = Node(el)
            elif el > node.value:
                if node.right: dfs(node.right)
                else: node.right = Node(el)
            else:
                node.count += 1
        
        if not self.root:
            self.root = Node(el)
        else:
            dfs(self.root)

    def get_inorder(self) -> Optional[List[int]]:
        if not self.root:
            return []
        result = []
        def dfs(node: Node):
            if not node:
                return
            dfs(node.left)
            for _ in range(node.count):
                result.append(node.value)
            dfs(node.right)
        dfs(self.root)
        return result

    def delete(self, el: int, force=False):
        def get_successor(node: Node) -> Node:
            if node.left:
                return get_successor(node.left)
            return node
        
        def dfs(node: Optional[Node]):
            if not node:
                return node
            
            if el < node.value:
                node.left = dfs(node.left)
            elif el > node.value:
                node.right = dfs(node.right)
            else:
                if node.count > 1 and not force:
                    node.count -= 1
                else:
                    if not node.left and not node.right:
                        return None
                    elif not node.left and node.right:
                        return node.right
                    elif node.left and not node.right:
                        return node.left
                    else:
                        successor = get_successor(node.right)
                        self.delete(successor.value, force=True)
                        node.value = successor.value
                        node.count = successor.count
            return node
        
        dfs(self.root)

    def get_max(self) -> Optional[int]:
        def dfs(node: Node):
            if node.right:
                return dfs(node.right)
            return node.value
        if not self.root: return None
        else: return dfs(self.root)
    
    def get_min(self) -> Optional[int]:
        def dfs(node: Node):
            if node.left:
                return dfs(node.left)
            return node.value
        if not self.root: return None
        else: return dfs(self.root)
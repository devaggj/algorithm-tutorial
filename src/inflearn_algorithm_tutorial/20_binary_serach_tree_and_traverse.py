"""
:ref_1: http://ejklike.github.io/2018/01/09/traversing-a-binary-tree-1.html
:ref_2: http://ejklike.github.io/2018/01/09/traversing-a-binary-tree-2.html
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        
class BinarySearchTree(object):
    
    # [이진트리 class 기본세팅]
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node
        
    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)
    
    # [이진트리 순회알고리즘 part]
    # 전위 순회 (root => left => right)
    def pre_order_traversal(self):
        def _pre_order_traversal(root):
            if root is None:
                pass
            else:
                print(root.data)
                _pre_order_traversal(root.left)
                _pre_order_traversal(root.right)
        _pre_order_traversal(self.root)
        
    # 정위 순회 (left => root => right)
    def in_order_traversal(self):
        def _in_order_traversal(root):
            if root is None:
                pass
            else:
                _in_order_traversal(root.left)
                print(root.data)
                _in_order_traversal(root.right)
        _in_order_traversal(self.root)
        
    # 후위 순회 (left => right => root)
    def post_order_traversal(self):
        def _post_order_traversal(root):
            if root is None:
                pass
            else:
                _post_order_traversal(root.left)
                _post_order_traversal(root.right)
                print(root.data)
        _post_order_traversal(self.root)


def main():
    # array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]
    # bst = BinarySearchTree()
    # for i in array:
    #     bst.insert(i)
        
    bst = BinarySearchTree()
    for i in range(1, 16):
        if i % 2 == 0:
            bst._insert_value(i, i)
        else:
            bst._insert_value(i, i)
    
    
    print(bst.find(15))
    print(bst.find(17))
    
    # bst.pre_order_traversal()
    bst.in_order_traversal()
    # bst.post_order_traversal()
    

if __name__ == "__main__":
    main()
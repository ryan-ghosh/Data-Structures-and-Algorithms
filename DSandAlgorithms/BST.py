
class Node:
    # change repr for needs. This outline uses string for printing
    def __init__(self, value: int, left=None, right=None, parent=None, height=1, bf=0):
        self.left = left
        self.right = right
        self.parent = parent
        self.bf = bf
        self.height = height
        self.value = value

    def __repr__(self):
        return str(self.value)


class BST:
    def __init__(self, root: Node):
        self.root = root

    def insert(self, node, curr=None):
        if curr:
            curr = curr
        else:
            curr = self.root
        if curr is None:
            curr = node
        if node.value < curr.value:
            if curr.left:
                self.insert(node, curr.left)
            else:
                node.parent = curr
                curr.left = node
        if node.value > curr.value:
            if curr.right:
                self.insert(node, curr.right)
            else:
                node.parent = curr
                curr.right = node

    def deleteNode(self, node: Node):
        if node == self.root:
            if not node.left and not node.right:
                node = None
            elif node.left and not node.right:
                self.root = node.left
                self.deleteNode(node.left)
            elif node.right and not node.left:
                self.root = node.right
                self.deleteNode(node.right)
            elif node.right and node.left:    # if both exist
                curr = node.left
                while curr.right:   # find successor
                    curr = curr.right
                node.value = curr.value
                self.deleteNode(curr)
        elif not node.left and not node.right:  # leaf
            if node.parent.right == node:
                node.parent.right = None
            if node.parent.left == node:
                node.parent.left = None
        elif node.left and not node.right:    #only left child
            node.left.parent = node.parent
            node.parent.right = node.left
            node = None
        elif node.right and not node.left:    #only right child
            node.right.parent = node.parent
            node.parent.right = node.right
            node = None
        elif node.right and node.left:    # if both exist
            curr = node.left
            while curr.right:   # find successor
                curr = curr.right
            curr.parent = node.parent
            node.value = curr.value
            
            self.deleteNode(curr)

    def search(self, val, curr=None):
        if curr:
            curr = curr
        else:
            curr = self.root
        if curr.value == val:
            return True
        if not curr.left and not curr.right:
            return False
        if not curr.left and curr.value > val:
            return False
        if not curr.right and curr.value < val:
            return False
        elif curr.value > val:  # if current greater than search value, go left
            return self.search(val, curr.left)
        elif curr.value < val:  # if current less than search value, go right
            return self.search(val, curr.right)

    def postorder(self, curr):  # good for deletion and balancing factor maintenance
        tree = []
        if curr:
            tree = self.postorder(curr.left)
            tree += self.postorder(curr.right)
            tree.append(curr.value)
        return tree

    def preorder(self, curr):  # good for building trees
        tree = []
        if curr:
            tree.append(curr.value)
            tree += self.preorder(curr.left)
            tree += self.preorder(curr.right)
        return tree

    def inorder(self, curr):  # good for listing in sorted order
        tree = []
        if curr:
            tree += self.inorder(curr.left)
            tree.append(curr.value)
            tree += self.inorder(curr.right)
        return tree

    def bf_traversal(self, node, bflist):
        if node:
            self.bf_traversal(node.left, bflist)
            self.bf_traversal(node.right, bflist)
            self.update_height(node)
            node.bf = self.find_bf(node)
            bflist.append(abs(node.bf))
        return bflist

    def delete_tree(self, curr=None):
        if curr==None:
            curr = self.root
        if curr.left:
            self.delete_tree(curr.left)
        elif curr.right:
            self.delete_tree(curr.right)
        if not curr.left and not curr.right:
            self.deleteNode(curr)

    def find_bf(self, node):
        if node.right is None and node.left is None:
            bfl = -1
            bfr = -1
        if node.right and node.left:
            bfr = node.right.height
            bfl = node.left.height
        if node.left and node.right is None:
            bfl = node.left.height
            bfr = -1
        if node.right and node.left is None:
            bfr = node.right.height
            bfl = -1
        bf = bfr - bfl
        return bf

    def balanced_insert(self, node, curr=None):
        curr = curr if curr else self.root
        self.insert(node, curr)
        self.balance_tree(node)

    def is_balanced(self):
        if self.root is None:
            return True
        bflist = []
        self.bf_traversal(node=self.root, bflist=bflist)
        if max(bflist) > 1:
            return False
        else:
            return True

    def left_rotate(self, z):
        y = z.right
        y.parent = z.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is z:
                y.parent.left = y
            elif y.parent.right is z:
                y.parent.right = y
        z.right = y.left
        if z.right is not None:
            z.right.parent = z
        y.left = z
        z.parent = y
        self.update_height(z)
        self.update_height(y)

    def right_rotate(self, z):
        y = z.left
        y.parent = z.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.right is z:
                y.parent.right = y
            elif y.parent.left is z:
                y.parent.left = y
        z.left = y.right
        if z.left is not None:
            z.left.parent = z
        y.right = z
        z.parent = y
        self.update_height(z)
        self.update_height(y)

    def balance_tree(self, node):
        if self.is_balanced():
            return
        while not self.is_balanced():
            parent = node.parent
            if node.bf == -1:
                if node.parent.bf > 1:
                    self.right_rotate(node)
            elif node.bf == 1:
                if node.parent.bf < -1:
                    self.left_rotate(node)
            elif node.bf < -1:
                self.right_rotate(node)
            elif node.bf > 1:
                self.left_rotate(node)
            node = parent
        return

    def height(self, node):
        return node.height if node else -1

    def update_height(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def lca(self, node1, node2):
        if node1.value > node2.value:
            node1, node2 = node2, node1
        if node1 == self.root or node2 == self.root:
            return self.root
        if node2.value > self.root.value > node1.value:
            return self.root.value
        if self.root.value < node2.value and self.root.value < node1.value:
            curr = self.root
            while curr.right:
                curr = curr.right
                if node2.value > curr.value > node1.value:
                    return curr.value
        if self.root.value > node2.value and self.root.value > node1.value:
            curr = self.root
            while curr.left:
                curr = curr.left
                if node2.value > curr.value > node1.value:
                    return curr.value



if __name__ == "__main__":
    q = Node(10)
    tree = BST(q)
    w = Node(5)
    e = Node(20)
    r = Node(3)
    t = Node(7)
    y = Node(15)
    u = Node(30)
    i = Node(6)
    node_list = [q,w,e,r,t,y,u,i]
    for i in node_list:
        tree.insert(i)
    # tree.deleteNode(q)
    # print(tree.search(10))
    # print(tree.root)
    # print(tree.root.right)
    # print(tree.root.left.left)
    tree.delete_tree()
    print(tree.root.left)



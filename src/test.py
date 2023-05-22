import time

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        self.height = 1
 
class AVLTree:
    def __init__(self):
        self.root = None

    #definir las funciones del AVL
    def insertAVL(self,key):
        self.root = self.insert(self.root,key)

    def deleteAVL(self,key):
        self.root = self.delete(self.root,key)

    def preOrderAVL(self):
        self.preOrder(self.root)

    def find_nodeAVL(self,key):
        return self.find_node(self.root,key)


    def insert(self, root, key):
         
        # Step 1 - Perform normal BST
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
 
        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.getHeight(root.left),
                          self.getHeight(root.right))
 
        # Step 3 - Get the balance factor
        balance = self.getBalance(root)
 
        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)
 
        # Case 2 - Right Right
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)
 
        # Case 3 - Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        # Case 4 - Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root

    def delete(self, root, key):
        if not root:
            return root
 
        elif key < root.val:
            root.left = self.delete(root.left, key)
 
        elif key > root.val:
            root.right = self.delete(root.right, key)
 
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
 
            elif root.right is None:
                temp = root.left
                root = None
                return temp
 
            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right,
                                      temp.val)
 
        # If the tree has only one node,
        # simply return it
        if root is None:
            return root
 
        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.getHeight(root.left),
                            self.getHeight(root.right))
 
        # Step 3 - Get the balance factor
        balance = self.getBalance(root)
 
        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)
 
        # Case 2 - Right Right
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)
 
        # Case 3 - Left Right
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        # Case 4 - Right Left
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root
 
    def leftRotate(self, z):
 
        y = z.right
        T2 = y.left
 
        # Perform rotation
        y.left = z
        z.right = T2
 
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                         self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                         self.getHeight(y.right))
 
        # Return the new root
        return y
 
    def rightRotate(self, z):
 
        y = z.left
        T3 = y.right
 
        # Perform rotation
        y.right = z
        z.left = T3
 
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                          self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                          self.getHeight(y.right))
 
        # Return the new root
        return y
 
    def getHeight(self, root):
        if not root:
            return 0
 
        return root.height
 
    def getBalance(self, root):
        if not root:
            return 0
 
        return self.getHeight(root.left) - self.getHeight(root.right)
 
    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
 
        return self.getMinValueNode(root.left)
 
    def preOrder(self, root):
 
        if not root:
            return
 
        print("{0} ".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def find_node(self, root, key):
        if not root:
            return None
        elif root.val == key:
            return root
        elif key < root.val:
            return self.find_node(root.left, key)
        else:
            return self.find_node(root.right, key)
    
    def get_path_to_node(self, root, key, path=[]):
        if not root:
            return None
        elif root.val == key:
            path.append(root)
            return path
        elif key < root.val:
            path.append(root)
            return self.get_path_to_node(root.left, key, path)
        else:
            path.append(root)
            return self.get_path_to_node(root.right, key, path)

    def distance_between_nodes(self, node_a, node_b):
        root = self.root
        path_to_a = self.get_path_to_node(root, node_a.val, [])
        path_to_b = self.get_path_to_node(root, node_b.val, [])

        if not path_to_a or not path_to_b:
            return None

        i = 0
        while i < len(path_to_a) and i < len(path_to_b) and path_to_a[i] == path_to_b[i]:
            i += 1

        distance = (len(path_to_a) - i) + (len(path_to_b) - i)
        return distance


myTree = AVLTree()

for i in range (100000000+1):
    root = myTree.insertAVL(i)

start = time.time()
myTree.deleteAVL(100000000)
end = time.time()
print("%.20f"%((end-start)*1000))
# Name: Abhay Kumar
# Roll No.: 2501730185
# Section: A

# ================= BST =================
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return BSTNode(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None:
            return False
        if root.key == key:
            return True
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def find_min(self, root):
        while root.left:
            root = root.left
        return root

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Case 1: No child
            if root.left is None and root.right is None:
                return None

            # Case 2: One child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Case 3: Two children
            temp = self.find_min(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        return root


# ================= GRAPH =================
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, w))

    def bfs(self, start):
        visited = set()
        queue = [start]

        while queue:
            node = queue.pop(0)
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                for neighbor, _ in self.graph.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        print(start, end=" ")
        visited.add(start)

        for neighbor, _ in self.graph.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)


# ================= HASH TABLE =================
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return

    def display(self):
        for i, bucket in enumerate(self.table):
            print(i, ":", bucket)


# ================= MAIN =================
def main():
    print("\n--- BST OPERATIONS ---")
    bst = BST()
    root = None

    values = [50, 30, 70, 20, 40, 60, 80]
    for v in values:
        root = bst.insert(root, v)

    print("Inorder:")
    bst.inorder(root)

    print("\nSearch 20:", bst.search(root, 20))
    print("Search 90:", bst.search(root, 90))

    # Delete leaf
    root = bst.delete(root, 20)
    print("\nAfter deleting 20:")
    bst.inorder(root)

    # Create one-child case
    root = bst.insert(root, 65)
    root = bst.delete(root, 60)
    print("\nAfter deleting 60:")
    bst.inorder(root)

    # Delete two-child node
    root = bst.delete(root, 50)
    print("\nAfter deleting 50:")
    bst.inorder(root)


    print("\n\n--- GRAPH ---")
    g = Graph()

    edges = [
        ('A','B',2), ('A','C',4),
        ('B','D',7), ('B','E',3),
        ('C','E',1), ('D','F',5),
        ('E','D',2), ('E','F',6),
        ('C','F',8)
    ]

    for u, v, w in edges:
        g.add_edge(u, v, w)

    print("Adjacency List:", g.graph)

    print("BFS from A:")
    g.bfs('A')

    print("\nDFS from A:")
    g.dfs('A')


    print("\n\n--- HASH TABLE ---")
    ht = HashTable(5)

    keys = [10, 15, 20, 7, 12]
    for k in keys:
        ht.insert(k, k*10)

    print("Hash Table:")
    ht.display()

    print("Get 10:", ht.get(10))
    print("Get 7:", ht.get(7))
    print("Get 12:", ht.get(12))

    ht.delete(15)
    print("After deleting 15:")
    ht.display()


if __name__ == "__main__":
    main()
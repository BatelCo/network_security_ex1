# Batel Cohen, 208521195, Yonatan Segal, 342476611

from hashlib import sha256

from Node import Node


class MerkleTree:
    def __init__(self):
        self.root = None
        self.nodes = []
        self.hash_to_node = dict()
        self.index_to_leaf_node = dict()

    # Fill in a list of leaf nodes, a dictionary from a hash to node and a dictionary from an index to a leaf node.
    def createLeaves(self, leaves):
        for i, leaf in enumerate(leaves):
            node = Node(leaf)
            node.index = i
            self.nodes.append(node)
            self.hash_to_node[leaf] = node
            self.index_to_leaf_node[i] = node

    # Loop through nodes and for each pair of children, create a parent with a hash value of the concatenation of its
    # children. Continue recursively.
    def createTree(self):
        # for each pair, create parent
        if len(self.nodes) == 1:
            self.root = self.nodes[0]
            return self.root
        parents = []
        for i in range(0, len(self.nodes), 2):
            hash = self.encrypt(self.nodes[i].hash_value + self.nodes[i + 1].hash_value)
            parent = Node(hash)
            # Keep parent for later calculation.
            self.hash_to_node[hash] = parent
            parent.add_left_child(self.nodes[i])
            parent.add_right_child(self.nodes[i + 1])
            parents.append(parent)
        self.nodes = parents
        return self.createTree()

    # Use SHA256 to encrypt.
    def encrypt(self, string):
        return sha256(string.encode()).hexdigest()

    # Return proof of inclusion.
    def get_proof_of_inclusion(self, leaf):
        path = self.get_path_to_root(leaf)
        print(path)
        return path

    # Retrieve node. Recursively hash node with its sibling to move up the tree.
    def get_path_to_root(self, node):
        # Get node.
        if node.isdigit() and int(node) in self.index_to_leaf_node:
            node = self.index_to_leaf_node[int(node)]
        else:
            node = self.hash_to_node[node]
        # If we reach the root.
        if node.parent is None:
            return ""
        # If we're on the left side of a node, hash sibling to our right.
        if not node.isLeft:
            return "l" + " " + node.get_sibling().hash_value + " " + self.get_path_to_root(
                self.encrypt(node.get_sibling().hash_value + node.hash_value))
        # If we're on the right side of the node, hash sibling to our left.
        else:
            return "r" + " " + node.get_sibling().hash_value + " " + self.get_path_to_root(
                self.encrypt(node.hash_value + node.get_sibling().hash_value))

    # Brute force through every combination of numbers until we get n leading zeros when hashed together with our
    # root hash.
    def find_nonce(self, n):
        root_value = self.root.hash_value
        i = 0
        while self.encrypt(str(i) + root_value)[:int(n)] != '0' * int(n):
            i += 1
        return str(i) + " " + self.encrypt(str(i) + root_value)

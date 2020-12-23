# Batel Cohen, 208521195, Yonatan Segal, 342476611

class Node:

    def __init__(self, value):
        self.hash_value = value
        self.left_child = None
        self.right_child = None
        self.isLeft = False
        self.parent = None
        self.index = None

    # add left child
    def add_left_child(self, left_child):
        left_child.isLeft = True
        left_child.parent = self
        self.left_child = left_child

    # add right child
    def add_right_child(self, right_child):
        right_child.isLeft = False
        right_child.parent = self
        self.right_child = right_child

    # get sibling
    def get_sibling(self):
        if self.isLeft:
            return self.parent.right_child
        else:
            return self.parent.left_child

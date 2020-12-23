# Batel Cohen, 208521195, Yonatan Segal, 342476611

from MerkleTree import MerkleTree
from Proof import Proof
import sys

def main():
    case = input()
    tree = None
    while case != '5':
        args = case.split(" ")
        # 1 create merkle tree from list of strings
        if args[0] == '1':
            tree = create_tree(leaves=args[1:])
        # 2 create proof of inclusion for leaf
        elif args[0] == '2':
            if tree is not None:
                tree.get_proof_of_inclusion(leaf=args[1])
                # if tree is none
            else:
                sys.exit()
        # 3 check proof of inclusion
        elif args[0] == '3':
            proof = Proof()
            print(proof.prove_inclusion(node_hash=args[1], root_hash=args[2], path=args[3:]))
        # 4 Find nonce for a given n.
        elif args[0] == '4':
            if tree is not None:
                # the difficulty can not be 0
                if args[1] == '0':
                    sys.exit()
                else:
                    print(tree.find_nonce(n=args[1]))
            # if tree is none
            else:
                sys.exit()
        # next case input
        case = input()


# create merkle tree by given leaves and print the hash value
def create_tree(leaves):
    merkle_tree = MerkleTree()
    merkle_tree.createLeaves(leaves)
    print(merkle_tree.createTree().hash_value)
    return merkle_tree


if __name__ == "__main__":
    main()

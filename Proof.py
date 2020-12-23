# Batel Cohen, 208521195, Yonatan Segal, 342476611
import sys
from hashlib import sha256


class Proof:
    def prove_inclusion(self, node_hash, root_hash, path):
        steps = self.get_steps(path)
        # Check all pairs of directions and corresponding hashes, encrypt as instructed and compare to the root hash
        # at the end.
        for step in steps:
            direction = step[0]
            hash_with = step[1]
            if direction == "l":
                hash = self.encrypt(hash_with + node_hash)
            elif direction == "r":
                hash = self.encrypt(node_hash + hash_with)
            else:
                sys.exit()
            node_hash = hash
        if node_hash == root_hash:
            return True
        return False

    # return the path from the leaf to the root as pairs of directions and hashes.
    def get_steps(self, path):
        steps = path
        smaller_steps = []
        for i in range(0, len(steps), 2):
            smaller_steps.append((steps[i], steps[i + 1]))
        return smaller_steps

    # encrypt function
    def encrypt(self, string):
        return sha256(string.encode()).hexdigest()

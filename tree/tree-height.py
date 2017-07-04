import threading
import numpy as np

"""
Input:
node number: 5
parent node: 4 -1 4 1 1
Output: 3
The input means that there are 5 nodes with numbers from 0 to 4, node 0 is a child of node 4, node 1
is the root, node 2 is a child of node 4, node 3 is a child of node 1 and node 4 is a child of node 1. -1 means the root
"""

class TreeHeight:
    def read(self, nodes, links):
        self.n = int(nodes)
        self.parent = list(map(int, links.split()))
        self.heightTable = np.zeros((int(nodes),), dtype=np.int)

    def compute_height(self):
        maxHeight = 0
        for vertex in range(self.n):
            height = 0
            i = vertex
            while i != -1:
                if self.heightTable[i] != 0:
                    height += self.heightTable[i]
                    break
                else:
                    height += 1
                    i = self.parent[i]
            maxHeight = max(maxHeight, height)
            self.heightTable[vertex] = height
        return maxHeight

def main():
    tree = TreeHeight()
    tree.read(nodes, links)
    print(tree.compute_height())

threading.Thread(target=main).start()
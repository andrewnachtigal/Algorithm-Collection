# python3
# python2
from functools import wraps
from time import time
import os
from collections import deque

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print 'func:%r args:[%r, %r] took: %2.4f sec' % (f.__name__, args, kw, te-ts)
        return result
    return wrap

def ReadTestFile():
    test_dir = 'tests/'
    for fName in os.listdir(test_dir):
        if fName[-2:] == ".a":
            continue
        elif fName != "02":
            continue 
        else:
            testFilepath = os.path.join(test_dir, fName)
            return testFilepath
"""
an AVL tree is a self-balancing binary search tree.
In an AVL tree, the heights of the two child subtrees of any node differ by at most one;
if at any time they differ by more than one, rebalancing is done to restore this property.
Lookup, insertion, and deletion all take O(log n) time in both the average and worst cases, 
where n is the number of nodes in the tree prior to the operation.
Insertions and deletions may require the tree to be rebalanced by one or more tree rotations.
"""
class Node:

  def __init__(self, key):
    self.left = None
    self.right = None
    self.key = key

  def __str__(self):
    return "%s" % self.key

class AVLTree():
  """
  Implementation of AVL tree
  """
  def __init__(self):
    self.node = None
    self.height = -1
    self.balance = 0

  def insert(self, key):
    """
    Insert new node to the tree

    If the key is 
    (1) smaller than current node, check if we can insert it in the left subtree. 
    (2) larger, try to insert it in the right subtree
    (3) Duplicates are not allowed in the tree
    """
    # Create new node
    n = Node(key)

    # Initial tree
    if self.node == None:
        self.node = n
        self.node.left = AVLTree()
        self.node.right = AVLTree()
    # Insert key to the left subtree
    elif key < self.node.key:
        self.node.left.insert(key)
    # Insert key to the right subtree
    elif key > self.node.key:
        self.node.right.insert(key)
    else:
        return
    # Exit, key already exists in the tree
       
    # Rebalance tree if needed
    self.rebalance()

  def delete(self, key):
    """
    Let node X be the node with the value we need to delete, 
    and let node Y be a node in the tree we need to find to take node X's place, 
    and let node Z be the actual node we take out of the tree.

    Steps to consider when deleting a node in an AVL tree are the following:
      * If node X is a leaf or has only one child, skip to step 5. (node Z will be node X)
        * Otherwise, determine node Y by finding the largest node in node X's left sub tree (in-order predecessor) 
          or the smallest in its right sub tree (in-order successor).
        * Replace node X with node Y (remember, tree structure doesn't change here, only the values). 
          In this step, node X is essentially deleted when its internal values were overwritten with node Y's.
        * Choose node Z to be the old node Y.
      * Attach node Z's subtree to its parent (if it has a subtree). If node Z's parent is null, update root. (node Z is currently root)
      * Delete node Z
      * Retrace the path back up the tree (starting with node Z's parent) to the root, adjusting the balance factors as needed.
    """
    if self.node != None:
        if self.node.key == key:
            # Key found in leaf node, just erase it
            if not self.node.left.node and not self.node.right.node:
                self.node = None
            # Node has only one subtree (right), replace root with that one
            elif not self.node.left.node:                
                self.node = self.node.right.node
            # Node has only one subtree (left), replace root with that one
            elif not self.node.right.node:
                self.node = self.node.left.node
            else:
                # Find  successor as smallest node in right subtree or
                #       predecessor as largest node in left subtree
                successor = self.node.right.node  
                while successor and successor.left.node:
                    successor = successor.left.node

                if successor:
                    self.node.key = successor.key

                    # Delete successor from the replaced node right subree
                    self.node.right.delete(successor.key)

        elif key < self.node.key:
            self.node.left.delete(key)

        elif key > self.node.key:
            self.node.right.delete(key)

        # Rebalance tree
        self.rebalance()

  def rebalance(self):
    """
    After (1)inserting or (2)deleting a node, 
    it is necessary to check each of the node's ancestors to know if we need to rebalance the tree by calculate 
    (1)update height
    (2)balance tree
    If tree is out of balance, and then rebalance it.
    Balancing is done by (1)single left or (2)right rotations or (3)with double left or right rotations of the tree.
    """
    self.update_heights(recursive=False)
    self.update_balances(recursive=False)
    while self.balance < -1 or self.balance > 1: 
        # Left subtree is larger than right subtree
        if self.balance > 1:

            # Left Right Case -> rotate y,z to the left
            if self.node.left.balance < 0:
                self.node.left.rotate_left()
                self.update_heights()
                self.update_balances()

            self.rotate_right()
            self.update_heights()
            self.update_balances()
        
        # Right subtree is larger than left subtree
        if self.balance < -1:
            
            # Right Left Case -> rotate x,z to the right
            if self.node.right.balance > 0:
                self.node.right.rotate_right() # we're in case III
                self.update_heights()
                self.update_balances()

            self.rotate_left()
            self.update_heights()
            self.update_balances()

  def update_heights(self, recursive=True):
    """
    Update tree height

    Tree height is max height of either left or right subtrees +1 for root of the tree
    """
    if self.node: 
        if recursive: 
            if self.node.left: 
                self.node.left.update_heights()
            if self.node.right:
                self.node.right.update_heights()
        
        self.height = 1 + max(self.node.left.height, self.node.right.height)
    else: 
        self.height = -1

  def update_balances(self, recursive=True):
    """
    Calculate tree balance factor

    The balance factor is calculated as follows: 
        balance = height(left subtree) - height(right subtree). 
    """
    if self.node:
        if recursive:
            if self.node.left:
                self.node.left.update_balances()
            if self.node.right:
                self.node.right.update_balances()

        self.balance = self.node.left.height - self.node.right.height
    else:
        self.balance = 0 


  def rotate_right(self):
    """
    With right rotation, left subtree replaces current root.
    Right rotation: set self as the right subtree of left subree
    """
    new_root = self.node.left.node
    new_left_sub = new_root.right.node
    old_root = self.node

    self.node = new_root
    old_root.left.node = new_left_sub
    new_root.right.node = old_root

  def rotate_left(self):
    """
    With left rotation, right subtree root replaces current root.
    Left rotation: set self as the left subtree of right subree
    """
    new_root = self.node.right.node
    new_left_sub = new_root.left.node
    old_root = self.node

    self.node = new_root
    old_root.right.node = new_left_sub
    new_root.left.node = old_root

  def getMinimum(self):
    
    if self.node.left.node == None:
      return self.node.key
    else:
      return self.node.left.getMinimum()

class JobQueue:
    def read_data(self):
        testFilepath = ReadTestFile()
        with open(testFilepath, 'r') as f:
          line1, line2, _= f.read().split('\n')
          self.num_workers, m = map(int, line1.split())
          self.jobs = list(map(int, line2.split()))
          assert m == len(self.jobs)
    def write_response(self):
        for i in range(len(self.jobs)):
          pass# print(self.assigned_workers[i], self.start_times[i])
    @timing
    def assign_jobs(self):

        # set worker number
        worker_tree = AVLTree()
        for key in range(self.num_workers): 
            worker_tree.insert(key)    

        # set schedule loggers
        
        self.assigned_workers = [None] * self.jobs.__len__()
        self.start_times = [None] * self.jobs.__len__()

        # set free time dictionary 
        free_time_tree = AVLTree()
        free_time_tree.insert(0)
        next_free_time_dict = {0: worker_tree}

        for i in range(len(self.jobs)):
            # assign tasks
            MinFreeTime = free_time_tree.getMinimum()
            HighPriorityWorker = next_free_time_dict[MinFreeTime].getMinimum()

            self.assigned_workers[i] = HighPriorityWorker
            self.start_times[i] = MinFreeTime
            
            # delete old record
            next_free_time_dict[MinFreeTime].delete(HighPriorityWorker)
            if next_free_time_dict[MinFreeTime].node == None: ## if the worker at that free time is empty     
              next_free_time_dict.pop(MinFreeTime)
              free_time_tree.delete(MinFreeTime)

            # compute new free time
            nextFreeTime = MinFreeTime + self.jobs[i]
            # insert it to free time dict and worker queue
            if nextFreeTime in next_free_time_dict:
              next_free_time_dict[nextFreeTime].insert(HighPriorityWorker)
            else:
              free_time_tree.insert(nextFreeTime)
              newQueue = AVLTree()
              newQueue.insert(HighPriorityWorker)
              next_free_time_dict[nextFreeTime] = newQueue

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

#if __name__ == '__main__':
def main():
    job_queue = JobQueue()
    job_queue.solve()
main()
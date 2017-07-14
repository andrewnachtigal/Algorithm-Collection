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
        elif fName != "01":
            continue 
        else:
            testFilepath = os.path.join(test_dir, fName)
            return testFilepath

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
          print(self.assigned_workers[i], self.start_times[i])

    def SiftUp(self, index):
        # 0-based min-heap
        node = index-1
        parent = (index >> 1) - 1
        while self._data[node] < self._data[parent]:
          self._swaps.append((parent, node))
          self._data[parent], self._data[node] = self._data[node], self._data[parent]
          parent = ((parent+1) >> 1) - 1
          node = ((node+1) >> 1) - 1
          if parent < 0:
            break

    def CreateHeap(self):
        self.next_free_time = deque([[0, deque(range(self.num_workers))]])
        self.HasFreeTime = {0:{}}

    def UpdateHeap(self):
        self.next_free_time[self.next_free_time[0][0]]
        
    def FindElement(self, element):
        return self.HasFreeTime.pop(element, None) is None
        





    #     workerQueue = deque([1,1,3,4,5])
    #     print workerQueue
    #     workerQueue.append(6)
    #     print workerQueue
    #     workerQueue.append(11)
    #     print workerQueue
    #     workerQueue.popleft()
    #     print workerQueue
    #     workerQueue.popleft()
    #     print workerQueue

    def assign_jobs(self):
        """
        Assign the jobs to the workers

        In "next_free_time", search the minimum and get next_worker from deque
        
        Update next_free_time[next_worker] += self.jobs[i]

        Sort next_free_time based on (1) time and (2) worker index
        
        Update start_times[next_job] <- next_free_time[next_worker]
        
        Update assigned_workers[next_job] <- next_worker
        """

        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)

        for i in range(len(self.jobs)):
          self.assigned_workers[i] = self.next_free_time[0][1][0]
          self.start_times[i] = next_free_time[self.next_free_time[0][0]]

          nextFreeTime = self.next_free_time[0][0] + self.jobs[i]
          if FindElement(self, nextFreeTime) is None:
            pass
          else:
            pass
          self.next_free_time.append([self.next_free_time[self.next_free_time[0][0]], ])

          UpdateHeap()

    def test(self, ele):
      a = [5,6,9,14,18,20,31,44,65,97]
      low = 0
      high = a.__len__() - 1
      mid  = (low + high) >> 1
      i = 0 
      while high >= low:
        if a[mid] == ele:
          return mid
        elif a[mid] > ele:
          if high == low:
            return -1
          high = mid6
        else:
          if high == low:
            return -1
          low = mid + 1

        mid  = (low + high) >> 1

        i+=1
        print i
        if i == a.__len__():
          break
    def quicksort_test(self, left, right, pivot):
      a = [97,9,14,44,18,6,65,20,5,31]
      left = 0
      right = a.__len__() - 1
      pivot = 0
      i = 0
      while right >= left:
        while a[pivot] > a[left]:
          left += 1
        while a[pivot] < a[right]:
          right -= 1
        if left <= right:
          a[right], a[left] = a[left], a[right]
        else:
          a[right], a[pivot] = a[pivot], a[right]
      
      i+=1
      print i
      if i == a.__len__():
        break  

    def quickSort(self, alist):
       quickSortHelper(alist,0,len(alist)-1)

    def quickSortHelper(self, alist,first,last):
       if first<last:

           splitpoint = partition(alist,first,last)

           quickSortHelper(alist,first,splitpoint-1)
           quickSortHelper(alist,splitpoint+1,last)


    def partition(self, alist,first,last):
       pivotvalue = alist[first]

       leftmark = first+1
       rightmark = last

       done = False
       while not done:

           while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
               leftmark = leftmark + 1



    def solve(self):
        self.read_data()
        self.quicksort_test()
        #self.CreateHeap()
        #print "the position" + str(self.test(i))

        #print self.FindElement(78)
        #self.assign_jobs()
        #self.write_response()

#if __name__ == '__main__':
@timing
def main():
    job_queue = JobQueue()
    job_queue.solve()
main()
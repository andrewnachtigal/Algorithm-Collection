# python2
class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def SiftUp(self, index):
    # 0-based min-heap
    node = index-1
    parent = (index >> 1)-1
    while self._data[node] < self._data[parent]:
      self._swaps.append((parent, node))
      self._data[parent], self._data[node] = self._data[node], self._data[parent]
      parent = ((parent+1) >> 1) - 1
      node = ((node+1) >> 1) - 1
      if parent < 0:
        break

  def GenerateSwaps(self):
    heapSize = len(self._data) 
    for i in range(heapSize, 1, -1):
      self.SiftUp(i)

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
  heap_builder = HeapBuilder()
  heap_builder.Solve()
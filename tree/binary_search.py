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
      high = mid
    else:
      if high == low:
        return -1
      low = mid + 1

    mid  = (low + high) >> 1

    i+=1
    print i
    if i == a.__len__():
      break

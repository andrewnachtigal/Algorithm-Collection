from functools import wraps
from time import time
import os
from collections import deque

def GetNumberLargerThan(array, target):
    low = 0
    high = array.__len__() -1
    while high >= low:
        mid = (low + high)/2
        if array[mid] > target:
            high = mid
        else:
            low = mid
        if high - low <= 1:
            return high
            
class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.finish_time_ = []

    def Process(self, request):
        # print ("packet arrival time: " + str(request.arrival_time))
        # print ("packet process time: " + str(request.process_time))
        # print ("before filter" + str(self.finish_time_))
        # filter
        index = GetNumberLargerThan(self.finish_time_, request.arrival_time)
        if self.finish_time_.__len__() == 0:
            pass
        elif request.arrival_time < self.finish_time_[index]:
            self.finish_time_ = self.finish_time_[index:]
        else:
            self.finish_time_ = []

        # process
        if self.finish_time_.__len__() < self.capacity:
            self.finish_time_.append(request.arrival_time + request.process_time)
            return Response(False, request.arrival_time)
        else:
            return Response(True, -1)

def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, raw_input().strip().strip("\n").split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, _buffer):
    return map(_buffer.Process, requests)

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    capacity, count = map(int, raw_input().strip().strip("\n").split())
    responses = ProcessRequests(ReadRequests(count), Buffer(capacity))
    PrintResponses(responses)
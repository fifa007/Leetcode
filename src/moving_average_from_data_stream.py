#!/usr/bin/env python2.7


'''
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

For example,
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
'''

class moving_average(object):
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.l = []

    def get_average(self, value):
        if self.count < self.size:
            self.count += 1
        else:
            self.l.pop(0)
        self.l.append(value)
        return float(sum(self.l)) / self.count
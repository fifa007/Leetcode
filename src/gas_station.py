#!/usr/bin/env python2.7

'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel
from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
'''

class Solution(object):
    def gas_station(self, gas, cost):
        if gas is None or cost is None or len(gas) != len(cost):
            return -1
        n = len(gas)
        sum = 0
        left = 0
        index = 0
        for i in xrange(n):
            sum += gas[i] - cost[i]
            left += gas[i] - cost[i]
            if sum < 0:
                index = i + 1
                sum = 0
        return index if left >= 0 else -1
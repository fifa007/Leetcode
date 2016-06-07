#!/usr/bin/env python2.7


'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
'''


class Solution(object):
    def dfs(self, s, cnt, sol, ret):
        if cnt == 4:
            if s == '':
                ret.append(sol[1:])
                return
        for i in xrange(1, 4):
            if i <= len(s):
                if int(s[:i]) <= 255:
                    self.dfs(s[i:], cnt+1, sol + '.' + s[:i], ret)
                if s[0] == '0':
                    break

    def restore_ip_address(self, s):
        if s is None:
            return None
        ret = []
        self.dfs(s, 0, '', ret)
        return ret
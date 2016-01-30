#!/usr/bin/env python2.7

'''
unit tests for shortest distance
'''

import src.shortest_word_distance
import unittest


class shortest_distance_test(unittest.TestCase):
    sol = src.shortest_word_distance.Solution()
    words = ["practice", "makes", "perfect", "coding", "makes"]

    def test_with_null_words(self):
        self.failUnless(self.sol.shortest_distance(None, 'a', 'b') == -1)

    def test_with_single_word(self):
        self.failUnless(self.sol.shortest_distance(['a'], 'a', 'b') == -1)

    def test_with_word_list1(self):
        self.failUnless(self.sol.shortest_distance(self.words,
                                                   "coding", "practice") == 3)

    def test_with_word_list2(self):
        self.failUnless(self.sol.shortest_distance(self.words,
                                                   "makes", "coding") == 1)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
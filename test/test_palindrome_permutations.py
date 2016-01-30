#!/usr/bin/env python2.7

'''
unit test for palindrome permutations
'''


import unittest
import src.palindrome_permutation


class palindrome_permutation_test(unittest.TestCase):
    sol = src.palindrome_permutation.Solution()


    def test_with_null_string(self):
        self.failUnless(self.sol.is_palindrome_permutation(None) == False)

    def test_with_char(self):
        self.failUnless(self.sol.is_palindrome_permutation('a') == True)


    def test_with_palindrome_str(self):
        self.failUnless(self.sol.is_palindrome_permutation('aab') == True)

    def test_with_non_palindrome_str(self):
        self.failUnless(self.sol.is_palindrome_permutation('aabbcd') == False)

def main():
    unittest.main()


if __name__ == "__main__":
    main()



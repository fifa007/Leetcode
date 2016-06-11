#!/usr/bin/env python2.7


'''
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A
.means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
'''

import src.data_structure

class Solution(object):
    def __init__(self):
        self.trie = src.data_structure.TrieNode()
        self.count = 0

    def add_word(self, word):
        if word is None:
            return
        p = self.trie
        for c in word:
            idx = ord(c) - ord('a')
            if not p.children[idx]:
                p.children[idx] = src.data_structure.TrieNode()
            p = p.children[idx]
        self.count += 1
        p.value = self.count

    def search_word(self, word):
        if word is None:
            return False
        return self.search_helper(word, 0, self.trie)

    def search_helper(self, word, start, p):
        if len(word) == start:
            if p.value == 0:
                return False
            else:
                return True
        if word[start] == '.':
            for child in p.children:
                if child:
                    if self.search_helper(word, start+1, child):
                        return True
        else:
            idx = ord(word[start]) - ord('a')
            if p.children[idx]:
                if self.search_helper(word, start+1, p.children[idx]):
                    return True
        return False
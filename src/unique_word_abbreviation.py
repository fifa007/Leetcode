#!/usr/bin/env python2.7


'''
An abbreviation of a word follows the form <first letter><number><last letter>.
Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary.
A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example:
Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true
'''

class ValidWordAbbr(object):
    def get_abbrev(self, s):
        if s is None or len(s) == 0:
            return None
        if len(s) == 1:
            return s
        return s[0] + str(len(s) - 2) + s[len(s)-1]

    def __init__(self, dictionary):
        self.s = {}
        if dictionary is None or len(dictionary) == 0:
            return
        for d in dictionary:
            key = self.get_abbrev(d)
            if self.s.has_key(key):
                self.s[key].append(d)
            else:
                self.s[key] = [d,]

    def is_unique(self, word):
        if word is None or len(word) == 0:
            return True
        key = self.get_abbrev(word)
        if key not in self.s:
            return True
        elif word in self.s[key]:
            for w in self.s[key]:
                if w != word:
                    return False
            return True
        return False
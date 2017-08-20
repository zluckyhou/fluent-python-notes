# -*- coding:utf-8 -*-
from collections import abc

my_dict = {}
isinstance(my_dict, abc.Mapping)
tt = (1, 2, (30, 40))
hash(tt)
t1 = (1, 2, [30, 40])
hash(t1)
tf = (1, 2, frozenset([30, 40]))
hash(tf)

# dict comprehensions

DIAL_CODES = [(86, 'China'),
              (91, 'India'),
              (1, 'United States'),
              (62, 'Indonesia'),
              (55, 'Brazil'),
              (92, 'Pakistan'),
              (880, 'Bangladesh'),
              (234, 'Nigeria'),
              (7, 'Russia'),
              (81, 'Japan'),
              ]

country_code = {country: code for code, country in DIAL_CODES}
{code: country.upper() for country, code in country_code.items() if code < 66}

# Handling missing keys with setdefault
import sys
import re

WORD_RE = re.compile('\w+')

index = {}
with open(sys.argv[0], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences
for word in sorted(index, key=str.upper):
    print(word, index[word])

import collections

index = collections.defaultdict(list)
with open(sys.argv[0], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index[word].append(location)
for word in sorted(index, key=str.upper):
    print(word, index[word])


# The __missing__ method
# test for item retrieval using `d[key]` notation::

class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


# Variations of dict
ct = collections.Counter('asdfsfdaasdsf')
ct.update('aaaaxxxx')
ct
ct.most_common(2)


class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item

# Immutable mappings
from types import MappingProxyType
d = {1:'A'}
d_proxy = MappingProxyType(d)
d_proxy
d_proxy[1]
d_proxy[2] = 'x'
d[2] = 'B'
d_proxy
d_proxy[2]

# Set theory

s = {1}
type(s)
s
s.pop()
s

s = {1,2,3}
s = set([1,2,3])

from dis import dis
dis('{1}')
dis('set([1])')

frozenset(range(10))
from unicodedata import name
{chr(i) for i in range(32,256) if 'SIGN' in name(chr(i),'')}
len(format(sys.maxsize,'b'))

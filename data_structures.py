# -*- coding:utf-8 -*-

import collections
import dis
import sys
import bisect
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])

# Example 2-9. Defining and using a named tuple type
City = collections.namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
tokyo[1]
City._fields
LatLong = collections.namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
delhi._asdict()
for key, value in delhi._asdict().items():
    print(key + ':', value)

# slice
s = 'bicycle'
s[::3]
s[::-1]

invoice = """
0.....6.................................40........52...55........
1909 Pimoroni PiBrella $17.50 3 $52.50
1489 6mm Tactile Switch x20 $4.95 2 $9.90
1510 Panavise Jr. - PV-201 $28.00 1 $28.00
1601 PiTFT Mini Kit 320x240 $34.95 1 $34.95
"""

SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)

line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])

# assigning to slicing
l = list(range(10))
del l[5:7]

board = [['_'] * 3 for i in range(3)]
board[1][2] = 'X'

weird_board = [['_'] * 3] * 3

l = [1, 2, 3]
id(l)
l *= 2
id(l)
t = (1, 2, 3)
id(t)
t *= 3
id(t)

# A += assignment puzzler
t = (1, 2, [30, 40])
t[2] += [50, 60]

dis.dis('s[a] += b')

# list.sort and the sorted built-in function
fruits = ['grape', 'raspberry', 'apple', 'banana']
sorted(fruits)
sorted(fruits, reverse=True)
sorted(fruits, key=len)
sorted(fruits, key=len, reverse=True)
fruits
fruits.sort()
fruits

# Managing ordered sequences with bisect
HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))


if __name__ == '__main__':
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect
    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)


def grade(score, brakepoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(brakepoints, score)
    return grades[i]

[grade(score) for score in [33, 99, 70, 77, 89, 90, 100]]

# Inserting with bisect.insort
SIZE = 7
random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list,new_item)
    print('%2d ->' % new_item,my_list)

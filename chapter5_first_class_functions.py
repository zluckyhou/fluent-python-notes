# -*- coding:utf-8 -*-
from functools import reduce


def factorial(n):
    '''returns n! '''
    return 1 if n < 2 else n * factorial(n - 1)


factorial(42)
factorial.__doc__
type(factorial)
fact = factorial
fact
fact(5)
map(fact, range(11))
list(map(fact, range(11)))

# high-order function
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
sorted(fruits, key=len)


def reverse(word):
    return word[::-1]


reverse('testing')

sorted(fruits, key=reverse)


def last(word):
    return word[-1]


sorted(fruits, key=last)

list(filter(lambda n: n % 2, range(6)))
list(map(factorial, filter(lambda n: n % 2, range(6))))
[factorial(n) for n in range(6) if n % 2]

from operator import add

reduce(add, range(100))
sum(range(100))
reduce(lambda x, y: x + y, range(100))

import random


class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self, *args, **kwargs):
        return self.pick()


bingo = BingoCage(range(3))
bingo.pick()
callable(bingo)

# -*- coding:utf-8 -*-
import operator
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


# annotations
def clip(text: str, max_len: 'int > 0' = 80) -> str:
    '''
    在max_len前面或后面的第一个空格处截断文本
    :param text:
    :param max_len:
    :return:
    '''
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:  # 没找到空格
        end = len(text)
    return text[:end].rstrip()


clip.__annotations__

from inspect import signature
sig = signature(clip)
sig.return_annotation
for param in sig.parameters.values():
    note = repr(param.annotation).ljust(13)
    print(note,':',param.name,'=',param.default)

from functools import reduce
def fact(n):
    return reduce(lambda a,b:a*b,range(1,n+1))
# fact(5)

from operator import mul
def fact(n):
    return reduce(mul,range(1,n+1))

metro_data = [
    ('Tokyo','JP',36.933,(35.343,139.2222)),
    ('Delhi NCR','IN',21.923,(28.323,77.20888)),
    ('Mexico City','MX',20.142,(19.2343,-99.234234)),
    ('New York-Newark','US',20.1333,(40.23423,-74.3435)),
    ('Sao Paulo','BR',10.464,(-23.533,-46.232))
]

from operator import itemgetter
for city in sorted(metro_data,key=itemgetter(1)):
    print(city)

cc_name = itemgetter(1,0)
for city in metro_data:
    print(cc_name(city))

from collections import namedtuple
LatLong = namedtuple('LatLong','lat long')
Metropolis = namedtuple('Metropolis','name cc pop coord')
metro_areas = [Metropolis(name,cc,pop,LatLong(lat,long)) for name,cc,pop,(lat,long) in metro_data]
metro_areas[0]
metro_areas[0].coord.lat

from operator import attrgetter
name_lat = attrgetter('name','coord.lat')
for city in sorted(metro_areas,key=attrgetter('coord.lat')):
    print(name_lat(city))

[name for name in dir(operator) if not name.startswith('_')]

from operator import methodcaller
s = 'the time has come'
upcase = methodcaller('upper')
upcase(s)
hiphenate = methodcaller('replace',' ','-')
hiphenate(s)
str.upper(s)
str.replace(s,' ','-')

from operator import mul
from functools import partial
triple = partial(mul,3)
triple(7)
list(map(triple,range(1,10)))
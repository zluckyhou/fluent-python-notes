# -*- coding:utf-8 -*-
import array
import os

cafe = bytes('cafe', encoding='utf_8')
cafe
cafe[0]
cafe[:1]
cafe_arr = bytearray(cafe)
cafe_arr
cafe_arr[-1:]
cafe_arr[0]

bytes.fromhex('31 4B CE A9').decode()
numbers = array.array('h', [-2, -1, 0, 1, 2])
octets = bytes(numbers)
octets

import struct

fmt = '<3s3sHH'
with open('TakachihoGorge.png', 'rb') as fp:
    img = memoryview(fp.read())
header = img[:10]
bytes(header)
struct.unpack(fmt, header)

bytes('A'.encode())

with open('cafe.txt','w',encoding='utf_8') as f:
    f.write('cafe')
with open('cafe.txt') as f:
    r = f.read()

os.stat('cafe.txt')




#!/usr/bin/env python3

from Crypto.Util.number import *
from secret import x, y, flag

print(f'x*y + 37*x + 13*y = {x*y + 37*x + 13*y}')

m = bytes_to_long(flag)
c = pow(m, 31337, x * y)

print(f'c = {c}')
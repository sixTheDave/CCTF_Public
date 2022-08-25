#!/usr/bin/env sage

from Crypto.Util.number import *
from secret import x, liar, flag

p = 2 ** 160 - 229233
E = EllipticCurve(GF(p), [313, 110])

m = bytes_to_long(flag.lstrip(b'CCTF{').rstrip(b'}'))
assert m < p

P = E((x, 348211368764139637940513065884307924565894663368))

Q = m * P
print(f'Q = ({Q.xy()[0]}, ?)')

for _ in liar:
	a, b = _
	print(f'{a} * P + {b} * Q = {(a*P + b*Q).xy()}')
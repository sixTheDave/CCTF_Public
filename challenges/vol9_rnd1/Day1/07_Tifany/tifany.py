#!/usr/bin/env python3

from Crypto.Util.number import *
from secret import PUBKEYS, flag

def keygen(nbit, k): # Public key generation function
	while True:
		p, q = [2 ** k * getRandomNBitInteger(nbit - k) + 1 for _ in '01']
		if isPrime(p) and isPrime(q):
			while True:
				y = getRandomRange(2, p * q)
				if pow(y, (p - 1) // 2, p) == p - 1 and pow(y, (q - 1) // 2, q) == q - 1:
					pubkey = k, p * q, y
					return pubkey

def encrypt(pubkey, m):
	k, n, y = pubkey
	assert k >= len(bin(m)[2:])
	x = getRandomRange(2, n)
	return pow(y, m, n) * pow(x, 2 ** k, n) % n

flag = flag.lstrip(b'CCTF{').rstrip(b'}')
flag = [bytes_to_long(flag[i*8:i*8 + 8]) for i in range(4)]
print(f'PUBKEYS = {PUBKEYS}')

ENC = [encrypt(PUBKEYS[_], flag[_]) for _ in range(4)]
print(f'ENC = {ENC}')
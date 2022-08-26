#!/usr/bin/env sage

from Crypto.Util.number import *
from random import *
from flag import flag


def keygen(nbit, l):
	p = getPrime(nbit)
	pubkey = []
	for _ in range(l):
		r, s = getPrime(nbit), getPrime(nbit >> 1)
		pubkey.append(r * p + s)
	return p, pubkey

def encrypt(msg, pubkey, size, nbit):
	bmsg = bin(bytes_to_long(msg))[2:]
	ENC, ERR = [], [getRandomNBitInteger(nbit >> 2) for _ in range(len(pubkey))]
	I = [[getRandomRange(0, l) for _ in range(size)] for _ in range(len(bmsg))]
	J = I.copy()
	shuffle(J)
	for i in range(len(bmsg)):
		BSE = [pubkey[_] for _ in I[i]]
		NSE = [ERR[_]  for _ in J[i]]
		ENC.append((p - 1337) * sum(BSE) + 31337 * sum(NSE) + int(bmsg[i]))
	return ENC

nbit, l, size = 128, 19, 5

p, pubkey = keygen(nbit, l)
ENC = encrypt(flag, pubkey, size, nbit)
print(f'p = SECRET')
print(f'pubkey = CENSORED')
print(f'ENC = {ENC}')
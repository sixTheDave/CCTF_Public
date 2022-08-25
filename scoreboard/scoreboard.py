#!/usr/bin/env python3

# This scoreboard is a community contribution by Robin Jadoul. Thank you!

import collections, pickle
import rich.console, rich.table
from pwn import *
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware
import eth_account, eth_abi
import pprint, time, json, shutil, os
import requests

web3 = Web3(HTTPProvider("https://polygon-rpc.com/"))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

GAME_CONTRACT = "0x36A1424DA63a50627863d8f65C0669da7347814A"
GAME = web3.eth.contract(GAME_CONTRACT, abi=json.load(open("game_abi.json")))

known_addresses = {
        #"address": "username", # Fill it if you want to see the names
}

#############################################################

BLOCK_START = 32265959
BLOCK_END = web3.eth.block_number
BLOCK_RANGE = 10000
if os.path.exists("scoreboard.pkl"):
    with open("scoreboard.pkl", "rb") as f:
        seenEvents = pickle.load(f)
else:
    seenEvents = {}

def iterEvents(ev):
    name = ev.event_name
    known, start = seenEvents.get(name, ([], BLOCK_START))

    yield from known
    for i in range(start, BLOCK_END + 1, BLOCK_RANGE):
        res = ev.getLogs(fromBlock=hex(i), toBlock=hex(i + BLOCK_RANGE))
        known += list(res)
        yield from res

    seenEvents[name] = (known, BLOCK_END)
    with open("scoreboard.pkl", "wb") as f:
        pickle.dump(seenEvents, f)

def main():
    con = rich.console.Console()

    allchals = []
    solves = collections.defaultdict(lambda: collections.defaultdict(lambda: False))

    for chal in iterEvents(GAME.events.FlagAdded):
        chal = (chal["args"]["flagId"], GAME.caller.flags(chal["args"]["flagId"])[3])
        allchals.append(chal)

    for solve in iterEvents(GAME.events.FlagSolved):
        solver, chal = solve["args"]["solver"], solve["args"]["flagId"]
        solves[solver][chal] = True

    board = [(solver if solver not in known_addresses else f"[bold cyan]{known_addresses[solver]}", str(GAME.caller.getPlayerPoints(solver))) + tuple(["[bold red]:x:", "[bold green]:heavy_check_mark:"][solved[c[0]]] for c in allchals) for solver, solved in solves.items()]

    allchals.sort()
    board.sort(key = lambda e: (int(e[1]), e[0]), reverse=True)

    tab = rich.table.Table("Rank", "User", "Score", *[c[1] for c in allchals], title="Scoreboard")
    for i, b in enumerate(board, 1):
        tab.add_row(str(i), *b)
    con.print(tab)

if __name__ == "__main__":
    main()

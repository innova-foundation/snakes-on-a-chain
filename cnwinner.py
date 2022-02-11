#thank you kawaiicrypto for how to do this
#show collateralnode winners from a block height range based on finding type: pubkeyhash in txid
from innovarpc.authproxy import AuthServiceProxy, JSONRPCException
import requests, urllib, json
import sys
rpc = AuthServiceProxy("http://%s:%s@127.0.0.1:14531"%("rpcuser", "rpcpassword"))

block_hash = rpc.getbestblockhash()
block = rpc.getblock(block_hash)
def get_cn_winner(blockheight):
    block = rpc.getblockbynumber(blockheight)
    winner = None
    for txid in block['tx']:
        tx = rpc.getrawtransaction(txid, 1)

        if 'proof-of-work' in block['flags'] and 'coinbase' in tx['vin'][0]:
            winner = sorted(tx['vout'], key = lambda x: x['value'])[0]['scriptPubKey']['addresses'][0]
        elif tx['vout'][0]['value'] == 0.0 and not 'coinbase' in tx['vin'][0]:
            winner = filter(lambda x: x['scriptPubKey']['type'] == 'pubkeyhash', tx['vout'])[0]['scriptPubKey']['addresses'][0]

        if winner:
            break

    return winner

for height in range(1524048, 1524058):
    print 'Winner of block {:d} is {winner}'.format(height, winner=get_cn_winner(height))

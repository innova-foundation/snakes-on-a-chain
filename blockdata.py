from innovarpc.authproxy import AuthServiceProxy, JSONRPCException

# rpc_user and rpc_password are set in the innova.conf file
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:14531"%("rpcuser", "rpcpassword"))
get_collateralnode_info = rpc_connection.collateralnode('list', 'full')
print(get_collateralnode_info)

def main():
  import time
  last_block = -1
  last_epoch = 0
  while True:
# get latest block count
    block = rpc_connection.getblockcount()
# get latest blockchain info, latest blackhash
    getblockhash = rpc_connection.getblockchaininfo()
    bestblockhash = getblockhash['bestblockhash']
    moneysupply = getblockhash['moneysupply']
# put blockhash from latest block and get extra info
    getblockhashinfo = rpc_connection.getblock(bestblockhash)
    blockhashinfowork = getblockhashinfo['flags']
    blockhashinfotime = getblockhashinfo['time']
    difference = blockhashinfotime - last_epoch
# collateralnode info
    collateralnodeinfo = rpc_connection.collateralnode('count')
    collateralnodecount = collateralnodeinfo

    if block != last_block:
      print "latest block:", (block)
      print "epoch:", (blockhashinfotime)
      print "converted time:", (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(blockhashinfotime)))
      print "bestblockhash:", (bestblockhash)
      print "Type of Work:", (blockhashinfowork)
      print "circulating:", (moneysupply)
      print "Collateralnodes:", (collateralnodecount)
      print "last block delta:", (difference), " seconds"
      last_block = block
      last_epoch = blockhashinfotime
    time.sleep(1)

main()

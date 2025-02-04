from innovarpc.authproxy import AuthServiceProxy, JSONRPCException

import time
import sys
import datetime
import urllib
import json
from influxdb import InfluxDBClient

# rpc_user and rpc_password are set in the innova.conf file
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:14531"%("rpcuser", "rpcpassword"))

#test
blocktest = rpc_connection.getblockcount()
print(blocktest)

#for i in range(3):
#    print(i)
#    block = rpc_connection.getblockbynumber(i)
#    print(block)


# Configure InfluxDB connection variables
host = "127.0.0.1" # My Ubuntu NUC
port = 8086 # default port
user = "admin" # the user/password with write access
password = "admin" 
dbname = "blocks" # the database we created earlier
interval = 60 # Sample period in seconds

# Create the InfluxDB client object
client = InfluxDBClient(host, port, user, password, dbname)

# think of measurement as a SQL table, it's not...but...
measurement = "measurement"
# location will be used as a grouping tag later
blockchain = "innova"

# Run until you get a ctrl^c
#def main():
import time
#for i in range(2499428, 2499437):
#    print(i)
blockcount = rpc_connection.getblockcount()
block = rpc_connection.getblockbynumber(blockcount)
grafanatime = block['time'] * 1000000000
hash = block['hash']
size = block['size']
height = block['height']
version = block['version']
merkleroot = block['merkleroot']
mint = int(block['mint'])
timed = block['time']
nonce = block['nonce']
bits = block['bits']
difficulty = float(block['difficulty'])
blocktrust = block['blocktrust']
chaintrust = block['chaintrust']
chainwork = block['chainwork']
previousblockhash = block['previousblockhash']
#nextblockhash = block['nextblockhash']
flags = block['flags']
proofhash = block['proofhash']
entropybit = block['entropybit']
modifier = block['modifier']
modifierchecksum = block['modifierchecksum']

data = [
  {
      "measurement": measurement,
          "tags": {
              "blockchain": blockchain,
          },
          "time": grafanatime,
          "fields": {
             #"block" : i,
              "hash" : hash,
              "size" : size,
	      "height" : height,
	      "version" : version,
	      "merkleroot" : merkleroot,
              "mint" : mint,
	      "time" : timed,
	      "nonce" : nonce,
	      "bits" : bits,
	      "difficulty" : difficulty,
	      "blocktrust" : blocktrust,
	      "chaintrust" : chaintrust,
	      "chainwork" : chainwork,
#	      "nextblockhash" : nextblockhash,
	      "flags" : flags,
	      "proofhash" : proofhash,
	      "entropybit" : entropybit,
	      "modifier" : modifier,
	      "modifierchecksum" : modifierchecksum
              }
          }
        ]
    # Send the JSON data to InfluxDB
print(difficulty)
client.write_points(data)

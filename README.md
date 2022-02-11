# snakes-on-a-chain
![Imgur Image](https://camo.githubusercontent.com/2b8284e38ddc67db8a01cc2027dc4f65d3c78e4e220d9668a47ec1526510f7e3/68747470733a2f2f692e696d6775722e636f6d2f5a6f30757a77392e706e67)

Innova Python RPC Daemon scripts  
For python innova RPC use https://github.com/innova-foundation/python-innovarpc  
sample site using grafana and influxdb https://innova.pro  
guide to setting up Innova Python RPC, influxdb, grafana and putting current block height in the dashboard.  
https://blockforums.org/topic/334-crypto-stats-using-grafana-influxdb-innova-daemon/  
guide to setting up to read Coingecko API  
https://blockforums.org/topic/377-setting-up-grafana-and-influxdb-docker-containers-and-showing-some-apis-stats/

#### python blockcount.py  
```
1882413
('latest block ', 1882413)
('latest block ', 1882414)
('latest block ', 1882415)
```
#### python blockdata.py  
```
latest block: 1882408
epoch: 1644602624
converted time: 2022-02-11 13:03:44
bestblockhash: f8f9b7ba22c2994fbaca72d986f0134aa1b3244ee66a39f15969bc415f78035a
Type of Work: proof-of-stake
circulating: 7575018.76210423
Collateralnodes: 21
last block delta: 1644602624  seconds
latest block: 1882410
epoch: 1644602790
converted time: 2022-02-11 13:06:30
bestblockhash: 486fe5e3c261887d1798c653b0a00e8b4b53e7220981203b00848f18da77f15f
Type of Work: proof-of-stake
circulating: 7575019.33465217
Collateralnodes: 21
last block delta: 35  seconds
latest block: 1882411
epoch: 1644602852
converted time: 2022-02-11 13:07:32
bestblockhash: a853b476c44f71bcb6f5dac665c25aed31eef09658dc70de50853ff76b4f9af9
Type of Work: proof-of-stake
circulating: 7575019.77372066
Collateralnodes: 21
last block delta: 24  seconds
```  
#### python cnwinner.py  
```
Winner of block 1882401 is iBxkgPucWhSz6ARbejRwznD3RMNur3BGQD
Winner of block 1882402 is iSM8P3ibwu6a5KK29GCQubsBTkScKNDHYc
Winner of block 1882403 is iEPTABUiwoEmxeBUgiAicqUrha1ev9wFvv
Winner of block 1882404 is iEPTABUiwoEmxeBUgiAicqUrha1ev9wFvv
Winner of block 1882405 is iAt1YJprLBKcYDvmosraGJoJrJVTGKX1EC
Winner of block 1882406 is iAt1YJprLBKcYDvmosraGJoJrJVTGKX1EC
Winner of block 1882407 is iJvNJANUWTY2cgBpfMPK3f2EQ6QCMFywAp
```
#### Docker Setup
Create a data directory and also a userid to use for the grafana Docker container  
```
mkdir data # creates a folder for your data
ID=$(id -u) # saves your user id in the ID variable
```
Docker run command with some environmental variables  
```
docker run -d \
-p 3000:3000 \
--name=grafana \
--user $ID \
--volume "$PWD/data:/var/lib/grafana" \
-e "GF_INSTALL_PLUGINS=grafana-worldmap-panel" \
-e "GF_USERS_VIEWERS_CAN_EDIT=false" \
-e "GF_USERS_EDITORS_CAN_ADMIN=false" \
-e "GF_USERS_ALLOW_SIGN_UP=false" \
-e "GF_USERS_ALLOW_ORG_CREATE=false" \
-e "GF_AUTH_DISABLE_LOGIN_FORM=false" \
-e "GF_AUTH_ANONYMOUS_ENABLED=true" \
-e "GF_AUTH_ANONYMOUS_ORG_ROLE=Viewer" \
-e "GF_ANALYTICS_GOOGLE_ANALYTICS_UA_ID=UA-157676508-1" \
-e "GF_SERVER_DOMAIN=innova.pro" \
grafana/grafana
```
Check this is up by going to your IP:3000  
Docker run command  
```
--name="influxdb" \
-p 8086:8086 \
-v /home/USERNAME/influxdb:/var/lib/influxdb \
influxdb -config /etc/influxdb/influxdb.conf
```
To get into influxdb Docker container
```
docker exec -it influxdb /bin/bash
```
To get into influx cli  
```
influx
```
then run commands like  
```
show databases
create database stats
drop database stats
```
Check its all working  
```
docker stop grafana
docker stop influxdb
docker start grafana
docker start influxdb
docker stop grafana
docker rm grafana
rerun the full grafana run command
```

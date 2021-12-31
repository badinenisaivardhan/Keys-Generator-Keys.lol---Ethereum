import blocksmith
import sys
import json
keysperpage = 128
totalpages= 904625697166532776746648320380374280100293470930272690489102837043110636675
keys = {}
pagenumber= int(sys.argv[1])
basepage = pagenumber-1
firstseed= basepage*keysperpage
for j in range(firstseed,firstseed+keysperpage-1):
  privatekey = '{:064x}'.format(j+1)
  publickey = str(blocksmith.EthereumWallet.generate_address(privatekey))
  keys[publickey]=privatekey
print(json.dumps(keys))

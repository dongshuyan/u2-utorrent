import time
import requests
import bencodepy
import bencode
import copy

# Example: If the path is "C:\Users\Admin\utorrent\resume.dat", put "C:\\Users\\Admin\\utorrent\\"
# Double back slash is import because \r is carriage return
# For linux/MacOS user please modify the path correspondingly
path = "C:\\Users\\Admin\\Desktop\\utorrent\\"
API = ""
wait = 2

jdata = {
	"jsonrpc": "2.0",
	"method": "query",
	"params": "96E66669C60AEA8ACD244576E04FCE883B4A7C48",
	"id": 1
  }

with open(path + "resume.dat", 'rb') as f:
    file = f.read()
    data = bencode.bdecode(file)
    ndata = copy.deepcopy(data)
    for key in data:
        if key == '.fileguard':
            continue
        else:
            filename = str(key)
            d = data[key]
            tracker = str(d['trackers'])
            if tracker[:26] == "['http://tracker.dmhy.org/":
                info = str(d['info'].hex())
                jdata["params"] = info
                print(jdata["params"])
                r = requests.post(API, json=jdata)
                time.sleep(wait)
                newkey = r.json()['result']
                newtracker = ["https://tracker.dmhy.org/announce?secure=" + newkey]
                ndata[key]['trackers'] = newtracker
#                 time.sleep(1)
                print("filename=" + filename)
                print(newtracker)
    with open(path + "resume_new.dat", 'wb') as nf:
        nf.write(bencode.bencode(ndata))

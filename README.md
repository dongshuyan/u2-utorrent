# u2-utorrent
To update U2 securekey

++Backup your files first++
Tested with python 3.7.6 (anaconda) and uTorrent 2.2.1 (build 25110)

Dependency: https://github.com/tomster/BitTorrent-bencode. Use pip install BitTorrent-bencode==5.0.8.1

# Parts need to be changed in code
1. Path for "resume.dat".
2. User's API
3. Wait time, which depends on the local network speed. I used 2s which worked.

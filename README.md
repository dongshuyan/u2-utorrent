# u2-utorrent
To update U2 securekey and set the tracker to HTTPS

**Backup your files first**

Tested with python 3.7.6 (anaconda) and uTorrent 2.2.1 (build 25110)

Dependency: bencode.py 4.0.0. https://github.com/fuzeman/bencode.py Use `pip install bencode.py`

# Parts need to be changed in code
1. Path for "resume.dat".
2. User's API
3. Wait time, which depends on the local network speed. I used 2s which worked.

After making these changes, run by `python Tracker.py`

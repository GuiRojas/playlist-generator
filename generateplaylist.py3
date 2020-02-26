#!/usr/bin/python
import sys
import os
import os.path

dir = "./"
if (len(sys.argv) >= 2):
	dir = str(sys.argv[1])
#print("creating playlist for" + dir)
ext = [".flac", ".mp3"]
arq = open(dir + "playlist.txt","w")
for dirpath, dirnames, filenames in os.walk(dir):
    for filename in [f for f in filenames if (f.endswith(tuple(ext)))]:
        #print(os.path.join(dirpath, filename))
        arq.write(os.path.join(dirpath, filename + "\n"))
arq.close()
arq = open(dir + "playlist.sh","w")
arq.write("mpv --playlist=playlist.txt --no-audio-display")
arq.close()
os.chmod(dir + "playlist.sh", 0o755)
import sys
import re
import subprocess
import os
import time

if len(sys.argv) != 4:
    print("Usage: " + sys.argv[0] + " [filelist] [source file] [destination folder]")
    exit(1)

if not os.path.exists(sys.argv[1]):
    print("Source file does not exist")
    exit(1)

def timeslice(a, b):
    b = [int(b) for b in re.findall("(\d+)", b)]
    a = [int(a) for a in re.findall("(\d+)", a)]
    c = [v[0] - v[1] for v in zip(b, a)]
    for x in range(len(c)):
        if x == 0:
            if c[0] < 0:
                print("badly formatted timestamps")
                return -1
        elif x == 1 or x == 2:
            if c[x] < 0:
                c[x - 1] = c[x - 1] - 1
                c[x] = c[x] + 60
        elif x == 3:
            if c[x] < 0:
                c[x - 1] = c[x - 1] - 1
                c[x] = c[x] + 999
    return ':'.join([str(j) for j in c[0:3]]) + '.' + str(c[3])


f = open(sys.argv[1])
subfolders = f.read().split('\n\n')
subfolders = [g.split('\n') for g in subfolders ]
for x in subfolders:
    fold = sys.argv[3] + x[0]
    if not os.path.exists(fold):
        os.makedirs(fold)
    for j in x[1:]:
        times = j.split(' ')
        times = [k for k in times if k != '']
        if len(times) != 2:
            continue
        offset = timeslice(times[0], times[1])
        if offset == -1:
            print('times for: ' + times + ' are misordered')
            continue
        subprocess.run(['ffmpeg', '-ss', times[0], '-to', times[1], '-i', sys.argv[2], '-c', 'copy', '-force_key_frames', times[0] + ',' + times[1], '-async', '-1', fold + '/' + str(time.time()) + '.mp4'])

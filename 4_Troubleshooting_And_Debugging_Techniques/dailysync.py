#!/usr/bin/env python
import subprocess
import os
from multiprocessing import Pool
import re


def run(src):
    dest = re.sub(r'/prod/', r'/prod_backup/', src)
    print(src)
    print(dest)
    subprocess.call(["rsync", "-arq", src, dest])


tree = os.walk('/home/student-00-ffe2712a982a/data/prod/')

dir_src = []

for address, dirs, files in tree:
    print(address, dirs)
    for direc in dirs:
        dir_src.append(os.path.join(address, direc))
    break

print(dir_src)
p = Pool(len(dir_src))
p.map(run, dir_src)

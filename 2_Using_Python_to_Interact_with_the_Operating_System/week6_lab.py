#!/usr/bin/env python3

import sys
import subprocess

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        filename = line.split('/')[-1]
        updated_line = line.replace('jane', 'jdoe')
        print(line)
        print(updated_line)
        subprocess.run(['mv', line, updated_line])

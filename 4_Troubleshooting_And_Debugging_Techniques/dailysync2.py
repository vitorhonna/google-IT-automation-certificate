#!/usr/bin/env python3
from multiprocessing import Pool
from functools import partial
import os
import subprocess

src = "./data/prod/"
dest = "./data/prod_backup/"


def run_bk(cwd, curr_src):
    '''Backs up the specified file/subfolder from src to dest'''
    origin = "{}/{}".format(cwd, curr_src)
    destination = cwd.replace(src, dest)
    print("  -- "+curr_src+" -> "+destination)
    subprocess.call(["rsync", "-zaq", origin, destination])


def main():
    '''Walks through the file tree and backsup all files/folders in every subfolder in different processes'''
    for root, dirs, files in os.walk(src):
        print("\nWorking dir: {}".format(root))
        if len(files) > 0:
            pool = Pool(len(files))
            pool.map(partial(run_bk, root), files)
            print("Backed up {} files".format(len(files)))
        if len(dirs) > 0:
            pool = Pool(len(dirs))
            pool.map(partial(run_bk, root), dirs)
            print("Processing {} dirs".format(len(dirs)))


main()

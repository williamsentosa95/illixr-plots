#!/usr/bin/env python
# -*- mode: python; coding: utf-8; fill-column: 80; -*-
#

"""
get_ate.py
Retrieve absoulte trajectory error from folders.
"""

import argparse
import codecs
import gzip
import io
import json
import numpy as np
import os
import sys
from os import listdir
from os.path import isfile, join, isdir
import subprocess


def main(args):
    folder_path = args[0];

    if (not os.path.isdir(folder_path)):
        print(folder_path + " does not exist!")
        return

    exp_folders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
    exp_folders.sort()

    line_num = 0
    compression_ratios = []

    for exp_folder_name in exp_folders:
        exp_folder_path = folder_path + "/" + exp_folder_name
        compression_info_file = exp_folder_path + "/compression_info.csv"

        if (os.path.isfile(compression_info_file)):
            files = open(compression_info_file, "r")
            for line in files.readlines():
                if (line_num > 0):
                    splits = line.split(",")
                    compression_ratios.append(float(splits[0]))
                line_num += 1

        print("%s\t%f" % (exp_folder_name, np.mean(compression_ratios)))
        compression_ratios = []
        line_num = 0 

            

        

if __name__ == '__main__':
    prog = sys.argv[0]
    num_args = len(sys.argv)

    if (num_args < 2):
        sys.stderr.write((u"Usage: %s" +
                          u" <folder-path>\n") %
                         (prog))
        sys.exit(1)

    args = sys.argv[1:]
    main(args)

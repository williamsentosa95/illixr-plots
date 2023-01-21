#!/usr/bin/env python
# -*- mode: python; coding: utf-8; fill-column: 80; -*-
#

"""
get_are.py
Retrieve absoulte rotational error from folders.
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
    pose_baseline_path = args[1];

    if (not os.path.isdir(folder_path)):
        print(folder_path + " does not exist!")
        return

    if (not os.path.isfile(pose_baseline_path)):
        print(pose_baseline_path + "does not exist!")
        return

    exp_folders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
    exp_folders.sort()

    for exp_folder_name in exp_folders:
        exp_folder_path = folder_path + "/" + exp_folder_name
        pose_file = exp_folder_path + "/pred_pose.csv"

        if (os.path.isfile(pose_file)):
            # evo_ape euroc $HOME/ILLIXR-dev/data-log/latency-hard/rtt-0ms/pred_pose.csv pred_pose_hard.tum -as -p --plot_mode xyz
            cmd = ["evo_ape", "euroc"]
            cmd.append(pose_file)
            cmd.append(pose_baseline_path)
            cmd = cmd + ["-as", "--pose_relation", "angle_deg"]
            output = subprocess.check_output(cmd).decode("utf-8")
            for line in output.split("\n"):
                if ("mean") in line:
                    mean_error = float(line.split("\t")[1])
                    break
            print("%s\t%f" % (exp_folder_name, mean_error))
            
        

if __name__ == '__main__':
    prog = sys.argv[0]
    num_args = len(sys.argv)

    if (num_args < 3):
        sys.stderr.write((u"Usage: %s" +
                          u" <folder-path> <pose_baseline_path>\n") %
                         (prog))
        sys.exit(1)

    args = sys.argv[1:]
    main(args)

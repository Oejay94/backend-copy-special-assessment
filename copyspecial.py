#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse
import sys
import commands
# This is to help coaches and graders identify student assignments
__author__ = "Joey Brown ft. Google and Coaches"


def get_special_paths(dir):
    file_list = []
    for dir_path, _, filenames in os.walk(dir):
        for f in filenames:
            if re.search(r'__\w+__', f):
                file_list.append(os.path.abspath(os.path.join(dir_path, f)))
                print(os.path.abspath(os.path.join(dir_path, f)) + '\n')
        break
    return file_list


def copy_to(paths, dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    for path in paths:
        shutil.copy(path, dir)


def zip_to(paths, zip_path):
    cmd = ['zip', '-j']
    zip_path = [zip_path]
    command_list = cmd + zip_path + paths
    print("Command I'm going to do: ")
    print(''.join(command_list))
    try:
        subprocess.call(command_list)
    except:
        subprocess.check_output(command_list)


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO need an argument to pick up 'from_dir'
    parser.add_argument('dir', help='name of directory to search')
    args = parser.parse_args()

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    source_dir, to_dir, to_zip = args.dir, args.todir, args.tozip
    if source_dir:
        files_list = get_special_paths(source_dir)
    if source_dir and to_dir:
        copy_to(files_list, to_dir)
    if source_dir and to_zip:
        zip_to(files_list, to_zip)


if __name__ == "__main__":
    main()

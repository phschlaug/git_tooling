#!/usr/bin/env python
#!python
# -*- coding: utf-8 -*-

"""
Simply lists the difference between the two given branches
"""

import subprocess
import argparse

def compare_branches(repo_path, branch1, branch2):
    command = f"git -C {repo_path} diff --name-status {branch1} {branch2}"
    try:
        output = subprocess.check_output(command, shell=True, universal_newlines=True)
        
        added_files = []
        modified_files = []
        deleted_files = []

        for line in output.strip().split("\n"):
            status, file_path = line.split("\t")
            if status == "A":
                added_files.append(file_path)
            elif status == "M":
                modified_files.append(file_path)
            elif status == "D":
                deleted_files.append(file_path)
        
        print("Added files:")
        for file_path in added_files:
            print(file_path)

        print("\nModified files:")
        for file_path in modified_files:
            print(file_path)

        print("\nDeleted files:")
        for file_path in deleted_files:
            print(file_path)
    except subprocess.CalledProcessError as e:
        print("Error:", e)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='GIT Branch Differences',
        description='Lists the differences between the provided branches'
    )
    parser.add_argument('-p','--path', help='Specify the path to the git repository', required=True)
    parser.add_argument('-b','--base', help='Specify the base branch e.g. main', required=True)
    parser.add_argument('-r','--ref', help='Specify the reference branch e.g. feat/feature1', required=True)
    arguments = parser.parse_args()
    repo_path = arguments.path
    base_branch = arguments.base
    ref_branch = arguments.ref
    compare_branches(repo_path, base_branch, ref_branch)

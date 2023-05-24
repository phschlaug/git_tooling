#!/usr/bin/env python
#!python
# -*- coding: utf-8 -*-

"""
This script lists all the branches and calculates the age of each in days.
"""

import argparse
import time
import datetime
import git
from print_table import Table

DATE_FORMAT = "%Y-%m-%d"

class Branch:
    """
    Representation of a branch containing all the information
    """
    def __init__(self, name: str, date_latest_commit: str, author: str) -> None:
        self.name = name
        self.date_of_latest_commit = date_latest_commit
        self.author= author
        self.elapsed_time = self.__calculate_elapsed_days()

    def __calculate_elapsed_days(self) -> int:
        latest_date = datetime.datetime.fromtimestamp(self.date_of_latest_commit)
        diff = datetime.datetime.utcnow() - latest_date
        return diff.days


def analyze_branch(repository: git.Repo, name: str) -> Branch:
    """
    Fetches the latest commit to the branch and returns the information as custom class
    Parameters
    ------------
        repository: git.Repo
            The git repository from which the branches should be analyzed from
        name: str,
            The name of the branch which should be analyzed
    Return
    -----------
        branch : Branch
            Storing the information of the analyzed branch in a respective custom class
    """
    commits = []
    for commit in repository.iter_commits(rev=name):
        commits.append(commit)
    first_commit = commits[0]
    author = first_commit.author
    date_of_first_commit = first_commit.committed_date
    return Branch(name, date_of_first_commit, author)

def print_branch_information(list_of_branches):
    """
    Uses the library 'print_table' to print all the given branches to the console
    Parameters
    ------------
        list_of_branches: [Branch]
            List of branches where the information should be printed from
    """
    branch_table = Table(numberOfCols=4).head(
        ['Branch Name','Author', 'Date of latest Commit','Days old'])
    for branch in list_of_branches:
        branch_table.row([branch.name, branch.author,
        time.strftime(DATE_FORMAT, time.gmtime(branch.date_of_latest_commit)), branch.elapsed_time])
    branch_table.printTable()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='GIT Branch Age',
        description='Lists all branches and calculates the age in days'
    )
    parser.add_argument('-p','--path', help='Specify the path to the git repository', required=True)
    arguments = parser.parse_args()
    repo_path = arguments.path

    repo = git.Repo(repo_path)
    repository_branches = repo.remote().refs
    branches = []
    for repo_branch in repository_branches:
        info_about_branch = analyze_branch(repo, repo_branch)
        branches.append(info_about_branch)
    branches.sort(key=lambda b: b.elapsed_time, reverse=True)
    print_branch_information(branches)

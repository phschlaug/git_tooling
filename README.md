# Git Tooling

Scripts to get information about a git repository.

## How to get started

Simply execute the following commands:

```{bash}
git clone https://github.com/phschlaug/git_tooling.git
pip install -r requirements.txt
```

## Branch Ages

This script lists all the branches from the given git repository and calculates the age of it in days.
To do so it fetches the latest commit from each branch and checks how many days passes since that commit.

To use the script simply execute the following command

```{bash}
python branch_ages --p <path_to_git_repository>
```

## Branch Differences

This script returns a lust of added, modified and deleted files between the two provided files.

The following shows the usage of the script:

```{bash}
python branch_diff.py --p=<path_to_git_repository> --b=<base_branch> --ref=<reference_branch>
```

import subprocess
import pytest


BRANCH_NAME = "local-branch"
FILE_PATH = "Aufgabe01/test.txt"

def git_branch_exists(branch_name):
    """Return True if branch exists (local or remote)."""
    try:
        subprocess.run(
            ["git", "rev-parse", "--verify", branch_name],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return True
    except subprocess.CalledProcessError:
        return False


def file_exists_in_branch(branch_name, file_path):
    """
    Return True if file exists and is committed in the given branch.
    """
    try:
        result = subprocess.run(
            ["git", "ls-tree", "-r", "--name-only", branch_name, file_path],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True  # get stdout as string
        )
        # ls-tree outputs the file path if it exists
        return bool(result.stdout.strip())
    except subprocess.CalledProcessError:
        return False



def test_branch():
    assert git_branch_exists(BRANCH_NAME), f"Branch '{BRANCH_NAME}' does not exist"
def test_branch_file():
    assert file_exists_in_branch(BRANCH_NAME, FILE_PATH), (
        f"File '{FILE_PATH}' not found in branch '{BRANCH_NAME}'"
    )

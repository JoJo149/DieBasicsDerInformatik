import subprocess
from pathlib import Path

def get_git_root() -> Path:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=True
    )
    return Path(result.stdout.strip())

def run_solution_binary():
    """
    Run the compiled 'solution' binary and return its output.
    """

    binary_path = Path(get_git_root().__str__() + "/Aufgabe01/solution")  # replace with your binary name
    if not binary_path.is_file():
        raise FileNotFoundError(f"{binary_path} does not exist")

    result = subprocess.run(
        [str(binary_path)],   # run the binary
        check=True,                # raise exception if it exits with non-zero
        stdout=subprocess.PIPE,    # capture stdout
        stderr=subprocess.PIPE,    # capture stderr
        text=True                  # decode bytes to string
    )

    return result.stdout

def test_solution_output():
    output = run_solution_binary()
    assert output.startswith("Hallo, ") and output.endswith("!\n"),(
            f"Solution Binary does not print correctly"
    )


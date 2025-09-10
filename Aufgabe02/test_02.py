import math
import random
import subprocess
import shutil
import pathlib
import pytest
import ctypes
import sys

def get_compiler() -> str:
    for candidate in ["gcc", "clang", "cc"]:
        if shutil.which(candidate):
            return candidate
    raise RuntimeError("No C compiler found")


@pytest.fixture(scope="module")
def clib(tmp_path_factory):
    tmpdir = tmp_path_factory.mktemp("build")
    src = pathlib.Path(__file__).parent / "solution.c"

    # platform-specific shared library extension
    if sys.platform.startswith("linux"):
        libname = "solution.so"
    elif sys.platform == "darwin":
        libname = "solution.dylib"
    else:
        raise RuntimeError(f"Unsupported platform: {sys.platform}")

    compiler = get_compiler()
    libpath = tmpdir / libname

    compile_cmd = [compiler, "-shared", "-fPIC", "-o", str(libpath), str(src), "-lm"]
    subprocess.run(compile_cmd, check=True)

    lib = ctypes.CDLL(str(libpath))

    return lib

def py_is_prime(n: int) -> bool:
    if n <= 1:
        return False
    else:
        is_prime = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                is_prime = False
                break
        return  is_prime

def data_source(clib):
    clib.isPrime.argtypes = [ctypes.c_int]
    clib.isPrime.restype = ctypes.c_bool

    solution_array = [random.randint(-20, 5000) for _ in range(100)]
    c_code_array = solution_array.copy()
    map( lambda x: (x, py_is_prime(x)), solution_array)
    map( lambda x: (x, clib.isPrime(x)), c_code_array)
    for a, b in zip(solution_array, c_code_array):
        yield a, b


@pytest.mark.parametrize('a, b', data_source())
def test_is_prime_param(a, b):
    assert a == b, f"Mismatch for n={a[0]}"









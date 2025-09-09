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
def test_is_prime_param(clib):
    clib.isPrime.argtypes = [ctypes.c_int]
    clib.isPrime.restype = ctypes.c_bool

    for n in range(20):  # test 20 random numbers
        n = random.randint(-50, 2000)  # adjust range as needed
        c_result = clib.isPrime(n)
        py_result = py_is_prime(n)
        assert c_result == py_result, f"Mismatch for n={n}"








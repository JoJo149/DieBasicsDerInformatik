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
        return is_prime

def test_is_prime(clib):
    # ensure ctypes signature
    clib.isPrime.argtypes = [ctypes.c_int]
    clib.isPrime.restype = ctypes.c_bool

    # random numbers
    rnd = random.Random(0)
    nums = [rnd.randint(-20, 100) for _ in range(100)]

    # create the "arrays" using Python and the C library
    py_results = [py_is_prime(n) for n in nums]
    c_results = [bool(clib.isPrime(n)) for n in nums]

    # compare element-wise
    for n, py_res, c_res in zip(nums, py_results, c_results):
        assert py_res == c_res, f"Mismatch for n={n}: solution={py_res}, your answer={c_res}"








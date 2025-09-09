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


@pytest.mark.parametrize(
    "n,expected",
    [
        # small prime
        (2, True), (3, True), (5, True), (7, True), (11, True), (13, True),
        # Small composites
        (4, False), (6, False), (8, False), (9, False), (10, False),
        # Larger numbers
        (29, True), (97, True), (100, False), (121, False),
        # Edge cases
        (0, False), (1, False), (-5, False), (-2, False)
    ],
    ids=[
        "prime_2", "prime_3", "prime_5", "prime_7", "prime_11", "prime_13",
        "composite_4", "composite_6", "composite_8", "composite_9", "composite_10",
        "prime_29", "prime_97", "composite_100", "composite_121",
        "composite_0", "composite_1", "composite_-5", "composite_-2"
    ]
)
def test_is_prime_param(clib, n, expected):
    clib.isPrime.argtypes = [ctypes.c_int]
    clib.isPrime.restype = ctypes.c_bool
    assert clib.isPrime(n) == expected








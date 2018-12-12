# -*- coding: utf-8 -*-

"""
pythoncompat

Copied from requests
"""

import sys

# -------
# Pythons
# -------


PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3


# ---------
# Specifics
# ---------

if PY2:
    from .zipencrypt2 import _ZipEncrypter

    builtin_str = str
    bytes = str
    str = unicode
    basestring = basestring
    numeric_types = (int, long, float)

    def zip_encrypt(pwd):
        ze = _ZipEncrypter(pwd)
        return lambda x: b"".join(map(ze, x))

elif PY3:
    from .zipencrypt3 import _ZipEncrypter

    builtin_str = str
    str = str
    bytes = bytes
    basestring = (str, bytes)
    numeric_types = (int, float)

    def zip_encrypt(pwd):
        ze = _ZipEncrypter(pwd)
        return lambda x: bytes(map(ze, x))

try:
    from zipfile import ZIP64_VERSION
except ImportError:
    ZIP64_VERSION = 45

try:
    from zipfile import BZIP2_VERSION
except ImportError:
    BZIP2_VERSION = 46

try:
    from zipfile import ZIP_BZIP2
except ImportError:
    ZIP_BZIP2 = 12

try:
    from zipfile import LZMA_VERSION
except ImportError:
    LZMA_VERSION = 63

try:
    from zipfile import ZIP_LZMA
except ImportError:
    ZIP_LZMA = 14

try:
    from zipfile import ZIP_MAX_COMMENT
except ImportError:
    ZIP_MAX_COMMENT = (1 << 16) - 1


# Copy from io
SEEK_SET = 0  # start of the stream (the default); offset should be zero or positive
SEEK_CUR = 1  # current stream position; offset may be negative
SEEK_END = 2  # end of the stream; offset is usually negative

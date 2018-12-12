# This code is extracted from zipencrypt
# written by Jonathan Koch
# https://github.com/devthat/zipencrypt

from zipfile import _ZipDecrypter


class _ZipEncrypter(_ZipDecrypter):
    def __call__(self, c):
        """Encrypt a single character."""
        _c = ord(c)
        k = self.key2 | 2
        _c = _c ^ (((k * (k ^ 1)) >> 8) & 255)
        _c = chr(_c)
        self._UpdateKeys(c)  # this is the only line that actually changed
        return _c

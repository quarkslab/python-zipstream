# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import zipstream


class PointerIOTestCase(unittest.TestCase):
    def test_init_no_args(self):
        zipstream.PointerIO()

    def test_init_mode(self):
        try:
            zipstream.PointerIO('wb')
        except Exception as err:
            self.fail(err)

        for mode in ['w', 'r', 'rb', 'a', 'ab']:
            self.assertRaises(Exception, zipstream.PointerIO, mode=mode)

        for mode in ['w', 'wb''r', 'rb', 'a', 'ab']:
            self.assertRaises(Exception, zipstream.PointerIO, mode=mode + '+')

    def test_has_fileobj_attrs(self):
        fileobj = zipstream.PointerIO()

        self.assertTrue(hasattr(fileobj, 'write'))
        self.assertTrue(hasattr(fileobj, 'close'))
        self.assertTrue(hasattr(fileobj, 'tell'))

    def test_write_bytes(self):
        fileobj = zipstream.PointerIO()
        data = b'Im a little tea pot'
        try:
            fileobj.write(data)
        except Exception as err:
            self.fail(err)
        self.assertEqual(fileobj.tell(), 19)

    def test_write_unicode(self):
        fileobj = zipstream.PointerIO()
        data = 'Im a little tea pot'
        try:
            fileobj.write(data)
        except Exception as err:
            self.fail(err)
        self.assertEqual(fileobj.tell(), 19)


        fileobj = zipstream.PointerIO()
        data = '幋 儳鑤 寱懤擨 拻敁柧'
        try:
            fileobj.write(data)
        except Exception as err:
            self.fail(err)
        self.assertEqual(fileobj.tell(), 30)

    def test_write_non_string_type(self):
        fileobj = zipstream.PointerIO()
        data = None
        self.assertRaises(TypeError, fileobj.write, data)

        fileobj = zipstream.PointerIO()
        data = []
        self.assertRaises(TypeError, fileobj.write, data)

        fileobj = zipstream.PointerIO()
        data = tuple()
        self.assertRaises(TypeError, fileobj.write, data)

        fileobj = zipstream.PointerIO()
        data = 1
        self.assertRaises(TypeError, fileobj.write, data)

        fileobj = zipstream.PointerIO()
        data = 1.00
        self.assertRaises(TypeError, fileobj.write, data)

if __name__ == '__main__':
    unittest.main()
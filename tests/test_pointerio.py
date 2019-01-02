# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import enczipstream


class PointerIOTestCase(unittest.TestCase):
    def test_init_no_args(self):
        enczipstream.PointerIO()

    def test_init_mode(self):
        try:
            enczipstream.PointerIO('wb')
        except Exception as err:
            self.fail(err)

        for mode in ['w', 'r', 'rb', 'a', 'ab']:
            self.assertRaises(Exception, enczipstream.PointerIO, mode=mode)

        for mode in ['w', 'wb''r', 'rb', 'a', 'ab']:
            self.assertRaises(Exception, enczipstream.PointerIO,
                              mode=mode + '+')

    def test_has_fileobj_attrs(self):
        fileobj = enczipstream.PointerIO()

        self.assertTrue(hasattr(fileobj, 'write'))
        self.assertTrue(hasattr(fileobj, 'close'))
        self.assertTrue(hasattr(fileobj, 'tell'))

    def test_write_bytes(self):
        fileobj = enczipstream.PointerIO()
        data = b'Im a little tea pot'
        try:
            fileobj.write(data)
        except Exception as err:
            self.fail(err)
        self.assertEqual(fileobj.tell(), 19)

    def test_write_unicode(self):
        fileobj = enczipstream.PointerIO()
        data = 'Im a little tea pot'
        try:
            fileobj.write(data)
        except Exception as err:
            self.fail(err)
        self.assertEqual(fileobj.tell(), 19)

        fileobj = enczipstream.PointerIO()
        data = '幋 儳鑤 寱懤擨 拻敁柧'
        try:
            fileobj.write(data)
        except Exception as err:
            self.fail(err)
        self.assertEqual(fileobj.tell(), 30)

    def test_write_non_string_type(self):
        fileobj = enczipstream.PointerIO()
        data = None
        self.assertRaises(TypeError, fileobj.write, data)

        fileobj = enczipstream.PointerIO()
        data = []
        self.assertRaises(TypeError, fileobj.write, data)

        fileobj = enczipstream.PointerIO()
        data = tuple()
        self.assertRaises(TypeError, fileobj.write, data)

        fileobj = enczipstream.PointerIO()
        data = 1
        self.assertRaises(TypeError, fileobj.write, data)

        fileobj = enczipstream.PointerIO()
        data = 1.00
        self.assertRaises(TypeError, fileobj.write, data)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from cushead import main

# Total errors: 7

class TestApp(unittest.TestCase):
    # no arguments
    # Exception
    @classmethod
    def test_1(self):
        main([])

    # -file and -preset together
    # Exception
    @classmethod
    def test_2(self):
        main(['-file', './test/together/test.txt', '-preset', './test/together/foo.bar'])

    # argument passed with -file doesn't exists
    # Exception
    @classmethod
    def test_3(self):
        main(['-file', 'foo.bar'])

    # correct -file usage
    # Success
    @classmethod
    def test_4(self):
        main(['-file', './test/correct/test.txt'])

    # void index.html
    # Success
    @classmethod
    def test_5(self):
        main(['-file', './test/void_index/test.txt'])

    # index.html doesn't exists
    # Exception
    @classmethod
    def test_6(self):
        main(['-file', './test/miss_index/test.txt'])

    # all optional parameters
    # Success
    @classmethod
    def test_7(self):
        main(['-file', './test/options/test.txt',
            '--exclude-comment',
            '--exclude-html',
            '--exclude-config',
            '--exclude-seo',
            '--exclude-opengraph',
            '--exclude-facebook',
            '--exclude-twitter',
            '--exclude-opensearch',
            '--exclude-author'
            ])

    # correct -preset usage
    # Success
    @classmethod
    def test_8(self):
        main(['-preset', './test/foo.bar'])

    # file passed with -file doesn't have path key-value pair
    # Exception
    @classmethod
    def test_9(self):
        main(['-file', './test/miss_path/test.txt'])

    # file passed with -file only have path key-value pair
    # Success
    @classmethod
    def test_10(self):
        main(['-file', './test/only_path/test.txt'])

    # file passed with -file are void
    # Exception
    @classmethod
    def test_11(self):
        main(['-file', './test/miss_value_preset/test.txt'])

    # missing some key-value pairs
    # color, title, preview, description
    # Success
    @classmethod
    def test_12(self):
        main(['-file', './test/miss_special/test.txt'])

    # void some values in key pairs
    # color, title, preview, description
    # Success
    @classmethod
    def test_13(self):
        main(['-file', './test/void_special/test.txt'])

    # void all values except path
    # Success
    @classmethod
    def test_14(self):
        main(['-file', './test/void_except_path/test.txt'])

    # void all values
    # Exception
    @classmethod
    def test_15(self):
        main(['-file', './test/void_preset/test.txt'])

    # miss only title
    # Success
    @classmethod
    def test_16(self):
        main(['-file', './test/miss_title/test.txt'])

    # miss only description
    # Success
    @classmethod
    def test_17(self):
        main(['-file', './test/miss_description/test.txt'])

    # void icon
    # Success
    @classmethod
    def test_18(self):
        main(['-file', './test/void_icon/test.txt'])

    # miss only preview
    # Success
    @classmethod
    def test_19(self):
        main(['-file', './test/miss_preview/test.txt'])

    # void preview
    # Success
    @classmethod
    def test_20(self):
        main(['-file', './test/void_preview/test.txt'])

    # miss only icon
    # Success
    @classmethod
    def test_21(self):
        main(['-file', './test/miss_icon/test.txt'])

    # miss only preview and void icon
    # Success
    @classmethod
    def test_22(self):
        main(['-file', './test/miss_preview_void_icon/test.txt'])

    # void preview and miss icon
    # Success
    @classmethod
    def test_23(self):
        main(['-file', './test/void_preview_miss_icon/test.txt'])


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestApp))
    return suite

unittest.TextTestRunner(verbosity=2).run(suite())
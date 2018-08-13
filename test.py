#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

if __name__ == "__main__":
    tests = unittest.TestLoader().discover('tests', pattern='*_test.py')
    unittest.TextTestRunner(verbosity=1).run(tests)

import unittest
from unittest import defaultTestLoader
from test.common.utils.patterDesignUtilTest import PatterDesignUtilTest

suite = defaultTestLoader.discover("test")

#add your class test here
suite.addTest(unittest.makeSuite(PatterDesignUtilTest))
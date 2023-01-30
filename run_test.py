from unittest import TextTestRunner

from test import test_suite

runner = TextTestRunner()
runner.run(test_suite.suite)
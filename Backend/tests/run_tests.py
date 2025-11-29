import sys
import unittest

sys.path.insert(0, '.')

loader = unittest.TestLoader()
suite = loader.discover(start_dir='tests', pattern='test_*.py')

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

if not result.wasSuccessful():
    sys.exit(1)
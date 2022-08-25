import unittest

import numpy as np

import basd.config as cfg


class TestConfig(unittest.TestCase):

    COMP_ARRAY = np.array([1, 2, 3])

    def test_fake(self):

        result = cfg.fake()

        self.assertEqual(True, result)

        np.testing.assert_array_equal(TestConfig.COMP_ARRAY, np.array([1, 2, 3]))


if __name__ == '__main__':
    unittest.main()

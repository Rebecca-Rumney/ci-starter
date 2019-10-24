import unittest
from unittest.mock import patch

import clock


class MyTestCase(unittest.TestCase):

    @patch('time.time', return_value=1571871846.8861961)
    def test_the_time(self, mock):
        self.assertEqual(clock.whats_the_time(), 1571871835.8861962)


if __name__ == '__main__':
    unittest.main()

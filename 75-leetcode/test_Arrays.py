import Arrays
import unittest   # The test framework

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(Arrays.twoSum([3,2,4], 6), [1,2])

    # This test is designed to fail for demonstration purposes.
    def test_decrement(self):
        self.assertEqual(Arrays.twoSum([2,7,11,134], 9), [0,1])

if __name__ == '__main__':
    unittest.main()

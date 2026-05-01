import unittest

class TestPractice (unittest.TestCase):

    def test_add(self):
        self.assertEqual(1 + 2, 3)
        self.assertEqual(-10 + 15, 5)
        
    def test_sub(self):
        self.assertEqual(5 - 2, 3) 
        self.assertEqual(10 - 20, -10)
        
    def test_multiply(self):
        self.assertEqual(3 * 4, 12)
        self.assertEqual(-2 * 5, -10)
        
    def test_divide(self):
        self.assertEqual(10 / 2, 5)
        self.assertEqual(30 / 3, 10)
        
if __name__ == '__main__':
    unittest.main()
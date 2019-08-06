#tests
import unittest
import dostuff

class TestDoStuff(unittest.TestCase):
    
    def test_squarit_squares_simple_numbers(self):
        self.assertEqual(squarit(12),144)
        self.assertEqual(squarit(-12),144)
        self.assertEqual(squarit(0),0)
        self.assertEqual(squarit(1),1)
        
    def test_cubit_cubes_simple_numbers(self):
        self.assertEqual(cubit(2),8)
        self.assertEqual(cubit(-2),-8)
        self.assertEqual(cubit(0),0)
        self.assertEqual(cubit(1),1)

if __name__ == '__main__':
    unittest.main()

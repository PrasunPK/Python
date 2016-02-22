import unittest
import ComplexNumber


class TestStringMethods(unittest.TestCase):

    def test_getX(self):
        c = ComplexNumber.ComplexNumber(1,2)
        self.assertEqual(c.getX(), 1)

    def test_getY(self):
        c = ComplexNumber.ComplexNumber(3,4)
        self.assertEqual(c.getY(), 4)

    def test_add(self):
        c1 = ComplexNumber.ComplexNumber(1,2)
        c2 = ComplexNumber.ComplexNumber(3,4)
        c3 = c1.add(c2)
        self.assertEqual(c3.getX(), 4)
        self.assertEqual(c3.getY(), 6)


suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
unittest.TextTestRunner(verbosity=2).run(suite)

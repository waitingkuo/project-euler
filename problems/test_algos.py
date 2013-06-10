import unittest
import algos

ERR = 0.000001

class TestAlgos(unittest.TestCase):

    def assertFloatEqual(self, a, b):
        self.assertTrue(a+ERR > b)
        self.assertTrue(a < b+ERR)

    def test_prod(self):

        # Integers
        to_prod = [1, 2, 3, 4, 5]
        expected = 120
        result = algos.prod(to_prod)
        self.assertEqual(expected, result)

        # Has Float
        to_prod = [1.1, 2, 3, 4, 5]
        expected = 132.0
        result = algos.prod(to_prod)
        self.assertFloatEqual(expected, result)

        # Has Zero
        to_prod = [0, 2, 3, 4, 5]
        expected = 0
        result = algos.prod(to_prod)
        self.assertEqual(expected, result)
        

    def test_get_primes(self):
        
        upper_bound = 20 # Included
        expected = [2, 3, 5, 7, 11, 13, 17, 19]
        result = algos.get_primes(upper_bound)
        self.assertEqual(expected, result)


    def test_factorize(self):
        
        # Give n
        n = 20
        primes = None
        expected = [2, 2, 5]
        result = algos.factorize(20)
        self.assertEqual(expected, result)

        # Give n and primes
        n = 20
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        expected = [2, 2, 5]
        result = algos.factorize(20)
        self.assertEqual(expected, result)

        # Give n and insufficient primes
        n = 20
        primes = [2, 3]
        self.assertRaises(Exception, algos.factorize, n=n, primes=primes)


    def test_number_of_divisors(self):
        
        # Give n
        n = 20
        primes = None
        factors = None
        expected = 6
        result = algos.number_of_divisors(n, primes, factors)
        self.assertEqual(expected, result)

        # Give n and primes
        n = 20
        primes = [2, 3, 5, 9, 11, 13, 17, 19]
        factors = None
        expected = 6
        result = algos.number_of_divisors(n, primes, factors)
        self.assertEqual(expected, result)

        # Give n and factors
        n = 20
        primes = None
        factors = [2, 2, 5]
        expected = 6
        result = algos.number_of_divisors(n, primes, factors)
        self.assertEqual(expected, result)

        # Give n and factors with extra 1s
        n = 20
        primes = None
        factors = [2, 2, 5, 1, 1]
        expected = 6
        result = algos.number_of_divisors(n, primes, factors)
        self.assertEqual(expected, result)
        

        # Give n and incorrect factors
        n = 20
        primes = None
        factors = [2, 2, 3, 5]
        self.assertRaises(Exception, algos.number_of_divisors, n=n, factors=factors)


    def test_divisors_sum(self):

        # Give n
        n = 20
        primes = None
        factors = None
        expected = 42
        result = algos.divisors_sum(n, primes, factors)
        self.assertEqual(expected, result)

        # Give n and primes
        n = 20
        primes = [2, 3, 5, 9, 11, 13, 17, 19]
        factors = None
        expected = 42
        result = algos.divisors_sum(n, primes, factors)
        self.assertEqual(expected, result)

        # Give n and factors
        n = 20
        primes = None
        factors = [2, 2, 5]
        expected = 42
        result = algos.divisors_sum(n, primes, factors)
        self.assertEqual(expected, result)

        # Give n and factors with extra 1s
        n = 20
        primes = None
        factors = [2, 2, 5, 1, 1]
        expected = 42
        result = algos.divisors_sum(n, primes, factors)
        self.assertEqual(expected, result)
        

        # Give n and incorrect factors
        n = 20
        primes = None
        factors = [2, 2, 3, 5]
        self.assertRaises(Exception, algos.divisors_sum, n=n, factors=factors)


    def test_geometric_series_sum(self):

        a = 3
        r = 3
        n = 3
        expected = 39
        result = algos.geometric_series_sum(a, r, n)
        self.assertEqual(expected, result)

        a = 1.1
        r = 1.2
        n = 3
        expected = 4.004
        result = algos.geometric_series_sum(a, r, n)
        self.assertFloatEqual(expected, result)

    def test_C(self):

        m = 0
        n = 0
        expected = 1
        result = algos.C(m, n)
        self.assertEqual(expected, result)

        m = 1
        n = 1
        expected = 1
        result = algos.C(m, n)
        self.assertEqual(expected, result)

        m = 3
        n = 0
        expected = 3
        result = algos.C(m, n)
        self.assertEqual(expected, result)
        
        m = 10
        n = 3
        expected = 120
        result = algos.C(m, n)
        self.assertEqual(expected, result)

        m = 20
        n = 10
        expected = 184756
        result = algos.C(m, n)
        self.assertEqual(expected, result)

        m = 0
        n = 1
        self.assertRaises(Exception, algos.C, m=m, n=n)

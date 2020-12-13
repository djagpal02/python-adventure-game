from bed import bed
import unittest
from player import player

#Creates interactive Map object Bed
class TestBed(unittest.TestCase):

    def setUp(self):
        self.b1 = bed("key", 100)
        self.p1 = player(gold=200)
    def test_1(self):
        self.assertTrue(self.b1.use_bed(self.p1))
        


if __name__ == '__main__':
    unittest.main()
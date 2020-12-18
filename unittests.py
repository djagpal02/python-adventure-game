from bed import bed
from character import character
from enemy import enemy
from items import item, weapon, shield, armour, pot
from Map import Map, all_maps, home_town, home
from shops import shop
from location import location
from story_character import story_character
from player import player
import unittest

#Creates interactive Map object Bed
class TestBed(unittest.TestCase):

    def setUp(self):
        self.b1 = bed("key", 100)

    def test1(self):
        self.assertEqual(self.b1.cost,100)
        self.assertEqual(self.b1.key, "key")
        self.b1.key = "abc"
        self.assertEqual(self.b1.key,"abc")
        self.b1.cost = 200
        self.assertEqual(self.b1.cost,200)


class TestCharacter(unittest.TestCase):

    def setUp(self):
        self.c1 = character(10,"bob",100)
        self.c2 = character(15,"john",500)

    def test1(self):
        self.assertEqual(self.c1.level,10)
        self.assertEqual(self.c1.name,"bob")
        self.assertEqual(self.c1.gold,100)
        self.assertEqual(self.c1.items,{})
        self.assertEqual(self.c1.HP,self.c1.level*200)
        self.assertEqual(self.c1.max_HP,self.c1.level*200) 
        self.assertEqual(self.c1.AD,self.c1.level*25) 

    def test2(self):
        self.c1.level = 11
        self.assertEqual(self.c1.level, 11)
        self.c1.name = "alice"
        self.assertEqual(self.c1.name, "alice")
        self.c1.gold = 200
        self.assertEqual(self.c1.gold, 200)
        self.c1.items = {"thing":1}
        self.assertEqual(self.c1.items, {"thing":1})

    def test3(self):
        self.assertEqual(self.c1.attack(self.c2),True)
        self.assertLess(self.c2.HP, self.c2.max_HP)


class TestEnemy(unittest.TestCase):

    def setUp(self):
        self.e1 = enemy(10)

    # Most of enemy attributes are used from character class, as such this only tests attributes unique to enemy
    def test1(self):
        self.assertEqual(self.e1.name, "No Name")
        self.assertNotEqual(self.e1.gold, 0)
        self.assertEqual(self.e1.EXP_given, int(self.e1.level*200 +150))

class TestItem(unittest.TestCase):

    def setUp(self):
        self.i1 = item("abc","thing",500)
    
    def test1(self):
        self.assertEqual(self.i1.key, "abc")
        self.assertEqual(self.i1.name,"thing")
        self.assertEqual(self.i1.value,500)
    
    def test2(self):
        self.i1.key = "def"
        self.assertEqual(self.i1.key, "def")
        self.i1.name = "stuff"
        self.assertEqual(self.i1.name, "stuff")
        self.i1.value = 1000
        self.assertEqual(self.i1.value, 1000)

class TestWeapon(unittest.TestCase):

    def setUp(self):
        self.w1 = weapon("abc", "weapon", 500, 25)
    
    # Most attributes already tested in base class Item
    def test1(self):
        self.assertEqual(self.w1.AD, 25)

class TestShield(unittest.TestCase):

    def setUp(self):
        self.s1 = shield("abc", "shield", 400, 100)

    # Most attributes already tested in base class Item
    def test1(self):
        self.assertEqual(self.s1.HP,100)

class TestArmour(unittest.TestCase):

    def setUp(self):
        self.a1 = armour("abc", "armour", 300, 200)

    # Most attributes already tested in base class Item
    def test1(self):
        self.assertEqual(self.a1.HP,200)

class TestPot(unittest.TestCase):

    def setUp(self):
        self.p1 = pot("abc", "pot", 50, 500)
    
    def test1(self):
        self.assertEqual(self.p1.regen, 500)

class TestMap(unittest.TestCase):
    
    def setUp(self):
        self.m1 = Map("map", "map1", [(1,1)],[[(99,"-WALL"),(99,"-WALL")],[(99,"-WALL"),(50,"DOOR1")]])

    def test1(self):
        self.assertEqual(self.m1.key, "map")
        self.assertEqual(self.m1.name,"map1")
        self.assertEqual(self.m1.doors, [(1,1)])
        self.assertEqual(self.m1.matrix,[[(99,"-WALL"),(99,"-WALL")],[(99,"-WALL"),(50,"DOOR1")]])


class TestLocation(unittest.TestCase):
    
    def setUp(self):
        # Using home Map since this test is only for location, can use game map for testing
        self.l1 = location(home,1,1)

    def test1(self):
        self.assertEqual(self.l1.map, home)
        self.assertEqual(self.l1.row, 1)
        self.assertEqual(self.l1.col, 1)

    def test2(self):
        self.l1.row = 0
        self.assertEqual(self.l1.row, 0)
        self.l1.col = 0
        self.assertEqual(self.l1.col, 0)

    def test3(self):
        self.assertTrue(self.l1.changemap("HTOWN"))
        self.assertEqual(self.l1.map, home_town)
        self.assertEqual(self.l1.row, 1)
        self.assertEqual(self.l1.col, 5)

class TestShop(unittest.TestCase):

    def setUp(self):
        self.s1 = shop("abc", ["bob"])
        self.s2 = shop("def", ["alice"])
    
    def test1(self):
        self.assertEqual(self.s1.key, "abc")
        self.assertEqual(self.s1.available_items, ["bob"])
    
    def test2(self):
        self.assertNotEqual(self.s1.available_items, self.s2.available_items)

class TestStoryCharacter(unittest.TestCase):

    def setUp(self):
        self.s1 = story_character("bob", "abc")

    def test1(self):
        self.assertEqual(self.s1.name, "bob")
        self.assertEqual(self.s1.key, "abc")

class TestPlayer(unittest.TestCase):
    
    def setUp(self):
        self.p1 = player()
        self.l1 = location(home,1,1)

    # Some attributes have already been tested in super class Character
    def test1(self):
        self.assertEqual(self.p1.current_location.map,self.l1.map)
        self.assertEqual(self.p1.current_location.row,self.l1.row)
        self.assertEqual(self.p1.current_location.col,self.l1.col)
        self.assertEqual(self.p1.last_save_location.map,self.l1.map)
        self.assertEqual(self.p1.last_save_location.row,self.l1.row)
        self.assertEqual(self.p1.last_save_location.col,self.l1.col)
        self.assertEqual(self.p1.EXP, 0)
        self.assertEqual(self.p1.exp_needed,500)
        self.assertEqual(self.p1.HP, 500 + self.p1.level*200)
        self.assertEqual(self.p1.AD, self.p1.level*50)
        self.assertEqual(self.p1.story_tracker, 1)

    def test2(self):
        # Test interact method
        self.assertEqual(self.p1.interact("storyCharacter","PARNT"),0)
        self.assertEqual(self.p1.interact("bed","HTLB2"),1)
        self.assertEqual(self.p1.interact("shop","SHOP1"),2)
        




if __name__ == '__main__':
    unittest.main()
import unittest, os
import Class_management as CM

class Test_Player_Class(unittest.TestCase):

    def test_get_first_class(self):
        player = CM.Player("test", 1)
        player.get_stats(player.id)
        self.assertEqual(player.health, 1000)
        self.assertEqual(player.power, 100)
        self.assertEqual(player.hero_name, "Bird Breathless")

    def test_get_second_class(self):
        player = CM.Player("test", 2)
        player.get_stats(player.id)
        self.assertEqual(player.health, 1500)
        self.assertEqual(player.power, 80)
        self.assertEqual(player.hero_name, "Contact 0")
    
    def test_get_third_class(self):
        player = CM.Player("test", 3)
        player.get_stats(player.id)
        self.assertEqual(player.health, 700)
        self.assertEqual(player.power, 180)
        self.assertEqual(player.hero_name, "Nova Flare")

if __name__ == '__main__':
    unittest.main()
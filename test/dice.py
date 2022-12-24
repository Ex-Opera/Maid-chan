import unittest
from commands.engine.dice import Dice

class TestDice(unittest.TestCase):
  def test_roll_with_bonus(self):
    dice = Dice("2d20+5")
     rolls, bonus, total = dice.roll()
     self.assertEqual(len(rolls), 2)
     self.assertEqual(bonus, "+5")
     self.assertIsInstance(total, int)

  def test_roll_without_bonus(self):
    dice = Dice("2d20")
    rolls, bonus, total = dice.roll()
    self.assertEqual(len(rolls), 2)
    self.assertIsNone(bonus)
    self.assertIsInstance(total, int)

  def test_roll_with_negative_bonus(self):
    dice = Dice("2d20-5")
    rolls, bonus, total = dice.roll()
    self.assertEqual(len(rolls), 2)
    self.assertEqual(bonus, "-5")
    self.assertIsInstance(total, int)

 def test_roll_with_multiplication(self):     dice = Dice("2d20*5")
    rolls, bonus, total = dice.roll()
    self.assertEqual(len(rolls), 2)
    self.assertEqual(bonus, "*5")
    self.assertIsInstance(total, int)

  def test_roll_with_division(self):
    dice = Dice("2d20/5")
    rolls, bonus, total = dice.roll()
    self.assertEqual(len(rolls), 2)
    self.assertEqual(bonus, "/5")
    self.assertIsInstance(total, int)

if __name__ == '__main__':
  unittest.main()

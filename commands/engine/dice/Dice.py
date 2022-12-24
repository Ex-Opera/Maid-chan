import random, re

class Dice:
  def __init__(self, dice_string: str):
    self.dice_string = dice_string
    self.rolls = []
    self.bonus = None
    self.total = None
    self.parse_dice_string()

  def parse_dice_string(self):
    # Find all occurrences of +, -, *, or / in dice string
    bonus_ops = re.finditer(r'[+\-*/]', self.dice_string)
    try:
      # Split dice string on first occurrence of bonus op
      first_bonus_op = next(bonus_ops).start()
      self.bonus = self.dice_string[first_bonus_op:]
      self.dice_string = self.dice_string[:first_bonus_op]
    except StopIteration:
      # No bonus op found, set bonus to None
      self.bonus = None

    self.rolls = [int(x) for x in self.dice_string.split('d')]
    if len(self.rolls) == 1:
      self.rolls.append(self.rolls[0])
      self.rolls[0] = 1

  def roll(self):
    # Roll the dice and apply bonus
    rolls = [random.randint(1, self.rolls[1]) for _ in range(self.rolls[0])]
    self.total = sum(rolls)
    if self.bonus:
      self.total = eval(f'{self.total}{self.bonus}')
    return self.total

dice = Dice("6d12+5")
print(dice.roll())

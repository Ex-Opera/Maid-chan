import random
import re
from typing import List, Tuple, Optional, Union

class Dice:
    def __init__(self, dice_string: str) -> None:
        self.dice_string: str = dice_string
        self.dice_info: Tuple[int, int] = None
        self.rolls: List[int] = None
        self.bonuses: Optional[str] = None
        self.total: Optional[Union[int, float]] = None
        self.parse_dice_string()

    def parse_dice_string(self) -> None:
        # Define the regex pattern to match the valid dice string format
        pattern = r'^(\d+)?d(\d+)(?:((?:[+\-*/]\d+)+))?$'
        match = re.match(pattern, self.dice_string)
        if not match:
            raise ValueError("Invalid dice string format")
        # Extract the number of dice and sides per die and bonuses
        num_dice = int(match.group(1) or 1)
        sides_per_die = int(match.group(2))
        self.dice_info = (num_dice, sides_per_die)
        self.bonuses = match.group(3)

    def roll(self) -> Tuple[List[int], Optional[str], Union[int, float]]:
        self.rolls = [random.randint(1, self.dice_info[1]) for _ in range(self.dice_info[0])]
        self.total = eval(f"{sum(self.rolls)}{self.bonuses or '*1'}")
        return self.rolls, self.bonuses, self.total

# Example usage
# dice = Dice("6d12+3")
# print(dice.roll())

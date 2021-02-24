from enum import Enum
from random import randint


class Turn(Enum):
    BOT = 0
    PLAYER = 1

    @staticmethod
    def random() -> 'Turn':
        return Turn.BOT if randint(0, 1) == 0 else Turn.PLAYER

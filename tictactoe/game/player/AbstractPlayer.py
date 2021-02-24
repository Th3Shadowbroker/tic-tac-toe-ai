from abc import ABC, abstractmethod


class AbstractPlayer(ABC):

    @abstractmethod
    def play(self):
        pass

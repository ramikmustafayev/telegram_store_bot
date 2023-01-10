import abc
from markup.markup import Keyboards

from data_base.dbalchemy import DbManager


class Handler(metaclass=abc.ABCMeta):
    def __init__(self,bot) -> None:
        self.bot=bot
        self.DB=DbManager()
        self.keyboards=Keyboards()

    @abc.abstractmethod
    def handle(self):
        pass
from typing import Union

from .quest import QuestIP
from .servant import ServantIP


def parse_servant(html: Union[bytes, str]):
    return ServantIP(html).parse()


def parse_quest(html: Union[bytes, str]):
    return QuestIP(html).parse()

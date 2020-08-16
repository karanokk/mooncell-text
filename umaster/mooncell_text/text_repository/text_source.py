from typing import Sequence, Dict


class TextSource:
    def page(self, title: str, *props) -> Dict[str, any]:
        pass

    def pages_revid(self, titles: Sequence[str]) -> Dict[str, int]:
        pass

    def save(self, file, name: str):
        pass

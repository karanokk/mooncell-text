import json
import os
from typing import Sequence, Dict

from .text_source import TextSource


class LocalTextSource(TextSource):

    def __init__(self, source_dir: str):
        if not os.path.exists(source_dir):
            os.makedirs(source_dir)
        self.source_dir = source_dir

    def page(self, title: str, *props) -> Dict[str, any]:
        path = os.path.join(self.source_dir, title)
        if os.path.exists(path):
            with open(path) as f:
                resp = json.load(f)
                return resp

    def pages_revid(self, titles: Sequence[str]) -> Dict[str, int]:
        result = {}
        for filename in os.listdir(self.source_dir):
            if filename in titles:
                page = self.page(filename)
                if page is None:
                    result[filename] = -1
                else:
                    title = page["title"]
                    result[title] = page["revid"]
        return result

    def save(self, file, name: str):
        path = os.path.join(self.source_dir, name)
        with open(path, 'w+') as f:
            if isinstance(file, dict):
                json.dump(file, f)
            elif isinstance(file, str):
                f.write(file)

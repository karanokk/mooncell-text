from .text_source import TextSource
from .utils import ServantProp, csv_from_page
from ..mediawiki_api import ParseProp


class TextRepository:
    def __init__(self,
                 local_source: TextSource,
                 remote_source: TextSource,
                 dirty_servants: dict = None
                 ):
        self.local_source = local_source
        self.remote_source = remote_source
        self.dirty_servants = dirty_servants
        self._servants_name_link = None

    # ------------------------------ Servant ------------------------------ #

    @property
    def servants_name_link(self):
        if not self._servants_name_link:
            self._servants_name_link = list(
                map(lambda x: x[0], self.lastest_servants(ServantProp.name_link)))
        return self._servants_name_link

    def checkout_dirty_servants(self):
        local_revids = self.local_source.pages_revid(self.servants_name_link)
        remote_revids = self.remote_source.pages_revid(self.servants_name_link)
        self.dirty_servants = dict(
            remote_revids.items() - local_revids.items())
        return self.dirty_servants

    def lastest_servants(self, *props):
        text = self.remote_source.page('英灵图鉴')[ParseProp.text]
        return csv_from_page(text, *props)

    def servant(self, name: str):
        if self.dirty_servants is None:
            self.checkout_dirty_servants()
        page: dict = None
        if name in self.dirty_servants.keys():
            page = self.remote_source.page(
                name, ParseProp.revid, ParseProp.text)
            self.local_source.save(page, name)
            self.dirty_servants.pop(name)
        else:
            page = self.local_source.page(name)
        return page[ParseProp.text]

    def all_servants(self):
        for name_link in self.servants_name_link:
            yield self.servant(name_link)

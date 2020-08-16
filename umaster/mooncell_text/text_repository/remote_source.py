from typing import Sequence, Dict, Tuple

from ..mediawiki_api import *
from .text_source import TextSource


class RemoteTextSource(TextSource):
    def __init__(self, endpoints: MediaWikiEndpoints):
        self._endpoints = endpoints

    def page(self, title: str, *props) -> Dict[str, any]:
        props = props if props else [ParseProp.text]
        params = {
            ParseParameter.page: title,
            ParseParameter.prop: props}
        resp = self._endpoints.parse(params)
        return resp

    def pages_revid(self, titles: Sequence[str]) -> Dict[str, int]:
        result = {}
        n = 0
        while n < len(titles):
            title_slice = titles[n:n+50]
            params = {
                QueryParameter.titles: title_slice,
                QueryParameter.prop: QueryProp.revisions
            }
            resp_json = self._endpoints.query(params)
            pages = resp_json["pages"]
            for page in pages:
                title = page["title"]
                result[title] = page[QueryProp.revisions][0]["revid"]
            n += 50
        return result

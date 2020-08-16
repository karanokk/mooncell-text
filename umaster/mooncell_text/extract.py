import os
import json
import logging

from .text_repository import LocalTextSource, RemoteTextSource, TextRepository
from .mediawiki_api import MediaWikiEndpoints
from .parser import ServantIP


_text_repo = TextRepository(
    LocalTextSource('./page_text'),
    RemoteTextSource(MediaWikiEndpoints('https://fgo.wiki/api.php'))
)

def dirty_servants():
    return _text_repo.checkout_dirty_servants()

def extract_all_servants():
    for servant_text in _text_repo.all_servants():
        servant = ServantIP(servant_text).parse()
        yield servant
import unittest

from mooncell_text.text_source.mediawiki_api import (
    MediaWikiEndpoints, ParseParameter, ParseProp, QueryParameter, QueryProp)


class MediaWikiApiTest(unittest.TestCase):
    def setUp(self):
        self.endpoints = MediaWikiEndpoints('https://fgo.wiki/api.php')

    def test_parse(self):
        pagename = '齐格飞'
        params = {ParseParameter.page: pagename,
                  ParseParameter.prop: [ParseProp.revid, ParseProp.text]}
        resp = self.endpoints.parse(params)
        self.assertGreaterEqual(resp[ParseProp.revid], 294793)
        self.assertEqual(resp['title'], pagename)
        self.assertTrue(resp[ParseProp.text].startswith(
            '<div class="mw-parser-output">'))

    def test_query(self):
        params = {QueryParameter.titles: [
            '玛修・基列莱特', '卫宫'], QueryParameter.prop: [QueryProp.revisions]}
        resp = self.endpoints.query(params)
        self.assertIsNotNone(resp['pages'])
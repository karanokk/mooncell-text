import unittest

from mockito import ANY, ARGS, mock, verify, verifyZeroInteractions, when

from mooncell_text.mediawiki_api import ParseProp
from mooncell_text.text_repository import TextRepository, TextSource


class TextRepositoryTest(unittest.TestCase):

    def setUp(self):
        self.local = mock(TextSource())
        self.remote = mock(TextSource())
        self.repo = TextRepository(self.local, self.remote)

    def test_check_dirty_servants(self):
        when(self.repo).lastest_servants('name_link').thenReturn([])
        when(self.local).pages_revid([]).thenReturn({'齐格飞': 1000, '卫宫': 1099})
        when(self.remote).pages_revid([]).thenReturn(
            {'齐格飞': 1000, '卫宫': 1100, '阿蒂拉': 1200})
        dirty_servants = self.repo.check_dirty_servants()
        self.assertEqual(dirty_servants, {'卫宫': 1100, '阿蒂拉': 1200})

    def test_lastest_servants(self):
        pass

    def test_servant(self):
        dirty_servant = '齐格飞'
        resp_json = {ParseProp.text: 'TEST'}
        self.repo.dirty_servants = {dirty_servant: 1000}
        when(self.local).save(ANY, ANY)

        with when(self.remote).page(dirty_servant, *ARGS).thenReturn(resp_json):
            result = self.repo.servant(dirty_servant)
            self.assertEqual(result, resp_json[ParseProp.text])
            verify(self.remote).page(dirty_servant, *ARGS)
            verify(self.local).save(resp_json, dirty_servant)
            verify(self.local, times=0).page(dirty_servant)

        exist_servant = '卫宫'
        with when(self.local).page(exist_servant).thenReturn(resp_json):
            result = self.repo.servant(exist_servant)
            self.assertEqual(result, resp_json[ParseProp.text])
            verify(self.remote, times=0).page(exist_servant)
            verify(self.local, times=0).save(resp_json, exist_servant)
            verify(self.local).page(exist_servant)

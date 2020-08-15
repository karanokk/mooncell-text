import unittest

from mooncell_text.MooncellText import MooncellText

class MooncellTextTest(unittest.TestCase):
    def test_all_servants(self):
        mt = MooncellText()
        # mt.extract_servant('玛修·基列莱特')
        mt.extract_all_servants_to_file('/Users/byunfi/Desktop/extract')
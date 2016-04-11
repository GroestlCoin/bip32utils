import unittest

from bip32utils import BIP32Key

class TestXpub(unittest.TestCase):
    def test_from_extended_key(self):
        extkey = 'xpub6BLBYTKDDbdgAmfVeZRE1VFTKCFtRv9CDkpUnSfrDiA3eN9NPPS8zLi4ykGgdQKoRvWhjnz6o1VffVGfjhdMnaby6Kmn8YLiJiCzuw8KugM'
        key = BIP32Key.fromExtendedKey(extkey)
        child = key.ChildKey(0).ChildKey(0)

        self.assertEqual('FjxiGJ7kkTHY1x3MBnZc9AHKFs9rRVUTKp', child.Address())
        self.assertEqual('020d54f0c23eb2f16d319e0168a9c7dfea90454f234b0b81359339db44d005e12a', child.PublicKey().encode('hex'))

        child = key.ChildKey(0).ChildKey(1)
        self.assertEqual('FZgDwnt2MbPPBtxNRLuG4xSxEvCeG11znT', child.Address())
        self.assertEqual('03e4e5e55b653cbe56555f31560df892b0d4ed967eae11754e6f35cedfc96e1fde', child.PublicKey().encode('hex'))


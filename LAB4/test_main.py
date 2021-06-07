import pytest
from tmain import Reg, count_mask

class TestMain:
    
    # def test_Reg_generateX(self):
    #     reg = Reg(2).generate_x()
    #     self.assertEqual(reg.X, 1)
    # def test_lfsr1iter_x(self):
    #     reg = Reg(2)
    #     for i in range(26):
    #         assert reg.lfsr1iter_x() == 0
        
    def test_count_mask(self):
        assert count_mask(32) == 0xFFFFFFFF
        assert count_mask(31) == 0x7FFFFFFF
        assert count_mask(30) == 0x3FFFFFFF

if __name__ == "__main__":
    TestMain().test_count_mask()
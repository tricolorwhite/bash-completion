import pytest


@pytest.mark.bashcomp(cmd="mii-diag")
class TestMiiDiag:
    @pytest.mark.complete("mii-diag ")
    def test_1(self, completion):
        assert completion

import pytest

@pytest.mark.skip(reason="Feature in development")
def test_feature_in_development():
    ...

@pytest.mark.skip(reason="Feature in development")
class TestPytestSkip:
    def test_feature_in_development_1(self):
        ...
    def test_feature_in_development_2(self):
        ...

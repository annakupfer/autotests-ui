import pytest

@pytest.mark.custom
class TestCustom:
    @pytest.mark.registration
    def test_user_registration(self):
        pass

    @pytest.mark.smoke
    def test_user_login(self):
        pass

    @pytest.mark.registration
    @pytest.mark.regression
    def test_password_reset(self):
        pass

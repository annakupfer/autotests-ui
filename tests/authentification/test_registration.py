
import pytest
import allure
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity
from pages.authentification.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage

@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTIFICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTIFICATION)
@allure.sub_suite(AllureStory.REGISTRATION)

class TestRegistration:
        @allure.title("Registration with correct email, username and password")
        @allure.severity(Severity.CRITICAL)
        def test_successful_registration(self,
                registration_page: RegistrationPage,
                dashboard_page: DashboardPage
        ) -> None:
                registration_page.visit(
                        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
                )
                registration_page.fill(
                        email="user.name@gmail.com",
                        username="username",
                        password="password")
                registration_page.click_registration_button()
                dashboard_page.dashboard_toolbar_view.check_visible()

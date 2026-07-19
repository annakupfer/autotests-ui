from playwright.sync_api import Page

from components.authentification.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage

class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form_component = RegistrationFormComponent(page)

        self.registration_button = page.get_by_test_id('registration-page-registration-button')
        self.login_link = page.get_by_test_id('registration-page-login-link')

    def fill(self, email: str, username: str, password: str):
        self.registration_form_component.fill(email, username, password)

    def click_registration_button(self):
        self.registration_button.click()

    def click_login_link(self):
        self.login_link.click()


from playwright.sync_api import Page

from elements.button import Button
from elements.link import Link
from components.authentification.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage

class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form_component = RegistrationFormComponent(page)

        self.registration_button = Button(page, 'registration-page-registration-button', 'Registration')
        self.login_link = Link(page, 'registration-page-login-link', "Login link")

    def fill(self, email: str, username: str, password: str):
        self.registration_form_component.fill(email, username, password)

    def click_registration_button(self):
        self.registration_button.click()

    def click_login_link(self):
        self.login_link.click()


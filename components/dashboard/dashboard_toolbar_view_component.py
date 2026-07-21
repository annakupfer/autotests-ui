from playwright.sync_api import Page

from elements.text import Text
from components.base_component import BaseComponent

class DashboardToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page,"dashboard-toolbar-title-text","Dashboard title")

    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text("Dashboard")
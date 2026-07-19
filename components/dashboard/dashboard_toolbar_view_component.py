from playwright.sync_api import expect

from components.base_component import BaseComponent

class DashboardToolbarViewComponent(BaseComponent):
    def check_visible(self):
        title = self.page.get_by_test_id("dashboard-toolbar-title-text")
        expect(title).to_be_visible()
        expect(title).to_have_text("Dashboard")
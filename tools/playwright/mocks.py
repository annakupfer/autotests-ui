from playwright.sync_api import Page, Route

def abort(route: Route):
    print(f'\nAborting url: {route.request.url}')
    route.abort()

def mock_static_resources(page: Page):
    page.route("**/*.{ico,png,jpg,svg,mp3,mp4,webp,woff,woff2}", abort)

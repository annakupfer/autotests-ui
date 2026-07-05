from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Наводим фокус на поле Email
    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.focus()

    # Вводим текст по символу с клавиатуры
    for char in "user.name@gmail.com":
        page.keyboard.type(char, delay=300)

    # Выделяем текст на странице
    page.keyboard.press("ControlOrMeta+A")

    # Задержка для наглядности выполнения теста
    page.wait_for_timeout(5000)

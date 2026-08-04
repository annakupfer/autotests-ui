import allure

@allure.step('Opening browser')
def open_browser():
    with allure.step('Get browser'):
        ...
    with allure.step('Start browser'):
        ...


@allure.step("Creating course with title '{title}'")
def create_course(title: str):
    with allure.step(f"Creating  course with title '{title}'"):
        ...


@allure.step('Closing browser')
def close_browser():
    ...



def test_feature():
    open_browser()
    create_course()
    close_browser()


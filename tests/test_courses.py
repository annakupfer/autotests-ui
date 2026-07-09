from playwright.sync_api import expect
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    # Переходим на страницу Courses
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверяется наличие и текст заголовка “Courses”
    courses_list_toolbar_title_text = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_list_toolbar_title_text).to_have_text('Courses')

    # Проверяется наличие и видимость иконки пустого блока
    courses_list_empty_view_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_list_empty_view_icon).to_be_visible()

    # Проверяется наличие и текст блока “There is no results”
    courses_list_empty_view_title_text = chromium_page_with_state.get_by_test_id(
        'courses-list-empty-view-title-text')
    expect(courses_list_empty_view_title_text).to_have_text('There is no results')

    # Проверяется наличие и текст описания блока:
    # "Results from the load test pipeline will be displayed here"
    courses_list_empty_view_description_text = chromium_page_with_state.get_by_test_id(
        'courses-list-empty-view-description-text')
    expect(courses_list_empty_view_description_text).to_have_text(
        'Results from the load test pipeline will be displayed here')



import pytest
from playwright.sync_api import Page
from pages.create_course_page import CreateCoursePage
from pages.courses_list_page import CoursesListPage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(
        chromium_page_with_state: Page,
        courses_list_page: CoursesListPage
):
    # Переходим на страницу Courses
    chromium_page_with_state.goto(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'
    )
    # Проверяется наличие и текст заголовка “Courses”
    courses_list_page.check_visible_courses_title()

    # Проверяется наличие кнопки создания курса
    courses_list_page.check_visible_create_course_button()

    # Проверяется отображение пустого блока
    courses_list_page.check_visible_empty_view()

@pytest.mark.courses
@pytest.mark.regression
def test_create_course(
        chromium_page_with_state: Page,
        create_course_page: CreateCoursePage,
        courses_list_page: CoursesListPage,
        ):
    # Переходим на страницу создания курса
    chromium_page_with_state.goto(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create'
    )

    # Проверяем заголовок, кнопку создания курса, и пустые блоки картинок
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()

    # Проверяем форму создания курса, заголовок заданий, кнопку создания заданий
    create_course_page.check_visible_create_course_form(
        title="",
        estimated_time="",
        description="",
        max_score="0",
        min_score="0",
    )
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()

    # Проверяем отображение блока с пустыми заданиями
    create_course_page.check_visible_exercises_empty_view()

    # Загружаем картинку и проверяем блок в состоянии загруженной картинки
    create_course_page.upload_preview_image(file = './testdata/files/image.png')
    create_course_page.check_visible_image_upload_view()

    # Заполняем форму создания курса
    create_course_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )

    # Создаем курс
    create_course_page.click_create_course_button()

    # Проверяем карточку курса, заголовок, кнопку создания курса
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(
        index=0,
        title="Playwright",
        estimated_time="2 weeks",
        max_score="100",
        min_score="10"
    )


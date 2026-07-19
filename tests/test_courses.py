import pytest

from pages.create_course_page import CreateCoursePage
from pages.courses_list_page import CoursesListPage

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(
        courses_list_page: CoursesListPage
):
    # Переход на страницу Courses
    courses_list_page.visit(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'
    )
    # Проверяется отображение Navbar, Sidebar, Toolbar
    courses_list_page.navbar.check_visible('username')
    courses_list_page.sidebar.check_visible()
    courses_list_page.toolbar_view.check_visible()

    # Проверяется отображение пустого блока
    courses_list_page.check_visible_empty_view()

@pytest.mark.courses
@pytest.mark.regression
def test_create_course(
        create_course_page: CreateCoursePage,
        courses_list_page: CoursesListPage,
        ):
    # Переход на страницу создания курса
    create_course_page.visit(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create'
    )
    # Проверяем заголовок, кнопку создания курса, и пустые блоки картинок
    create_course_page.create_course_toolbar_view.check_visible()

    create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)

    # Проверяем форму создания курса, заголовок заданий, кнопку создания заданий
    create_course_page.create_course_form.check_visible(
        title="",
        estimated_time="",
        description="",
        max_score="0",
        min_score="0",
    )
    create_course_page.create_course_exercises_toolbar_view.check_visible()

    # Проверяем отображение блока с пустыми заданиями
    create_course_page.check_visible_exercises_empty_view()

    # Загружаем картинку и проверяем блок в состоянии загруженной картинки
    create_course_page.image_upload_widget.upload_preview_image(file = './testdata/files/image.png')
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

    # Заполняем форму создания курса
    create_course_page.create_course_form.fill(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )

    # Создаем курс
    create_course_page.create_course_toolbar_view.click_create_course_button()

    # Проверяем карточку курса, Toolbar
    courses_list_page.toolbar_view.check_visible()
    courses_list_page.course_view.check_visible(
        index=0,
        title="Playwright",
        estimated_time="2 weeks",
        max_score="100",
        min_score="10"
    )


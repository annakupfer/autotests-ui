import pytest
import re
import allure
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity
from pages.courses.create_course_page import CreateCoursePage
from pages.courses.courses_list_page import CoursesListPage
from tools.routes import AppRoute
from config import settings

@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)

class TestCourses:
    @allure.title('Check displaying of empty courses list')
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self,
            courses_list_page: CoursesListPage
    ):
        # Переход на страницу Courses
        courses_list_page.visit(AppRoute.COURSES)
        # Проверяется отображение Navbar, Sidebar, Toolbar
        courses_list_page.navbar.check_visible(settings.test_user.username)
        courses_list_page.sidebar.check_visible()
        courses_list_page.toolbar_view.check_visible()

        # Проверяется отображение пустого блока
        courses_list_page.check_visible_empty_view()

    @allure.title('Create course')
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self,
            create_course_page: CreateCoursePage,
            courses_list_page: CoursesListPage,
    ):
        # Переход на страницу создания курса
        create_course_page.visit(AppRoute.COURSES_CREATE)
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
        create_course_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)
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
    @allure.title('Edit course')
    @allure.severity(Severity.NORMAL)
    def test_edit_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit(AppRoute.COURSES_CREATE)
        create_course_page.create_course_form.fill(
            title='Playwright',
            estimated_time='1h20m',
            description='Playwright',
            max_score='10',
            min_score='3'
        )
        create_course_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)
        create_course_page.create_course_toolbar_view.click_create_course_button()
        courses_list_page.check_current_url(re.compile(".*/#/courses"))
        courses_list_page.course_view.check_visible(
            index=0,
            title='Playwright',
            estimated_time='1h20m',
            max_score='10',
            min_score='3'
        )
        courses_list_page.course_view.menu.click_edit(0)
        create_course_page.create_course_form.fill(
            title='Python',
            estimated_time='2h30m',
            description='Python',
            max_score='15',
            min_score='2'
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()
        courses_list_page.course_view.check_visible(
            index=0,
            title='Python',
            estimated_time='2h30m',
            max_score='15',
            min_score='2'
        )
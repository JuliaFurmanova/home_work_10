import allure
from selene import have, be
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_dynamic_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")
        browser.driver.fullscreen_window()

    with allure.step("Ищем репозитория"):
        s('.search-input').click()
        s('#query-builder-test').type("eroshenkoam/allure-integration-example").press_enter()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-integration-example")).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие текста No results на странице"):
        s(by.text('No results')).should(be.visible)


def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-integration-example")
    go_to_repository("eroshenkoam/allure-integration-example")
    open_issue_tab()
    should_see_text('No results')


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")
    browser.driver.fullscreen_window()


@allure.step("Ищем репозитория {repo}")
def search_for_repository(repo):
    s('.search-input').click()
    s('#query-builder-test').type(repo).press_enter()

@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие текста {value}")
def should_see_text(value):
    s(by.text('No results')).should(be.visible)

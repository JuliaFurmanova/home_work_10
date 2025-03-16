from selene import browser, have, by, be
from selene.support.shared.jquery_style import s


def test_selene():
    browser.open("https://github.com")
    browser.driver.fullscreen_window()
    s('.search-input').click()
    s('#query-builder-test').send_keys("eroshenkoam/allure-integration-example").press_enter()

    s(by.link_text("eroshenkoam/allure-integration-example")).click()

    s("#issues-tab").click()

    s(by.text('No results')).should(be.visible)

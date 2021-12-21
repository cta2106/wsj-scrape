import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from webdriver import WebDriver
from xpaths import (
    SIGN_IN_XPATH,
    USERNAME_BOX_XPATH,
    PASSWORD_BOX_XPATH,
    CONTINUE_WITH_PASSWORD_XPATH,
    SIGN_IN_BUTTON_XPATH,
    HEADLINE_XPATH,
)


def get_page_source(url: str) -> str:
    with WebDriver() as driver:
        driver.get(url)
        _sign_in(driver, SIGN_IN_XPATH)
        _write_username(driver, USERNAME_BOX_XPATH)
        _continue_with_password(driver, CONTINUE_WITH_PASSWORD_XPATH)
        _write_password(driver, PASSWORD_BOX_XPATH)
        _submit(driver, SIGN_IN_BUTTON_XPATH)
        page_source = _page_source(driver, HEADLINE_XPATH)
    return page_source


def _sign_in(driver: WebDriver, sign_in_xpath: str) -> None:
    sign_in_button = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, sign_in_xpath))
    )
    sign_in_button.click()


def _write_username(driver: WebDriver, username_box_xpath: str) -> None:
    username_box = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, username_box_xpath))
    )
    driver.implicitly_wait(10)
    username_box.send_keys(os.getenv("WSJ_USERNAME"))


def _continue_with_password(
    driver: WebDriver, continue_with_password_xpath: str
) -> None:
    continue_with_password_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, continue_with_password_xpath))
    )
    continue_with_password_button.click()


def _write_password(driver: WebDriver, password_box_xpath: str) -> None:
    password_box = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, password_box_xpath))
    )
    driver.implicitly_wait(10)
    password_box.send_keys(os.getenv("WSJ_PASSWORD"))


def _submit(driver: WebDriver, sign_in_button_xpath: str) -> None:
    sign_in_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, sign_in_button_xpath))
    )
    sign_in_button.click()


def _page_source(driver: WebDriver, headline_xpath: str) -> str:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, headline_xpath))
    )

    page_source = driver.execute_script("return document.body.innerHTML;")
    return page_source

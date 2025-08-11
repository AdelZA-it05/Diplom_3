from selenium import webdriver
import pytest

from api_helpers import ApiMethods
import data


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome()
        data.DRIVER_NAME = 'chrome'
    else:
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox()
        data.DRIVER_NAME = 'firefox'
    yield driver
    driver.quit()

@pytest.fixture()
def user():
    apimethods = ApiMethods()
    responce = apimethods.create_user()
    yield responce
    apimethods.delete_user(responce[2][0], responce[2][1])

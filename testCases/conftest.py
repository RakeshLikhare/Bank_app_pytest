import pytest as pytest
from selenium import webdriver

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("headless")

def pytest_addoption(parser):          ##command linear for cross browsing
    parser.addoption("--browser")

@pytest.fixture()
def setup(request):
    browser=request.config.getoption("--browser")
    if browser=="chrome":
       driver = webdriver.Chrome()
    elif browser=="firefox":
        driver = webdriver.Firefox()
    elif browser=="edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://bankapp.credence.in/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()



##jitne hamare data sets hai utni he hame testcase me conditional statments(if,elif,else) dena padenga and utne he hamare testcase bhi consider hote hai

@pytest.fixture(params=[

    ("Admin","pass"),    ##data set ##usernme meand Admin ka index ho gya 0 and expected result means pass ka index ho gya 1
    ("Tushar","pass"),
    ("Admin420","fail"),
    ("demo2","pass"),
    ("demo13","fail")

])

def getDataForSearchUser(request):
    return request.param

##commands for generating allure report:
# >pytest -v  --alluredir="Allure-result"--for generating
# >allure serve Allure-result --for see
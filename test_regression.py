import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

base_url = 'https://homepro.herokuapp.com/index.php'
expected_url = 'https://homepro.herokuapp.com/order.php'
expected_success_url = "https://homepro.herokuapp.com/orderconfirm.php"


@pytest.mark.parametrize("name, lastname", [
    ("Vladimir", "LastName2"),
    ("Anton", "LastName2"),
    ("Mia", "LastName2"),
    ("Crabs", "LastName2"),
    ("Alex", "LastName2")
])
@pytest.mark.regressiontest2
def test_schedule_success(browser, name, lastname):
    browser.get(base_url)
    browser.find_element(By.LINK_TEXT, "Schedule an Appointment").click()
    assert expected_url == browser.current_url
    jobtype_dropdown = Select(browser.find_element(By.NAME, "job_type"))
    jobtype_dropdown.select_by_visible_text("Decorating")
    browser.find_element(By.NAME, "first_name").send_keys(name)
    browser.find_element(By.NAME, "last_name").send_keys(lastname)
    browser.find_element(By.NAME, "phone").send_keys("+7-951-289-75-12")
    browser.find_element(By.NAME, "email").send_keys("eudvlad@gmail.com")
    browser.find_element(By.XPATH, "//input[@value = 'Schedule My consultation']").click()
    assert expected_success_url == browser.current_url
"""
Test Suite: DemoQA (https://demoqa.com)
Tests cover text box forms, buttons, alerts, and checkboxes.
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

BASE_URL = "https://demoqa.com"


class TestTextBoxForm:
    def test_text_box_submission(self, fresh_driver):
        """Submitting the text box form should display filled values."""
        fresh_driver.get(f"{BASE_URL}/text-box")
        wait = WebDriverWait(fresh_driver, 10)

        # Fill in all fields
        fresh_driver.find_element(By.ID, "userName").send_keys("Bhoomi Bhavsar")
        fresh_driver.find_element(By.ID, "userEmail").send_keys("bhoomi@example.com")
        fresh_driver.find_element(By.ID, "currentAddress").send_keys("Toms River, NJ")
        fresh_driver.find_element(By.ID, "permanentAddress").send_keys("Toms River, NJ")

        # Submit
        fresh_driver.find_element(By.ID, "submit").click()

        # Verify output section appears
        wait.until(EC.visibility_of_element_located((By.ID, "output")))
        output = fresh_driver.find_element(By.ID, "output").text
        assert "Bhoomi Bhavsar" in output, "Name not found in output"
        assert "bhoomi@example.com" in output, "Email not found in output"

    def test_invalid_email_shows_error(self, fresh_driver):
        """Submitting an invalid email should mark the field as invalid."""
        fresh_driver.get(f"{BASE_URL}/text-box")
        fresh_driver.find_element(By.ID, "userName").send_keys("Test User")
        fresh_driver.find_element(By.ID, "userEmail").send_keys("not-an-email")
        fresh_driver.find_element(By.ID, "submit").click()

        email_field = fresh_driver.find_element(By.ID, "userEmail")
        field_class = email_field.get_attribute("class")
        assert "field-error" in field_class, "Error class not applied to invalid email"


class TestButtons:
    def test_single_click(self, fresh_driver):
        """Single click button should confirm single click action."""
        fresh_driver.get(f"{BASE_URL}/buttons")
        wait = WebDriverWait(fresh_driver, 10)

        btn = fresh_driver.find_element(By.ID, "clickMeBtn")
        btn.click()

        wait.until(EC.visibility_of_element_located((By.ID, "dynamicClickMessage")))
        msg = fresh_driver.find_element(By.ID, "dynamicClickMessage").text
        assert "dynamic click" in msg.lower()

    def test_double_click(self, fresh_driver):
        """Double click button should confirm double click action."""
        fresh_driver.get(f"{BASE_URL}/buttons")
        wait = WebDriverWait(fresh_driver, 10)

        btn = fresh_driver.find_element(By.ID, "doubleClickBtn")
        ActionChains(fresh_driver).double_click(btn).perform()

        wait.until(EC.visibility_of_element_located((By.ID, "doubleClickMessage")))
        msg = fresh_driver.find_element(By.ID, "doubleClickMessage").text
        assert "double click" in msg.lower()

    def test_right_click(self, fresh_driver):
        """Right click button should confirm right click action."""
        fresh_driver.get(f"{BASE_URL}/buttons")
        wait = WebDriverWait(fresh_driver, 10)

        btn = fresh_driver.find_element(By.ID, "rightClickBtn")
        ActionChains(fresh_driver).context_click(btn).perform()

        wait.until(EC.visibility_of_element_located((By.ID, "rightClickMessage")))
        msg = fresh_driver.find_element(By.ID, "rightClickMessage").text
        assert "right click" in msg.lower()


class TestCheckbox:
    def test_home_checkbox_selectable(self, fresh_driver):
        """Home checkbox in the tree should be selectable."""
        fresh_driver.get(f"{BASE_URL}/checkbox")
        wait = WebDriverWait(fresh_driver, 10)

        home_toggle = fresh_driver.find_element(By.CSS_SELECTOR, "button[title='Toggle']")
        home_toggle.click()

        home_checkbox = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='tree-node-home'] span.rct-checkbox"))
        )
        home_checkbox.click()

        result = wait.until(EC.visibility_of_element_located((By.ID, "result")))
        assert result.is_displayed(), "Result section not displayed after selecting checkbox"

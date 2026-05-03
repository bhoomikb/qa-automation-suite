"""
Test Suite: Books to Scrape (http://books.toscrape.com)
Tests cover homepage, book listings, navigation, and detail pages.
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://books.toscrape.com"


class TestHomepage:
    def test_homepage_title(self, driver):
        """Homepage should load with correct page title."""
        driver.get(BASE_URL)
        assert "Books to Scrape" in driver.title, f"Unexpected title: {driver.title}"

    def test_logo_visible(self, driver):
        """Site logo should be visible on homepage."""
        driver.get(BASE_URL)
        logo = driver.find_element(By.CSS_SELECTOR, ".thumbnail")
        assert logo is not None

    def test_books_displayed_on_homepage(self, driver):
        """Homepage should display 20 books per page."""
        driver.get(BASE_URL)
        books = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
        assert len(books) == 20, f"Expected 20 books, found {len(books)}"

    def test_next_page_button_exists(self, driver):
        """Pagination 'next' button should exist on homepage."""
        driver.get(BASE_URL)
        next_btn = driver.find_elements(By.CSS_SELECTOR, "li.next a")
        assert len(next_btn) > 0, "Next page button not found"


class TestNavigation:
    def test_category_sidebar_exists(self, driver):
        """Left sidebar should contain book categories."""
        driver.get(BASE_URL)
        sidebar = driver.find_element(By.CSS_SELECTOR, "div.side_categories")
        assert sidebar.is_displayed(), "Category sidebar not visible"

    def test_category_link_navigates(self, driver):
        """Clicking a category should filter books correctly."""
        driver.get(BASE_URL)
        # Click the "Mystery" category
        mystery_link = driver.find_element(
            By.XPATH, "//a[normalize-space()='Mystery']"
        )
        mystery_link.click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "article.product_pod")))
        assert "mystery" in driver.current_url.lower(), "URL did not change to mystery category"

    def test_all_books_page_accessible(self, driver):
        """'All products' breadcrumb link should work."""
        driver.get(BASE_URL + "/catalogue/category/books_1/index.html")
        books = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
        assert len(books) > 0, "No books found on all-books page"


class TestBookDetails:
    def test_book_detail_page_loads(self, driver):
        """Clicking on a book should open its detail page."""
        driver.get(BASE_URL)
        first_book = driver.find_element(By.CSS_SELECTOR, "article.product_pod h3 a")
        book_title = first_book.get_attribute("title")
        first_book.click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.product_main")))
        page_title = driver.find_element(By.CSS_SELECTOR, "div.product_main h1").text
        assert page_title == book_title, f"Title mismatch: expected '{book_title}', got '{page_title}'"

    def test_book_price_displayed(self, driver):
        """Book detail page should show a price."""
        driver.get(BASE_URL)
        driver.find_element(By.CSS_SELECTOR, "article.product_pod h3 a").click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "p.price_color")))
        price = driver.find_element(By.CSS_SELECTOR, "p.price_color").text
        assert "£" in price, f"Price format unexpected: {price}"

    def test_add_to_basket_button_exists(self, driver):
        """Book detail page should have an Add to Basket button."""
        driver.get(BASE_URL)
        driver.find_element(By.CSS_SELECTOR, "article.product_pod h3 a").click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket")))
        btn = driver.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
        assert btn.is_displayed(), "Add to Basket button not visible"

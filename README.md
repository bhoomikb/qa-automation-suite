# 🧪 QA Automation Suite

A professional automated testing project built with **Python, Selenium, and pytest**. This suite runs end-to-end tests on real public websites, demonstrating core QA automation skills including Page Object Model (POM) design, test reporting, and CI-ready structure.

---

## 📌 What This Project Tests

- **[Books to Scrape](http://books.toscrape.com)** — A practice e-commerce site
  - Homepage loads correctly
  - Book listings display with correct data
  - Navigation and category filtering works
  - Book detail pages load properly

- **[DemoQA](https://demoqa.com)** — A QA practice web app
  - Form field validations
  - Button interactions
  - Alert and popup handling

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.x | Core language |
| Selenium WebDriver | Browser automation |
| pytest | Test framework |
| pytest-html | HTML test reports |
| webdriver-manager | Auto-manages ChromeDriver |

---

## 📂 Project Structure

```
qa-automation-suite/
├── tests/
│   ├── test_books_to_scrape.py   # E-commerce site tests
│   └── test_demoqa.py            # Form & UI interaction tests
├── pages/
│   ├── base_page.py              # Base Page Object
│   └── books_page.py             # Books site Page Object
├── conftest.py                   # Shared pytest fixtures
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Run

```bash
# 1. Clone the repo
git clone https://github.com/YOUR-USERNAME/qa-automation-suite.git
cd qa-automation-suite

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run all tests
pytest tests/ -v

# 4. Run with HTML report
pytest tests/ -v --html=reports/report.html
```

---

## 📸 Sample Output

```
tests/test_books_to_scrape.py::test_homepage_title PASSED
tests/test_books_to_scrape.py::test_books_displayed PASSED
tests/test_books_to_scrape.py::test_navigation_links PASSED
tests/test_demoqa.py::test_text_box_form PASSED
tests/test_demoqa.py::test_button_click PASSED

====== 5 passed in 12.43s ======
```

---

## 💡 Key Concepts Demonstrated

- ✅ Page Object Model (POM) design pattern
- ✅ Reusable pytest fixtures
- ✅ Explicit waits (no flaky `sleep()` calls)
- ✅ Cross-test setup and teardown
- ✅ HTML reporting

---

## 👩‍💻 Author

**Bhoomi Bhavsar** — CS Graduate | Manual QA Tester | Anthropic AI Certified  
[LinkedIn](https://www.linkedin.com/in/bhoomi-bhavsar)

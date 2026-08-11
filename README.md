# Selenium Python QA Automation Framework

UI and end-to-end automation framework built with **Python, Selenium WebDriver, and Pytest**, featuring Page Object Model architecture, advanced browser interactions, and HTML reporting.

## Systems Under Test

### SauceDemo

Primary application used for storefront end-to-end testing:

- Valid and invalid login
- Product validation and sorting
- Shopping cart operations
- Checkout validation
- Complete E2E purchase workflow

### The Internet (Herokuapp)

Used for advanced Selenium browser interaction testing:

- JavaScript alerts
- iframes
- Multiple windows and tabs
- Mouse hover interactions
- File uploads
- Dynamic elements and explicit waits

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- pytest-html
- Chrome & Firefox

## Framework Features

- Page Object Model with reusable `BasePage`
- Pytest fixtures and `conftest.py`
- Parameterized / data-driven testing
- Smoke, regression, and E2E markers
- Explicit waits and dynamic element handling
- Advanced browser interactions
- Cross-browser and headless execution
- Automatic screenshots on failures
- Logging and HTML reporting
- Centralized configuration (`config/config.py`)

## Test Flow

```text
Login
  ↓
Products
  ↓
Add to Cart
  ↓
Cart Validation
  ↓
Checkout
  ↓
Order Completion
```

## Project Structure

```text
selenium-python-automation/
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── checkout_complete_page.py
├── tests/
├── config/
├── utils/
├── reports/
├── screenshots/
├── logs/
├── conftest.py
├── pytest.ini
└── requirements.txt
```

## Run Tests

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the complete suite:

```bash
pytest -v
```

Run specific test categories:

```bash
pytest -m smoke
pytest -m regression
pytest -m e2e
```

Cross-browser execution:

```bash
pytest --browser chrome
pytest --browser firefox
```

Generate an HTML report:

```bash
pytest --html=reports/report.html --self-contained-html
```

## Purpose

Demonstrates practical **QA Automation / SDET engineering** skills including UI automation, E2E testing, Selenium, Pytest framework architecture, POM, data-driven testing, advanced browser interactions, cross-browser testing, failure diagnostics, and reporting.

## Next Steps

Not implemented yet, planned for later: Git/GitHub workflow polish, GitHub Actions CI, and optionally Docker.
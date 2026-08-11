# Selenium Python QA Automation Framework

QA automation framework built with **Python, Selenium WebDriver, and Pytest**, covering UI and end-to-end testing with CI integration.

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Docker
- GitHub Actions
- pytest-html
- Chrome & Firefox

## Features

- Page Object Model (POM) with reusable BasePage
- Pytest fixtures and `conftest.py`
- Parameterized / data-driven testing
- Smoke, regression, and E2E markers
- Explicit waits and dynamic element handling
- Alerts, iframes, tabs/windows, hover, and file uploads
- Cross-browser and headless execution
- Screenshots automatically captured on failures
- Logging and HTML test reports
- Configuration and test-data management
- Dockerized test execution
- Automated GitHub Actions CI on push

## Test Coverage

- Valid and invalid login
- Product validation and sorting
- Add products to cart
- Cart validation
- Checkout information
- Complete E2E purchase
- Advanced Selenium browser interactions

## Architecture

```text
selenium-python-automation/
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
├── config/
├── utils/
├── reports/
├── screenshots/
├── logs/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── Dockerfile
└── .github/workflows/tests.yml
```

## Run Tests

```bash
pytest -v
pytest -m smoke
pytest -m regression
pytest -m e2e
pytest --browser firefox
pytest --html=reports/report.html --self-contained-html
```

## Docker

```bash
docker build -t selenium-tests .
docker run --rm selenium-tests
```

## CI

**GitHub Actions** automatically runs the Selenium/Pytest test suite in headless Chrome on every push and publishes test artifacts.

## Purpose

Demonstrates practical **QA Automation / SDET** skills including Selenium, Pytest, POM, parameterization, test organization, cross-browser testing, reporting, CI, and Docker.
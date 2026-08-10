# Selenium Python QA Automation Framework

Production-style QA automation framework built with **Python, Selenium WebDriver, and Pytest**, covering UI, API, and end-to-end testing with CI/CD integration.

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Requests
- Page Object Model (POM)
- Docker
- GitHub Actions
- pytest-xdist
- HTML Reporting

## Features

- Page Object Model architecture
- Reusable Pytest fixtures and `conftest.py`
- Explicit waits and robust element handling
- Positive and negative test scenarios
- Data-driven and parameterized testing
- Cross-browser and headless execution
- Parallel test execution
- Screenshots and logs on failure
- REST API automation
- API + UI integration testing
- Dockerized execution
- Automated GitHub Actions CI/CD

## Test Coverage

### Authentication
- Valid and invalid login
- Empty credentials
- Locked-out users
- Error-message validation

### Products
- Product validation
- Product count
- Price and name sorting
- Dynamic element validation

### Shopping Cart
- Add/remove products
- Cart badge validation
- Product and price verification

### Checkout
- Customer information
- Order summary validation
- Complete E2E purchase workflow

### API
- GET / POST / PUT / PATCH / DELETE
- Status-code validation
- JSON payload validation
- Headers and authentication
- Positive and negative API scenarios

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
│   ├── ui/
│   └── api/
├── utils/
├── test_data/
├── reports/
├── screenshots/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── Dockerfile
└── .github/workflows/tests.yml
```

## Run Tests

Install dependencies:

```bash
pip install -r requirements.txt
```

Run all tests:

```bash
pytest -v
```

Run in parallel:

```bash
pytest -n auto
```

Run smoke tests:

```bash
pytest -m smoke
```

Generate HTML report:

```bash
pytest --html=reports/report.html --self-contained-html
```

Run with Docker:

```bash
docker build -t selenium-tests .
docker run --rm selenium-tests
```

## CI/CD

GitHub Actions automatically executes the automated test suite on pushes and pull requests and publishes test artifacts for failed/test runs.

## Purpose

This project demonstrates practical **QA Automation / SDET engineering** skills including test design, UI automation, API testing, framework architecture, test isolation, reporting, parallel execution, containerization, and CI/CD.
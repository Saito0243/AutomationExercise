# Automation Exercise Project

## Overview

This project is a personal QA automation exercise focused on building and expanding automated tests using Python and pytest.

The project is currently under development and is being used to practice web UI automation, API testing, test organization, reusable fixtures, and the Page Object Model.

## Technologies

* Python
* pytest
* Selenium WebDriver
* REST APIs
* Postman
* Git / GitHub

## Project Structure

The project separates page-specific functionality from test cases, allowing tests to interact with the application through reusable Page Object classes.

```text
AutomationExercise/
│
├── pages/
│   ├── home_page.py
│   ├── registration_detail_page.py
│   └── signup_login_page.py
│
├── tests/
│   └── test_register_user.py
│
├── conftest.py
├── data.py
├── .gitignore
└── README.md
```

### Pages

The `pages` directory contains Page Object classes representing individual pages or areas of the application.

These classes contain the Selenium locators and page-specific actions used by the tests.

### Tests

The `tests` directory contains the actual pytest test cases.

Tests use the Page Objects to interact with the application rather than placing all Selenium interactions directly inside the test functions.

### conftest.py

`conftest.py` contains reusable pytest fixtures used to provide common test setup and resources.

### data.py

`data.py` contains test data that is separated from the test logic.

## Current Focus

The project currently focuses on:

* Automating web UI test cases with Selenium
* Using pytest to organize and execute tests
* Applying the Page Object Model
* Creating reusable pytest fixtures with `conftest.py`
* Separating test data from test logic
* Using API requests where appropriate for test setup and cleanup
* Improving test organization and maintainability

## Current Tests

The test suite is currently in the early stages of development.

Current work includes automating user registration functionality and building the Page Objects and fixtures needed to support those tests.

Additional test cases and automation features will be added as the project develops.

## Goals

The primary goals of this project are to:

1. Build practical experience with Python-based test automation.
2. Develop a maintainable pytest test structure.
3. Gain experience with Selenium WebDriver.
4. Practice the Page Object Model.
5. Practice API testing and API integration within automated tests.
6. Develop experience creating and using pytest fixtures.
7. Improve test data management and test organization.
8. Gradually expand the project into a more complete automated test suite.

## Running the Tests

Install the required Python dependencies and run the test suite with:

```bash
pytest
```

A specific test file can be run with:

```bash
pytest tests/test_register_user.py
```

## Project Status

**In Development**

This project is an ongoing learning exercise. The structure, tests, and automation approach will continue to evolve as new concepts are learned and implemented.

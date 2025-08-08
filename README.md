

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running Tests

To run all tests:

```bash
pytest
```

To run specific tests:

```bash
pytest tests/test_home_page.py
```

To run tests with verbose output:

```bash
pytest -v
```
To run tests with specific browser

```bash
pytest tests/ -k "chrome" -v
```
or

```bash
pytest tests/ -k "firefox" -v
```


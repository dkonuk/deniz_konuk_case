

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Make sure you have the appropriate WebDriver for your browser:
   - For Chrome: ChromeDriver
   - For Firefox: GeckoDriver
   - For Edge: EdgeDriver

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


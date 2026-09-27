# Week 7 – Testing, Debugging, and Optimization

## Project
Python Full-Stack Car Rental Application

## Objective
This submission demonstrates unit testing, integration testing, debugging, error logging, and performance optimization for a car rental application.

## Testing Strategy
- Unit testing: individual backend functions such as vehicle availability, booking validation, and payment validation.
- Integration testing: API endpoint behavior and interaction between application components.
- Front-end testing: basic validation of important UI actions and form inputs.
- Regression testing: repeat important tests after fixes to confirm that existing functionality remains stable.

## Tools
- Python
- PyTest
- Flask test client (for API integration examples)
- JavaScript test examples
- Python logging
- Git/version control practices

## How to Run
1. Install Python 3.10+.
2. Create/activate a virtual environment.
3. Install dependencies:
   `pip install -r requirements.txt`
4. Run tests:
   `pytest -v`
5. Run only backend unit tests:
   `pytest backend/tests -v`
6. Run integration tests:
   `pytest backend/integration_tests -v`

The integration example assumes a Flask application exposing `/api/vehicles`.

## Included Files
- backend/tests/: unit test examples
- backend/integration_tests/: API integration test
- frontend/tests/: front-end validation test examples
- logs/error_log.txt: representative error log
- reports/debugging_report.md: debugging process and lessons learned
- reports/performance_report.md: optimization work
- pytest.ini: PyTest configuration
- requirements.txt: test dependencies

## Test Summary
The suite covers:
- Vehicle availability
- Booking date validation
- Payment amount validation
- API response status and data type
- Front-end booking form validation

## Optimization Summary
- Validate input before database/API operations.
- Return only required fields from API responses.
- Add database indexes to frequently queried columns.
- Avoid repeated database queries inside loops.
- Cache relatively static vehicle/category data where appropriate.
- Use pagination for large vehicle lists.
- Log errors with enough context for diagnosis without exposing sensitive payment information.

## Important
The included tests are structured as adaptable examples because the exact source code and endpoint names of the student's application may differ. Replace endpoint/import names with those used by the final application before execution.

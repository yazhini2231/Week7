# Debugging Report

## 1. Problem Identification
Testing was used to identify invalid booking dates, invalid payment amounts, and API integration dependencies.

## 2. Debugging Process
1. Reproduce the failing behavior with a small test case.
2. Identify the input that caused the failure.
3. Trace the value through validation and business logic.
4. Locate the missing or incorrect condition.
5. Implement the smallest appropriate fix.
6. Re-run the failing test.
7. Run the complete regression suite.

## 3. Examples
### Booking validation
A booking where the return date was before the pickup date should not be accepted. The validation function was updated to ensure the start date is less than or equal to the end date.

### Payment validation
A payment amount of zero or a negative amount is invalid. Positive-value validation was added before payment processing.

### API testing
The integration test checks for HTTP 200 and a list response. The exact import and endpoint should be connected to the final Flask project.

## 4. Lessons Learned
- Automated tests make defects reproducible.
- Validation should occur before expensive operations.
- Integration tests reveal problems that unit tests cannot detect.
- Error logs should provide useful diagnostic information without recording sensitive payment data.
- Regression testing is important after every bug fix.

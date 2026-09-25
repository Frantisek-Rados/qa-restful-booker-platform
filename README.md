# QA Portfolio – Restful Booker Platform

This repository contains my QA work for the **Restful Booker Platform** – a bed & breakfast booking system used for testing practice.

- **Live app:** https://automationintesting.online
- **Admin login:** admin / password
- **Source code:** https://github.com/mwinteringham/restful-booker-platform

## What's inside

| Folder | Description |
|---|---|
| `docs/` | Test strategy, test scenarios, defect reports |
| `api-tests/` | Automated API tests written in Python (pytest + requests) |
| `frontend-tests/` | Automated frontend tests written in Python (Playwright) |
| `postman/` | Postman collection for manual API testing |

## How to run the tests

### API tests

```bash
cd api-tests
pip install -r requirements.txt
pytest
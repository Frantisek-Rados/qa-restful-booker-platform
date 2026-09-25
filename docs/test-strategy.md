# Test Strategy – Restful Booker Platform

## 1. What to test

I focus on the critical parts of the application:
- **Booking process** – room selection, dates, guest details, confirmation
- **Admin panel** – login, viewing and managing bookings
- **Contact form** – submitting and retrieving messages
- **API layer** – verifying the backend correctly stores data

## 2. Order and why

1. **Booking flow (Happy Path)** – if booking doesn't work, the app has no purpose.
2. **Admin panel** – verify the booking was actually saved.
3. **API tests** – verify communication between frontend and backend.
4. **Negative scenarios** – invalid dates, empty fields.
5. **Regression** – if time is left.

## 3. Types of testing

- Functional (manual)
- API (Postman, Python)
- Regression
- Basic non-functional (performance, security)
- Exploratory

## 4. Where to focus first (limited time)

With only 60 minutes, I focus on the **critical user journey**:
- Booking a room end-to-end
- Verifying it shows up in the admin panel
- One API call to create a booking

I skip cross-browser testing and deep security tests.
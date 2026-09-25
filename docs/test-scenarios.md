# Test Scenarios – Restful Booker Platform

## Frontend

1. **Booking happy path** – open site, pick a room, select valid dates, fill in details, submit, check confirmation.
2. **Validation check** – submit form with empty required field, verify error message.
3. **Date validation** – check-out earlier than check-in should be blocked.
4. **Admin login** – login with admin/password, verify booking list is visible.
5. **Contact form** – fill in valid data, submit, check success message.

## Backend

1. **Create booking via API** – POST with valid data, verify 200/201 and booking ID.
2. **Get booking by ID** – GET existing booking, verify correct guest name and dates.
3. **Invalid booking data** – POST with missing fields, verify 400 Bad Request.
4. **Authentication check** – access protected endpoint without token, verify 401.
5. **Delete booking** – DELETE existing booking, verify 200/204 and GET returns nothing.
# Defect Reports – Restful Booker Platform

## Defect 1: "Amenities" navigation link does not work

**Title:** "Amenities" navigation link does not work – no section or page is displayed

**Environment:** Chrome (latest), Windows 11, https://automationintesting.online

**Steps to Reproduce:**
1. Open https://automationintesting.online
2. Look at the top navigation menu.
3. Click on the "Amenities" link.
4. Observe that nothing happens.

**Expected Result:** Clicking "Amenities" should scroll to an "Amenities" section or navigate to a dedicated page.

**Actual Result:** Clicking "Amenities" does nothing. Other links (e.g. "Location") work correctly.

**Severity:** Medium

**Priority:** Medium

**Why it's a defect:** The link is part of the main navigation and is expected to work. Broken links damage trust and prevent users from finding information about facilities.

---

## Defect 2: Inconsistent date picker behaviour

**Title:** Date picker requires drag-and-drop on room detail page, but works normally on the home page

**Environment:** Chrome (latest), Windows 11, https://automationintesting.online

**Steps to Reproduce:**
1. On the home page, try changing dates in the availability section – it works with a simple click.
2. Open a room detail page (e.g. Single room).
3. Try to change dates – a simple click does not work.
4. Hold the left mouse button and drag the cursor over the dates – this works.

**Expected Result:** The date picker should behave consistently across the app.

**Actual Result:** The room detail page requires a non-standard click-and-drag gesture.

**Severity:** Medium

**Priority:** High

**Why it's a defect:** Inconsistent UX. Users who book from the home page will be confused when the same calendar behaves differently.
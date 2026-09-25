from playwright.sync_api import sync_playwright


def test_homepage_loads():
    """Verify the home page loads and shows the B&B name."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://automationintesting.online")

        # Verify the page title / heading
        assert "Shady Meadows" in page.content()

        browser.close()


def test_navigation_to_booking():
    """Verify that clicking 'Book Now' opens the booking section."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://automationintesting.online")

        # Click the "Book Now" button
        page.click("text=Book Now")

        # Verify the booking form is visible
        assert page.is_visible("text=Check Availability")

        browser.close()
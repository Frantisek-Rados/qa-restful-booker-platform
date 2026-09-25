from playwright.sync_api import sync_playwright


def test_homepage_loads():
    """Verify the home page loads and shows the B&B name."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://automationintesting.online")

        # Wait for the page to render (Next.js loads content via JavaScript)
        page.wait_for_load_state("networkidle")

        # Verify the page contains the expected heading
        heading = page.locator("h1").first
        heading.wait_for(state="visible", timeout=10000)
        assert "Shady Meadows" in heading.inner_text()

        browser.close()


def test_navigation_to_booking():
    """Verify that clicking 'Book Now' opens the booking section."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://automationintesting.online")

        # Wait for the page to render
        page.wait_for_load_state("networkidle")

        # Click the "Book Now" button
        page.click("text=Book Now")

        # Wait for the booking form to appear
        booking_heading = page.locator("text=Check Availability").first
        booking_heading.wait_for(state="visible", timeout=10000)

        browser.close()
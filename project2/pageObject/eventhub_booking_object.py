from playwright.sync_api import expect, Page


class EventHubBookingPage:
    def __init__(self, page: Page):
        self.page = page

    def select_event(self, event_name):
        self.page.locator('#nav-events').click()
        expect(self.page.get_by_role(role="heading",name="Upcoming Events")).to_be_visible()
        self.page.locator('select:has(option[value="Conference"])').select_option("Conference")
        event_card = self.page.get_by_role("heading", name="World Tech Summit").locator(
            "xpath=ancestor::div[.//a[@data-testid='book-now-btn']]"
        )
        event_card.get_by_test_id("book-now-btn").click()



    def complete_booking(self):
        raise NotImplementedError("Implement booking actions here.")

    def verify_booking_result(self, expected):
        raise NotImplementedError("Implement booking verification here.")

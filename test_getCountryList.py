from playwright.sync_api import Page,expect

def test_save_country_name(page:Page):
    page.goto("https://www.townscountiespostcodes.co.uk/")
    



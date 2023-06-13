from playwright.sync_api import Page,expect

def test_save_country_name(page:Page):
    country_section_selector = "#nav div"
    country_lists_selector = "ul li a"
    country_title_selector = "#content h1"


    page.goto("/")
    country_section = page.locator(country_section_selector).nth(3)
    country_lists = country_section.locator(country_lists_selector)
    totalCountry = country_lists.count()
    for singleCountry in range(totalCountry):
        country_name_option = country_lists.nth(singleCountry)
        country_name = country_name_option.inner_text()
        print(country_name)
        country_name_option.click()
        country_title = page.locator(country_title_selector).nth(0).inner_text()
        print(country_title)
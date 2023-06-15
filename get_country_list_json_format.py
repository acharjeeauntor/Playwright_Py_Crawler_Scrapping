from playwright.sync_api import Page
import json

def test_save_country_name(page:Page):
    country_section_selector = "#nav ul"
    country_lists_selector = "li a"
    sub_country_list_selector = "tbody tr"
    sub_country_data_selector = "td"


    page.goto("/")
    country_section = page.locator(country_section_selector).nth(3)
    country_lists = country_section.locator(country_lists_selector)
    total_country = country_lists.count()
    data={}
    for single_country_index in range(total_country):
        country_name_option = country_lists.nth(single_country_index)
        country_name = country_name_option.inner_text()
        country_name_option.click()
        page.wait_for_timeout(4000)

        sub_country_list = page.locator(sub_country_list_selector)
        total_sub_country = sub_country_list.count()

        # Store Data into Excel File ---- Start From Here ----
        sub_country_names = []
        for sub_country_index in range(1,total_sub_country):
            sub_country_name = sub_country_list.nth(sub_country_index).locator(sub_country_data_selector).nth(1).inner_text()
            sub_country_names.append(sub_country_name)
        data[country_name] = sub_country_names

    file_path = f'{country_name}.json'

# Open the file in write mode and write the JSON data
    with open(file_path, 'w') as file:
        json.dump(data, file)

    print('Data stored in JSON format successfully.')

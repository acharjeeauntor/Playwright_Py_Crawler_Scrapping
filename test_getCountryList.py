from playwright.sync_api import Page
import csv

def test_save_country_name(page:Page):
    country_section_selector = "#nav div"
    country_lists_selector = "ul li a"
    country_title_selector = "#content h1"
    sub_country_list_selector = "tbody tr"
    sub_country_data_selector = "td"


    page.goto("/")
    country_section = page.locator(country_section_selector).nth(3)
    country_lists = country_section.locator(country_lists_selector)
    total_country = country_lists.count()
    for single_country_index in range(total_country):
        country_name_option = country_lists.nth(single_country_index)
        country_name = country_name_option.inner_text()
        #print(country_name)
        country_name_option.click()
        country_title = page.locator(country_title_selector).nth(0).inner_text()
        #print(country_title)

        sub_country_list = page.locator(sub_country_list_selector)
        total_sub_country = sub_country_list.count()
        # Header
        header = ['Country Name']
        # File path to save the CSV
        file_path = f'{country_name}.csv'
        # Store Data into CSV File ---- Start From Here ----
        with open(file_path, 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(header)
            for sub_country_index in range(1,total_sub_country):
                sub_country_name = sub_country_list.nth(sub_country_index).locator(sub_country_data_selector).nth(1).inner_text()
                csv_writer.writerow([sub_country_name])
                print('Data stored in CSV successfully.')
from playwright.sync_api import Page
import csv
import os

def test_save_country_name(page:Page):
    country_section_selector = "#nav ul"
    country_lists_selector = "li a"
    sub_country_list_selector = "tbody tr"
    sub_country_data_selector = "td"


    page.goto("/")
    country_section = page.locator(country_section_selector).nth(3)
    country_lists = country_section.locator(country_lists_selector)
    total_country = country_lists.count()
    for single_country_index in range(total_country):
        country_name_option = country_lists.nth(single_country_index)
        country_name = country_name_option.inner_text()
        country_name_option.click()
        page.wait_for_timeout(4000)

        sub_country_list = page.locator(sub_country_list_selector)
        total_sub_country = sub_country_list.count()
        # Header
        header = ['Country Name']
        # File path to save the CSV
        file_directory = 'Country_List_CSV_Data'
        if not os.path.exists(file_directory):
            os.makedirs(file_directory)
        
        file_path = os.path.join(file_directory, f'{country_name}.csv')
        # Store Data into CSV File ---- Start From Here ----
        with open(file_path, 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(header)
            for sub_country_index in range(1,total_sub_country):
                sub_country_name = sub_country_list.nth(sub_country_index).locator(sub_country_data_selector).nth(1).inner_text()
                csv_writer.writerow([sub_country_name])
from playwright.sync_api import sync_playwright

class BusinessCrawler:
    def __init__(self):
        self.base_url = "https://search.sunbiz.org/Inquiry/CorporationSearch/ByName"

    def search_business(self, business_name):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            try:
                # Navigate to the base URL
                page.goto(self.base_url)

                # Fill the search input field and submit the form
                page.fill('#SearchTerm', business_name)
                page.click('input[type="submit"][value="Search Now"]')

                # Wait for the search results container to appear
                page.wait_for_selector('#search-results', timeout=30000)

                # Check if there are results
                if page.locator('#search-results a').count() == 0:
                    print("No results found.")
                    return None

                # Click the first result
                first_result = page.locator('#search-results a').first
                first_result.click()

                # Wait for the details section to load
                page.wait_for_selector('.detailSection', timeout=30000)

                # Extract business details
                details = {
                    'business_name' : page.locator('#maincontent > div.searchResultDetail > div.detailSection.corporationName > p:nth-child(2)').text_content().strip(),
                    'registration_date' : page.locator('#maincontent > div.searchResultDetail > div.detailSection.filingInformation > span:nth-child(2) > div > span:nth-child(6)').text_content().strip(),
                    'principals_and_contact_information': page.locator('#maincontent > div.searchResultDetail > div:nth-child(7)').text_content().strip(),
                    'mailing_address': page.locator('#maincontent > div.searchResultDetail > div:nth-child(5)').text_content().strip(),
                    'latest_annual_report' : page.locator(' #maincontent > div.searchResultDetail > div:nth-child(10) > table > tbody > tr:nth-child(1)').get_attribute("href"),
                    'state': page.locator('#maincontent > div.searchResultDetail > div.detailSection.filingInformation > span:nth-child(2) > div > span:nth-child(10)').text_content().strip(),
                }
                #print(details)
                return details

            except Exception as e:
                print(f"Error during crawling: {str(e)}")
                return None

            finally:
                browser.close()

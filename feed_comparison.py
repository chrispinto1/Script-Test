from striprtf.striprtf import rtf_to_text
import xml.etree.ElementTree as ET
import requests
from bs4 import BeautifulSoup

RTF_FEED_PATH = 'feeds.rtf'

class FeedComparison():
    def __init__(self, rtf_feed_path: str):
        self.feed_data_as_xml = None
        self.rtf_feed_path = rtf_feed_path
        self.base_url = "https://stats-api.mlssoccer.com/matches/MLS-MAT-00067D/commentary?"
        self.commentary_data = []
        self.events_dict = {}

    def get_xml_feed(self):
        with open(self.rtf_feed_path, 'r', encoding='utf-8') as file:
            rtf_file_text = file.read()

        rtf_string = rtf_to_text(rtf_file_text)
        self.feed_data_as_xml = ET.fromstring(rtf_string)

    def compare_feed_data(self):
        if not len(self.commentary_data):
            self._get_feed_data_from_api()

        if self.feed_data_as_xml == None:
            self.get_xml_feed()
            self._build_events_dict()

        if self.commentary_data is not None and self.feed_data_as_xml is not None and len(self.events_dict):
            return

    def _add_commentary_data(self, data):
        commentary_data = data.get("commentary")
        if commentary_data and len(commentary_data):
            self.commentary_data = self.commentary_data + commentary_data

    def _build_events_dict(self):
        if not len(self.events_dict):
            events_in_feed = self.feed_data_as_xml.findall('Event')
            for event in events_in_feed:
                self.events_dict[event.attrib.get("EventId")] = event

    def _fetch_data(self, url: str):
        try:
            request = requests.get(url)
            request.raise_for_status()
            return request
        except requests.exceptions.HTTPError as e:
            # Possibly log/report depending on what the case would be for a bad request from automation (if we are hitting an internal api in the automation)
            print(f"There was an issue fetching the data. Error: {e}")

    def _get_feed_data_from_api(self):
        # This method is hard coded to the design of the api call (i.e not dynamic for all use cases/not a method to reuse for fetching other data)
        data = self._fetch_data(self.base_url)
        data = data.json() # Did this here instead of fetch_data in the event we want _fetch_data to be more universal
        if data:
            commentary_data = data.get("commentary")
            self._add_commentary_data(data)
            token = data.get("next_page_token")

            while token and len(commentary_data): #added len(commentary_data) in the extreme event token is always present (i.e bug or api design change), ensuring to stop if theres no data being returned to avoid infinite loop
                data = self._fetch_data(self.base_url + f"page_token={token}")
                data = data.json()
                self._add_commentary_data(data)
                token = data.get("next_page_token")


feed_comparison = FeedComparison(RTF_FEED_PATH)
feed_comparison.compare_feed_data()


"""

    UNUSED CODE

    Explaination of code: This is in the event I have to parse the actual HTML and not go the api route

    from selenium import webdriver
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC

    FEED_URL = 'https://www.mlssoccer.com/competitions/mls-regular-season/2025/matches/nshvsmia-10-18-2025/feed'
    
    self.feed_url = feed_url
    self.html_feed = None
    self.browser = None

    def parse_html_feed_section(self):
        if not self.html_feed:
            self.get_feed_from_url()

        feed_data = self.html_feed.find(attrs={'class': 'mls-o-match-feed'})
        return

    def get_feed_from_url(self):
        html = self._get_data_from_url_by_class_name('mls-o-match-feed', 100)
        self.browser.quit()
        self.html_feed = BeautifulSoup(html, 'html.parser')
        return

    def _get_data_from_url_by_class_name(self, class_name: str, timeout: int):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.browser = webdriver.Chrome(options=options)
        self.browser.get(self.feed_url)
        wait = WebDriverWait(self.browser, timeout=timeout)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, class_name)))
        return self.browser.page_source
"""

"""
    PREVIOUS CODE

    Explaination of why it didn't work: This works great for more static data but because the feed is generated dynamically, 
                                        needed to go a different route to get the commentary as html
    def get_feed_from_url(self):
        request = requests.get(self.feed_url)
        content_type = request.headers.get('Content-Type')
        if content_type == 'text/html':
            self.html = BeautifulSoup(browser.page_source, 'html.parser')
            return
        else:
            raise NotImplementedError('Only currently able to work with HTML content at the moment')
"""
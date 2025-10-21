from striprtf.striprtf import rtf_to_text
import xml.etree.ElementTree as ET
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

RTF_FEED_PATH = 'feeds.rtf'
FEED_URL = 'https://www.mlssoccer.com/competitions/mls-regular-season/2025/matches/nshvsmia-10-18-2025/feed'

class FeedComparison():
    def __init__(self, rtf_feed_path: str, feed_url: str):
        self.html_feed = None
        self.xml = None
        self.rtf_feed_path = rtf_feed_path
        self.feed_url = feed_url
        self.browser = None

    def get_xml_feed(self):
        with open(self.rtf_feed_path, 'r', encoding='utf-8') as file:
            rtf_file_text = file.read()

        rtf_string = rtf_to_text(rtf_file_text)
        self.xml = ET.fromstring(rtf_string)
        return

    def get_feed_from_url(self):
        html = self._get_data_from_url_by_class_name('mls-o-match-feed', 100)
        self.browser.quit()
        self.html_feed = BeautifulSoup(html, 'html.parser')
        return

    def parse_html_feed_section(self):
        if not self.html_feed:
            self.get_feed_from_url()

        feed_data = self.html_feed.find(attrs={'class': 'mls-o-match-feed'})
        return

    def _get_data_from_url_by_class_name(self, class_name: str, timeout: int):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.browser = webdriver.Chrome(options=options)
        self.browser.get(self.feed_url)
        wait = WebDriverWait(self.browser, timeout=timeout)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, class_name)))
        return self.browser.page_source

feed_comparison = FeedComparison(RTF_FEED_PATH, FEED_URL)
feed_comparison.parse_html_feed_section()

"""
    NOTES:

    possible apis available to read from:

    GET - https://stats-api.mlssoccer.com/matches/MLS-MAT-00067D/commentary? - 
    This is a bit more work as there's no images returned in this version
"""

"""
    UNUSED PREVIOUS CODE

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
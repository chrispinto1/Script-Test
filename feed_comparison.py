from striprtf.striprtf import rtf_to_text
import xml.etree.ElementTree as ET
import requests
from bs4 import BeautifulSoup

RTF_FEED_PATH = 'feeds.rtf'
FEED_URL = 'https://www.mlssoccer.com/competitions/mls-regular-season/2025/matches/nshvsmia-10-18-2025/feed'

class FeedComparison():
    def __init__(self, rtf_feed_path: str, feed_url: str):
        self.html = None
        self.xml = None
        self.rtf_feed_path = rtf_feed_path
        self.feed_url = feed_url

    def get_xml_feed(self):
        with open(self.rtf_feed_path, 'r', encoding='utf-8') as file:
            rtf_file_text = file.read()

        rtf_string = rtf_to_text(rtf_file_text)
        self.xml = ET.fromstring(rtf_string)
        return

    def get_feed_from_url(self):
        request = requests.get(self.feed_url)
        content_type = request.headers.get('Content-Type')
        if content_type == 'text/html':
            self.html = BeautifulSoup(request.text)
            return
        else:
            raise NotImplementedError('Only currently able to work with HTML content at the moment')

feed_comparison = FeedComparison(RTF_FEED_PATH, FEED_URL)

"""
    NOTES:

    possible apis available to read from:

    GET - https://stats-api.mlssoccer.com/matches/MLS-MAT-00067D/commentary? - 
    This is a bit more work as there's no images returned in this version
"""
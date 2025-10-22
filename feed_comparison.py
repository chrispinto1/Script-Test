from striprtf.striprtf import rtf_to_text
import xml.etree.ElementTree as ET
import requests
import sys

RTF_FEED_PATH = './assets/feeds.rtf'
BASE_API_URL = 'https://stats-api.mlssoccer.com/matches/MLS-MAT-00067D/commentary?'
class FeedComparison():
    def __init__(self, rtf_feed_path: str, base_api_url: str):
        """
            Sets the following instance attributes

            feed_data_as_xml -> None
            rtf_feed_path -> The Path given in the first parameter
            base_api_url -> The url given in the second parameter
            api_response_data -> None
            events_dict -> {} empty dictionary -> It will have the following format 
                {
                    commentary: List<Event>
                    match_info: Dictionary
                    next_page_token: String - Will be present only if there's a next page in the pagination
                }
        """
        self.feed_data_as_xml = None
        self.rtf_feed_path = rtf_feed_path
        self.base_api_url = base_api_url
        self.api_response_data = None
        self.events_dict = {}

    def get_xml_feed(self):
        """
            This method opens the RTF file and gets the xml version of the content.
        """
        with open(self.rtf_feed_path, 'r', encoding='utf-8') as file:
            rtf_file_text = file.read()

        try:
            rtf_string = rtf_to_text(rtf_file_text)
            self.feed_data_as_xml = ET.fromstring(rtf_string)
        except:
            print("Unable to convert the RTF file content to XML")

    def compare_feed_data(self, get_full_report: bool):
        """
            Parameters:

            get_full_report (default = False) - A boolean type, which is determine the type of response you get back from the method.
                                                If set to true, it will get all the data that isn't included and display it or will 
                                                display all match. If false, it will get just check if any match and return true and false

            This method will do the following:
            
            1. Get the feed data from the api if the api_response_data attribute is None
            2. Get the xml data from the file
            3. return either if any match or which are missing based on the parameter get_full_report explained above
        """
        if not self.api_response_data:
            self._get_feed_data_from_api(get_full_report)

        if self.feed_data_as_xml == None:
            self.get_xml_feed()
            self._build_events_dict()

        if self.api_response_data is not None and self.feed_data_as_xml is not None and len(self.events_dict):
            if get_full_report:
                events_not_included = []
                for commentary in self.api_response_data.get('commentary'):
                    if commentary["event_id"] not in self.events_dict:
                        events_not_included.append(commentary["event_id"])
                if len(events_not_included):
                    return f"The following events are not included in the XML feed: {", ".join(events_not_included)}"
                else:
                    return "All the events are included in the xml feed"
            else:
                return self._check_for_matching_data()

    def _set_response_data(self, data):
        """
            This method sets the api_response_data attribute to the data passed in
        """
        self.api_response_data = data

    def _build_events_dict(self):
        """
            This method builds a dictionary with the RTF file given with the xml in its content.
            The dictionary will be built out as

            {
                ["eventId"] = Event_element
            }

            This is in the event you need to do more with the event element based on event ids
        """
        if not len(self.events_dict):
            events_in_feed = self.feed_data_as_xml.findall('Event')
            for event in events_in_feed:
                self.events_dict[event.attrib.get('EventId')] = event

    def _check_for_matching_data(self):
        """"
            This method will find if any matches are found the the api feed and the RTF file.
            If there's no matches with the current set of data, it will reach out to the next
            available link and set the data until theres a match.

            This method returns True or False
        """
        commentary_data = self.api_response_data.get('commentary')
        while True:
            for commentary in commentary_data:
                if commentary['event_id'] in self.events_dict:
                    return True

            token = self.api_response_data.get("next_page_token")
            if token:
                self.api_response_data = self._fetch_data(self.base_url + f'page_token={token}')
                commentary_data = self.api_response_data.get('commentary')

            return False

    def _fetch_data(self, url: str):
        """
            Parameters:
                url: string

            This method fetches data from the url given and ensures it returned ok, if not it will return an error message
        """
        try:
            request = requests.get(url)
            request.raise_for_status()
            return request
        except requests.exceptions.HTTPError as e:
            # Possibly log/report depending on what the case would be for a bad request from automation (if we are hitting an internal api in the automation)
            print(f"There was an issue fetching the data. Error: {e}")

    def _get_feed_data_from_api(self, get_full_report: bool):
        """

            Parameters:
                get_full_report - boolean

            This method gets the data from the api url and get the full data before moving forward if the get_full_report
            parameter is set to True
        """
        
        data = self._fetch_data(self.base_url)
        data = data.json()
        if data:
            self._set_response_data(data)
            if get_full_report:
                commentary_data = data.get("commentary")
                token = data.get("next_page_token")
                while token and len(commentary_data):
                    data = self._fetch_data(self.base_url + f"page_token={token}")
                    data = data.json()
                    self._set_response_data(data)
                    token = data.get("next_page_token")

if __name__ == "__main__":
    get_full_report = False
    if len(sys.argv) > 1:
        arg_val = sys.argv[1]
        if arg_val.lower() == "true":
            get_full_report = True

    print(FeedComparison(RTF_FEED_PATH, BASE_API_URL).compare_feed_data(get_full_report))


"""

    UNUSED CODE

    Explaination of code: This is code I worked on trying to parse the HTML and not using 
                          the api (as I'm not exactly sure of the ask due to images not being 
                          part of the api call response without merging more than 1 call)

    from bs4 import BeautifulSoup
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
from striprtf.striprtf import rtf_to_text
import xml.etree.ElementTree as ET


RTF_FILE = 'feeds.rtf'
XML_FILE = 'feeds.xml'

def get_xml_from_rtf(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        rtf_file_text = file.read()

    rtf_string = rtf_to_text(rtf_file_text)
    xml = ET.fromstring(rtf_string)

    return xml

print(get_xml_from_rtf(RTF_FILE))
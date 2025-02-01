import os
import xml.etree.ElementTree as ET

def extract_security_logs():
    print("Extracting Windows Security Logs...")
    os.system('wevtutil qe Security /f:xml > windows_logs.xml')

    tree = ET.parse('windows_logs.xml')
    root = tree.getroot()

    for event in root.findall('.//Event'):
        event_id = event.find('.//EventID').text
        time_created = event.find('.//TimeCreated').attrib.get('SystemTime')
        print(f"Event ID: {event_id} | Time: {time_created}")

if __name__ == "__main__":
    extract_security_logs()

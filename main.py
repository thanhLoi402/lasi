import xml.etree.ElementTree as ET
import change_format_data as fx
try:
    root = ET.parse('etc/config.xml').getroot()
    for child in root:
        try:
            print("===========Start read "+child.get('name') + "================")
            print("partDiv:"+child.find('partDiv').text)
            print("partLog:"+child.find('partLog').text)
            print("oldFormat:"+child.find('oldFormat').text)
            print("newFormat:"+child.find('newFormat').text)
            fx.change_format(child.find('partDiv').text, child.find('partLog').text, child.find('oldFormat').text, child.find('newFormat').text)
            print("===========End read "+child.get('name') + "================")
        except:
            print("ERROR change fomat data!!!")
except:
    print("ERROR file ./etc/config.xml not format")
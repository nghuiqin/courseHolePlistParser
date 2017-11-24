import os
import xml.etree.ElementTree as ET
import sys
reload(sys)
sys.setdefaultencoding('utf8')

path = './greenXML'
pathOutput = './greenPLIST'

for readFileName in os.listdir(path) :
    if not readFileName.endswith('.kml.xml'): continue
    fullname = os.path.join(path, readFileName)
    writeFileName = readFileName.replace('Tee_Green_Position_', '').replace('.kml.xml', '_Holes_GPS_Points_Colored_Tees.plist')
    writeFilePath = os.path.join(pathOutput, writeFileName)

    tree = ET.parse(fullname)
    root = tree.getroot()

    writeFile = open(writeFilePath, 'w')

    writeFile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    writeFile.write('<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n')
    writeFile.write('<plist version="1.0">\n')
    writeFile.write('<dict>\n')

    namespace = '{http://www.opengis.net/kml/2.2}'
    document = root.find(namespace + 'Document')
    for item in document.findall(namespace + 'Placemark') :
        name = item.find(namespace + 'name')
        coordinates = item.find(namespace + 'Point').find(namespace + 'coordinates')
        array = coordinates.text.strip().split(',0')

        writeFile.write('    <key>' + name.text + '</key>\n')
        writeFile.write('    <array>\n')
        for coordinate in array :
            location = coordinate.strip().split(',')
            if location[0]:
                lon = location[0]
                lat = location[-1]
                writeFile.write('        <real>' + lat + '</real>\n')
                writeFile.write('        <real>' + lon + '</real>\n')

        writeFile.write('    </array>\n')

    writeFile.write('</dict>\n')
    writeFile.write('</plist>\n')

    print "file: ", readFileName, "is done."


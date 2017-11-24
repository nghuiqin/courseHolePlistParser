eadFileName = 'HoleArea.kml.xml'
writeFileName = 'output.plist'

import xml.etree.ElementTree as ET
tree = ET.parse(readFileName)
root = tree.getroot()

import sys
reload(sys)
sys.setdefaultencoding('utf8')

writeFile = open(writeFileName, 'w')

writeFile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
writeFile.write('<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n')
writeFile.write('<plist version="1.0">\n')
writeFile.write('<dict>\n')

namespace = '{http://www.opengis.net/kml/2.2}'
document = root.find(namespace + 'Document')
for item in document.findall(namespace + 'Placemark') :
    name = item.find(namespace + 'name')
    coordinates = item.find(namespace + 'Polygon').find(namespace + 'outerBoundaryIs').find(namespace + 'LinearRing').find(namespace + 'coordinates')
    array = coordinates.text.split(',0')

    longitude = []
    latitude = []
    for coordinate in array :
         location = coordinate.strip().split(',')
         lon = location[0]
         lat = location[-1]
         longitude.append(lon)
         latitude.append(lat)

    writeFile.write('       <key>' + name.text + '_latitude' + '</key>\n')
    writeFile.write('       <array>\n')
    for number in latitude :
        writeFile.write('               <real>' + number + '</real>\n')

    writeFile.write('       </array>\n')

    writeFile.write('       <key>' + name.text + '_longitude' + '</key>\n')
    writeFile.write('       <array>\n')
    for number in longitude :
        writeFile.write('               <real>' + number + '</real>\n')

    writeFile.write('       </array>\n')

writeFile.write('</dict>\n')
writeFile.write('</plist>\n')


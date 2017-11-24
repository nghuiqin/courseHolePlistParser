import xml.etree.ElementTree as ET
tree = ET.parse('HoleArea.kml.xml')
root = tree.getroot()

namespace = '{http://www.opengis.net/kml/2.2}'
document = root.find(namespace + 'Document')
for item in document.findall(namespace + 'Placemark') :
    name = item.find(namespace + 'name')
    print name.text
    coordinates = item.find(namespace + 'Polygon').find(namespace + 'outerBoundaryIs').find(namespace + 'LinearRing').find(namespace + 'coordinates')
    print  coordinates.text


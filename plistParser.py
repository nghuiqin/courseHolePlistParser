import xml.etree.ElementTree as ET
tree = ET.parse('HoleArea.kml.xml')
root = tree.getroot()

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
         long = location[0]
         lat = location[-1]
         longitude.append(long)
         latitude.append(lat)

    print name.text + '_latitude'
    for number in latitude :
        print number

    print name.text + '_longitude'
    for number in longitude :
        print number


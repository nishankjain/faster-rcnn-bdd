from __future__ import with_statement
import ijson
from xml.etree.ElementTree import Element, SubElement, Comment, tostring, ElementTree
from xml.etree import ElementTree as ET
from xml.dom import minidom

f = open("bdd-data/labels/bdd100k_labels_images_train.json")

counter = 0
exc_counter = 0

for item in ijson.items(f, "item"):
    img = item["name"]
    annotation = Element('annotation')
    tree = ElementTree(annotation)
    filename = SubElement(annotation, 'filename')
    filename.text = img
    for o in item["labels"]:
        if 'box2d' in o:
            object = SubElement(annotation, 'object')
            name = SubElement(object, 'name')
            name.text = o['category']
            d = SubElement(object, 'difficult')
            d.text = '0'
            box = SubElement(object, 'bndbox')
            xmin = SubElement(box, 'xmin')

            xmin.text = str(round(o['box2d']['x1']))
            ymin = SubElement(box, 'ymin')
            ymin.text = str(round(o['box2d']['y1']))
            xmax = SubElement(box, 'xmax')
            xmax.text = str(round(o['box2d']['x2']))
            ymax = SubElement(box, 'ymax')
            ymax.text = str(round(o['box2d']['y2']))

    x = minidom.parseString(ET.tostring(annotation)).toprettyxml()
    try:
        with open("data/bdd_data/Annotations/"+img[:-4]+'.xml', 'w') as p:
            p.write(x)
            counter += 1
    except EnvironmentError:
        print(img)
        exc_counter += 1

print(counter)
print(exc_counter)

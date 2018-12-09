
import ijson
from xml.etree.ElementTree import Element, SubElement, Comment, tostring,ElementTree
from xml.etree import ElementTree as ET
from xml.dom import minidom


f = open("bdd100k/labels/bdd100k_labels_images_val.json")

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
    with open("bdd100k/lab/"+img[:-4]+'.xml', 'w') as p:
        p.write(x)

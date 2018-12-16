import ijson

f = open("bdd-data/labels/bdd100k_labels_images_val.json")

test_images_list = []

counter = 0

for item in ijson.items(f, "item"):
    img = item["name"]
    test_images_list.append(img[:-4])
    counter += 1

x = "\n".join(test_images_list)

with open("data/bdd_data/ImageSets/Main/test.txt", 'w') as p:
    p.write(x)

print(counter)
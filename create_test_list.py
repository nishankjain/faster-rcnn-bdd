import ijson

f = open("bdd-data/labels/bdd100k_labels_images_val.json")

test_images_list = []

counter = 0

for item in ijson.items(f, "item"):
    img = item["name"]
    test_images_list.append(img[:-4])
    counter += 1
    if counter == 1000:
        break

x = "\n".join(test_images_list)

with open("data/bdd_data/ImageSets/Main/testinitial.txt", 'w') as p:
    p.write(x)

print(counter)

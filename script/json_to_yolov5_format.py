import json
import os
import glob
import shutil



cat_dict = {
    "tank": 1,
    "car": 2,
    "truck": 3,
    "boat": 4,
    "airplane":5,
    "horse trailer" : 6,
    "train": 7,
    "motorcycle": 8,
    "Unknow": 9
}



file_dir = "/mnt/1028D91228D8F7A4/SUS/annotated/watched/vott-json-export" #directory with all the file
save_json = "/mnt/1028D91228D8F7A4/SUS_model/yolor/dataset/original_dataset" #ouptut_directory
#get the file information
files_png = glob.glob(file_dir + "/*.png")
for f in files_png:
    shutil.copy(f, save_json)


#json file position with all the annotation
json_file = "/mnt/1028D91228D8F7A4/SUS/annotated/watched/vott-json-export/SUS-project-export.json"
with open(json_file) as f:
    imgs_anns = json.load(f)

#move label 

save_json = "/mnt/1028D91228D8F7A4/SUS_model/yolor/dataset/original_dataset/labels" #ouptut_directory
height, width = 1080, 1440
for image_data in imgs_anns["assets"].values():
    print(image_data)
    name = image_data["asset"]["name"].split(".")[0]
    f = open(os.path.join(save_json, f'{name}.txt'), "w+")
    num_regions = len(image_data["regions"])
    print(num_regions)
    for i in range(num_regions):
        category = cat_dict[image_data["regions"][i]["tags"][0]]
        x_center = (image_data["regions"][i]["boundingBox"]["left"] + (image_data["regions"][i]["boundingBox"]["width"] / 2)) / width
        y_center = (image_data["regions"][i]["boundingBox"]["top"] + (image_data["regions"][i]["boundingBox"]["height"] / 2)) / height
        w = image_data["regions"][i]["boundingBox"]["width"] / width
        h = image_data["regions"][i]["boundingBox"]["height"] / height
        f.write(f"{category} {x_center} {y_center} {w} {h} \n")


#move images
images = "/mnt/1028D91228D8F7A4/SUS/annotated/watched/vott-json-export"
save_images_dir = "/mnt/1028D91228D8F7A4/SUS_model/yolor/dataset/original_dataset/images"


for file in glob.iglob(os.path.join(images, "*.png")) :
    shutil.copy(file, save_images_dir)
    print(f"file: {file} copied")

'''
The purpose of this script is to get the labels from the json file and create the coco annotation files, and to put that
in the right directory
'''


import re
import os
import cv2
import json
import itertools
import numpy as np
from glob import glob
import scipy.io as sio
from pycocotools import mask as cocomask
from PIL import Image

#setup information
categories = [
    {"supercategory": "none", "name": "tank", "id": 1, "color": "#5db300"},
    {"supercategory": "none", "name": "car", "id": 2, "color": "#e81123"},
    {"supercategory": "none", "name": "truck", "id": 3, "color": "#6917aa"},
    {"supercategory": "none", "name": "boat", "id": 4, "color": "#015cda"},
    {"supercategory": "none", "name": "airplane", "id": 5, "color": "#4894fe"},
    {"supercategory": "none", "name": "horse trailer", "id": 6, "color": "#4894fe"},
    {"supercategory": "none", "name": "train", "id": 7, "color": "#4894fe"},
    {"supercategory": "none", "name": "motorcycle", "id": 8, "color": "#4894fe"},
    {"supercategory": "none", "name": "Unknow", "id": 9, "color": "#4894fe"},
]

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


phases = ["train", "val", "test"]

# The current code contains the directory information for which you want to create the annotation file in COCO format

#path_directory = "/mnt/1028D91228D8F7A4/SUS_model/yolor/dataset/original_dataset/images/test_dir"
#path_directory = "/mnt/1028D91228D8F7A4/SUS_model/yolor/dataset/original_dataset/images/train_dir"
path_directory = "/mnt/1028D91228D8F7A4/SUS_model/yolor/dataset/original_dataset/images/val_dir"


file_to_check = os.listdir(path_directory)

image_file = '/mnt/1028D91228D8F7A4/SUS/annotated/watched/vott-json-export/8452_(NARA_LID-111-SFR-53-R03_MPPC_NAID-36151_OFMID-1603892600524_H264_1440x1080_AAC-stereo_24fps_12Mbit_GOP01_crop_AC_VHH-P_OFM_2022-01-12_sid_77_pos_6873_ELS.png'

#open json file
json_file = "/mnt/1028D91228D8F7A4/SUS/annotated/watched/vott-json-export/SUS-project-export.json"
with open(json_file) as f:
    imgs_anns = json.load(f)


#save_json = "/home/giuseppe/Scrivania/test2017.json"
#save_json = "/home/giuseppe/Scrivania/train2017.json"
save_json = "/home/giuseppe/Scrivania/val2017.json"


id = 0
annot_count = 0
res_file = {
    "categories": categories,
    "images": [],
    "annotations": []
}

for image_data in imgs_anns["assets"].values():
    if len(image_data["regions"]) == 0:
        continue
    else:
    #check if the file with the annotation is in the current examined directory
        file_name = image_data["asset"]["name"] # name of the file I am checking in
        #print(f"file_name: {file_name}")
        if file_name not in file_to_check:
            continue
            
        else:
            #process image if "regions" in image is not empty, only if there are annotations
            height, width = cv2.imread(image_file).shape[:2]
            img_elem = {
                "file_name": image_data["asset"]["name"],
                "height": image_data["asset"]["size"]["height"],
                "width": image_data["asset"]["size"]["width"],
                "id": id
            }

            res_file["images"].append(img_elem)
            num_regions = len(image_data["regions"])
        
            for i in range(num_regions):
                poly = [[int(image_data["regions"][i]["points"][0]["x"]), int(image_data["regions"][i]["points"][0]["y"])],
                    [int(image_data["regions"][i]["points"][1]["x"]), int(image_data["regions"][i]["points"][1]["y"])],
                    [int(image_data["regions"][i]["points"][2]["x"]), int(image_data["regions"][i]["points"][2]["y"])],
                    [int(image_data["regions"][i]["points"][3]["x"]), int(image_data["regions"][i]["points"][3]["y"])]
                    ]
                annot_elem = {
                "id": annot_count,
                "image_id": id,
                "category_id": cat_dict[image_data["regions"][i]["tags"][0]],
                "bbox": [image_data["regions"][i]["boundingBox"]["left"], image_data["regions"][i]["boundingBox"]["top"], 
                image_data["regions"][i]["boundingBox"]["width"] + image_data["regions"][i]["boundingBox"]["left"], 
                image_data["regions"][i]["boundingBox"]["height"] + image_data["regions"][i]["boundingBox"]["top"]],
                "area": width*height,
                "segmentation": list([poly]),
                "iscrowd": 0
                }
                res_file["annotations"].append(annot_elem)
                annot_count += 1
            id += 1

#print(len(res_file["images"]), len(res_file["annotations"]))

with open(save_json, "w") as f:
    json_str = json.dumps(res_file)
    f.write(json_str)

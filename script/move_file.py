import glob
import os
import numpy as np
import sys
import shutil


'''
The purpose of the following script is 
to divide the dataset into train and test set, and to move the file in the 
proper directory.
'''
#directory to get the images
default_dir = "/mnt/1028D91228D8F7A4/SUS_model/yolor/dataset/original_dataset/images"

#directory to get the labels
labels_dir = "/mnt/1028D91228D8F7A4/SUS_model/yolor/dataset/original_dataset/labels" 

#final directory for the images
train_dir  = "/mnt/1028D91228D8F7A4/SUS_model/yolor/dataset/original_dataset/images/train_dir"
test_dir = "/mnt/1028D91228D8F7A4/SUS_model/yolor/dataset/original_dataset/images/test_dir"
val_dir = "/mnt/1028D91228D8F7A4/SUS_model/yolor/dataset/original_dataset/images/val_dir"

#final directory for the labels
train_dir_labels  = "/mnt/1028D91228D8F7A4/SUS_model/yolor/dataset/original_dataset/labels/train_dir"
test_dir_labels = "/mnt/1028D91228D8F7A4/SUS_model/yolor/dataset/original_dataset/labels/test_dir"
val_dir_labels = "/mnt/1028D91228D8F7A4/SUS_model/yolor/dataset/original_dataset/labels/val_dir"



#file = glob.glob(os.path.join(default_dir, "*.png"))
file = [x for x in os.listdir(default_dir) if x.endswith(".png")]

#calculating the splitting point
split_percentage = 0.7
i = 0

#fill in the train file
for _ in range(round(len(file) * split_percentage)):
    shutil.copyfile(os.path.join(default_dir,file[i]), os.path.join(train_dir,file[i]))
    #create the labels name and copy the file
    labels_name = file[i].replace(".png" , ".txt")
    shutil.copyfile(os.path.join(labels_dir,labels_name), os.path.join(train_dir_labels,labels_name))
    i+=1


#fill the test file
for _ in range(round((len(file) * (1 - split_percentage) / 2))):
    shutil.copyfile(os.path.join(default_dir,file[i]), os.path.join(test_dir,file[i]))
    #create the labels name and copy the file
    labels_name = file[i].replace(".png" , ".txt")
    shutil.copyfile(os.path.join(labels_dir,labels_name), os.path.join(test_dir_labels,labels_name))
    i+=1

#fill the validation file
for _ in range(round((len(file) * (1 - split_percentage) /2))):
    shutil.copyfile(os.path.join(default_dir,file[i]), os.path.join(val_dir,file[i]))
    #create the labels name and copy the file
    labels_name = file[i].replace(".png" , ".txt")
    shutil.copyfile(os.path.join(labels_dir,labels_name), os.path.join(val_dir_labels,labels_name))
    i+=1




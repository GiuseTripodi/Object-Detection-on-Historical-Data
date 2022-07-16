# Object Detcion On Historical Data

This archive contains the work for the lesson Scene Understanding & Surveillance (SUS) 2022. We detect various vehicles in historical film shots by using the three following methodologies as basis:

- [YOLOR](https://github.com/augmentedstartups/yolor)
- [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX)
- [RetinaNet](https://github.com/benihime91/pytorch_retinanet)

## Installation


The project was mainly carried out on Google Colab, so no special installation is required.

The only requirement is to have a **Google account**, and thus access to the following two platforms:
- [Google Drive](https://www.google.at/drive/about.html)
- [Google Colab](https://colab.research.google.com/?utm_source=scs-index)

## Usage

To run the notebook, proceed as follows
1. clone the repository on your device
2. open each notebook on [Google Colab](https://research.google.com/colaboratory/)
3. copy the following directory (that you can find on the repository) to your [Google Drive](https://drive.google.com/drive/my-drive) (directories must be placed under the "MyDrive" directory)
    - [**dataset**](dataset): For inference the dataset on GitHub is fine, but if you want to do Trainining and Testing you have to load the complete datast. The correct folder structure is specified below. (Unzip the folder before copying it)
    - [**configuration_file_SUS_project**](configuration_file_SUS_project)
    - WEIGHTS: To make inference with the pre-trained weights, you must also add the directory containing all weights. The structure this directory should have is specified in the notebooks.

You can now run each notebook without any problems.

At some point during execution you will be asked to give access to your Google Drive account, you will have to grant this access.

After that, you will be able to observe the execution on each notebook. Note that the directory names must be exactly as stated above.


## Usage on Custom Dataset

To use models on a custom dataset, first prepare the directory containing the dataset. The dataset directory must be organized on the following way:

```
dataset
└─── original dataset
|   |
|   └─── images
|   |   |
|   |   └─── test_dir
|   |   └─── train_dir
|   |   └─── val_dir
|   |
|   |
|   └─── labels
|   |   |
|   |   └─── test_dir
|   |   └─── train_dir
|   |   └─── val_dir

```

Under images each directory contains all the images used as training, validation and test sets. Under labels each directory contains the labels for each image. 
The image and its labels must have the same name.

The scripts in the [script](script) directory can be used to manage the dataset, and possibly convert the annotations.



## References
We build our project on the following repositories:

- [YOLOR](https://github.com/augmentedstartups/yolor)
```
@misc{https://doi.org/10.48550/arxiv.2105.04206,
  doi = {10.48550/ARXIV.2105.04206},
  
  url = {https://arxiv.org/abs/2105.04206},
  
  author = {Wang, Chien-Yao and Yeh, I-Hau and Liao, Hong-Yuan Mark},
  
  keywords = {Computer Vision and Pattern Recognition (cs.CV), FOS: Computer and information sciences, FOS: Computer and information sciences},
  
  title = {You Only Learn One Representation: Unified Network for Multiple Tasks},
  
  publisher = {arXiv},
  
  year = {2021},
  
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```
- [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX)
```
@misc{https://doi.org/10.48550/arxiv.2107.08430,
  doi = {10.48550/ARXIV.2107.08430},
  
  url = {https://arxiv.org/abs/2107.08430},
  
  author = {Ge, Zheng and Liu, Songtao and Wang, Feng and Li, Zeming and Sun, Jian},
  
  keywords = {Computer Vision and Pattern Recognition (cs.CV), FOS: Computer and information sciences, FOS: Computer and information sciences},
  
  title = {YOLOX: Exceeding YOLO Series in 2021},
  
  publisher = {arXiv},
  
  year = {2021},
  
  copyright = {arXiv.org perpetual, non-exclusive license}
}


```
- [RetinaNet](https://github.com/facebookresearch/detr/blob/main/README.md)
```
@misc{https://doi.org/10.48550/arxiv.1708.02002,
  doi = {10.48550/ARXIV.1708.02002},
  
  url = {https://arxiv.org/abs/1708.02002},
  
  author = {Lin, Tsung-Yi and Goyal, Priya and Girshick, Ross and He, Kaiming and Dollár, Piotr},
  
  keywords = {Computer Vision and Pattern Recognition (cs.CV), FOS: Computer and information sciences, FOS: Computer and information sciences},
  
  title = {Focal Loss for Dense Object Detection},
  
  publisher = {arXiv},
  
  year = {2017},
  
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

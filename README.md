# Implementation of Faster R-CNN For Object Detection On Berkeley Deep Drive dataset

## Setup Instructions

* Install CUDA 9.0
* Install NVIDIA Driver 390
* Add CUDA paths to the bashrc file
* Create *data* directory
* Create *bdd_data* inside *data*
* Create *ImageSets*, *JPEGImages*, *Annotations* and *results* directory inside *bdd_data*
* Create *Main* directory inside *ImageSets*
* Copy all training and validation images from BDD100k images to *JPEGImages*
* Run *create_val_list* and *create_train_list*

For other implementation details, obtaining pretrained models and setup, refer https://github.com/jwyang/faster-rcnn.pytorch

For obtaining the BDD dataset, visit http://bdd-data.berkeley.edu

Get models, results, annotations and detections from https://drive.google.com/drive/folders/1v7qRDaLZqXINDbTPERYI_FNQOv6ukjFJ

## Instance Segmentation using YOLOv11

**Author: Abhishek Dey**


### About:

In this work, an instance segmentation model is developed using [YOLOv11](https://docs.ultralytics.com/models/yolo11/) 

### Dataset:

[ROBOFLOW Bottle Detection dataset](https://universe.roboflow.com/hh-hh-nfwyj/bottle-gl3ty) dataset is considered for training the YOLO instance segmentation model. The dataset is split into the following:

* train - 587 images

* valid - 167 images

* test - 84 images


### Create virtual environment

```
conda create -n yolo_env python 3.10

pip3 install -r requirements.txt

```

### Follow the notebook:

[yolo-instance-segmentation.ipynb](yolo-instance-segmentation.ipynb)

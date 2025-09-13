## Vehicle number plate detection and recognition using YOLOv11 and EasyOCR

**Author: Abhishek Dey**


### About:

In this work, a vehicle number plate detection and recognition system is developed using [YOLOv11](https://docs.ultralytics.com/models/yolo11/) and [EasyOCR](https://github.com/JaidedAI/EasyOCR)

### Dataset:

**[ROBOFLOW License Plate Recognition]**(https://universe.roboflow.com/roboflow-universe-projects/license-plate-recognition-rxg4e) dataset is considered for training the YOLO number plate detection model. The dataset is split into the following:

* train - 7057 images

* val - 2048 images

* test - 1020 images

### Pipeline

* Given a input image

* Detect the number plate bounding box using YOLO

* The number plate bounding box is cropped, enhanced and passed to the EasyOCR for recogition

* Finally the detected and recognised number plate is displayed

### Create virtual environment

```
conda create -n yolo_env python 3.10

pip3 install -r requirements.txt

```

### Follow the notebook:

[number-plate-det-recog.ipynb](number-plate-det-recog.ipynb)

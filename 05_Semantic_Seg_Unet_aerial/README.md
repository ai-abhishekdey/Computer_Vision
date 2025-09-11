## U-Net Semantic Segmentation on aerial imagery

**Author: Abhishek Dey**

## Dataset

* Download [Semantic segmentation of aerial imagery](https://www.kaggle.com/datasets/humansintheloop/semantic-segmentation-of-aerial-imagery) dataset from Kaggle. 

* Total images: 72

* No. of classes: 6

* Class Names: **Building, Land, Road, Vegetation, Water, Unlabeled**

## Data Pre-processing:

* Unzip the downloaded dataset

### Separate out images and masks and split the dataset

```
python3 prepare_and_split_dataset.py --root_dir archive/Semantic\ segmentation\ dataset/ --output_dir aerial_image_dataset --seed 42 --split 0.8 0.1 0.1


```

* Frame count after splitting

  * Train set : 57
  * Val set   : 7
  * Test set  : 8
  

## Conda environment

```

create conda -n unet_env python=3.10 -y

pip3 install -r requirements.txt

```

## Run Jupyter Notebook:

* [unet-aerial-dataset.ipynb](unet-aerial-dataset.ipynb)

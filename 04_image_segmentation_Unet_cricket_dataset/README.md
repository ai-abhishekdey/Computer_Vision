## U-Net Semantic Segmentation on Cricket dataset

**Author: Abhishek Dey**

## Dataset

* Download [Cricket (Semantic Segmentation)](https://www.kaggle.com/datasets/sadhliroomyprime/cricket-semantic-segmentation/data) dataset from Kaggle. The dataset is created by taking every 12th frame from the 3rd ODI cricket match highlights between India v/s Zimbabwe

* Total images: 298

* No. of classes: 9

* Class Names: **Batsman, Bowler, Wicket Keeper, Fielder, Ball, Umpire, Wicket, Ground, and Background**


Dataset Credit: Acme AI Ltd. (www.acmeai.tech)


## Data Pre-processing:

* Unzip the downloaded dataset

### Separate out images and masks

* List images

```
ls archive/www.acmeai.tech\ ODataset\ 4\ -\ Cricket\ Semantic\ Segmentation/images/ | grep ".png" | grep -v "__" > images.list

```

* List masks

```
ls archive/www.acmeai.tech\ ODataset\ 4\ -\ Cricket\ Semantic\ Segmentation/images/ | grep "fuse" > masks.list


```

### Split the dataset

* Using the below script, **split the dataset into train, val, test sets in 70:10:20 ratio**

```
python3 split_dataset.py --src_images cricket_dataset/images/ --src_masks cricket_dataset/masks/ --dst_dir cricket_dataset/ --seed 42 --split 0.7 0.1 0.2

```

* Frame count after splitting

  * Train set : 208
  * Val set   : 29
  * Test set  : 61
  

## Conda environment

```

create conda -n unet_env python=3.10 -y

pip3 install -r requirements.txt

```

## Run Jupyter Notebook:

* [unet-cricket-dataset.ipynb](unet-cricket-dataset.ipynb)

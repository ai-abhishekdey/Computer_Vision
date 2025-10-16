## Unlabelled image data segregation using K-Means clustering

**Author: Abhishek Dey**

**Date: 16 Oct 2025**

### Problem Statement:

Given a huge unlabelled image dataset, how do you segregate the data in order to build an image classification model

### Proposed Solution:

* Download the unlabelled dataset. For this experimentation, [fashion-product-images-small](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-small/data) is considered from Kaggle

* Load **facebook/dinov2-base**  Model

* Extract embeddings from DINOv2 model

* Visualize Sample Images & Corresponding DINOv2 Feature Maps

* Use **Elbow method** to get an estimate of the possible no. of clusters (K). If you have prior knowledge of the no. of classes then estimation using elbow method can be skipped

* Using the extracted embeddings perform K-means clustering and segregate the image data into K-Clusters

* The Created clusters won't be very accurate but it would give one level of automated data filtering and manual filtering is required on top of the clustering

* Once the clusters are filtered then labels can be assigned against each cluster and downstream image classification task can be performed 

### Experimentation:

This experimentation is carried out in Kaggle. The notebook can be found [here](k-means-clustering.ipynb)

### Observations:

The quality of segregating the unlabelled images using the proposed DINOv2 embeddings based clustering approach is pretty good. Below is a sample example of the clusters.

<p align="left">
<img src="cluster_visualization.png" width="1080" height="1920">
</p>


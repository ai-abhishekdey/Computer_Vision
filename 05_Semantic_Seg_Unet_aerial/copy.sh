#!/bin/bash


src_path="archive/www.acmeai.tech ODataset 4 - Cricket Semantic Segmentation/images"

dst_path="cricket_dataset/masks"

input_file="masks.list"

mkdir -p "$dst_path"


while IFS= read -r line; do
    
    cp "$src_path/$line" "$dst_path/"

done < $input_file


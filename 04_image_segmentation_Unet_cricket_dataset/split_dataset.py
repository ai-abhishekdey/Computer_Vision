import os
import shutil
import random
import argparse

# ---------------- ARGPARSE ----------------
parser = argparse.ArgumentParser(description="Split images and masks into train/val/test folders")
parser.add_argument("--src_images", type=str, required=True, help="Source images directory")
parser.add_argument("--src_masks", type=str, required=True, help="Source masks directory")
parser.add_argument("--dst_dir", type=str, required=True, help="Destination directory for splits")
parser.add_argument("--seed", type=int, default=42, help="Random seed for reproducibility")
parser.add_argument("--split", type=float, nargs=3, default=[0.7, 0.1, 0.2],
                    help="Train/Val/Test split ratios, e.g., 0.7 0.1 0.2")
args = parser.parse_args()
# ------------------------------------------

train_ratio, val_ratio, test_ratio = args.split
assert abs(train_ratio + val_ratio + test_ratio - 1.0) < 1e-6, "Split ratios must sum to 1"

# Make destination folders
for split in ["train", "val", "test"]:
    os.makedirs(os.path.join(args.dst_dir, split, "images"), exist_ok=True)
    os.makedirs(os.path.join(args.dst_dir, split, "masks"), exist_ok=True)

# Collect base images (ignore files with '__')
all_images = sorted([f for f in os.listdir(args.src_images)
                     if f.endswith(".png") and "__" not in f])

# Shuffle with fixed seed
random.seed(args.seed)
random.shuffle(all_images)

n_total = len(all_images)
n_train = int(train_ratio * n_total)
n_val = int(val_ratio * n_total)

train_files = all_images[:n_train]
val_files = all_images[n_train:n_train + n_val]
test_files = all_images[n_train + n_val:]

splits_dict = {"train": train_files, "val": val_files, "test": test_files}

# Copy images and masks
for split, files in splits_dict.items():
    for fname in files:
        # Copy image
        src_img_path = os.path.join(args.src_images, fname)
        dst_img_path = os.path.join(args.dst_dir, split, "images", fname)
        shutil.copy2(src_img_path, dst_img_path)

        # Copy corresponding mask
        mask_name = fname.replace(".png", ".png___fuse.png")
        src_mask_path = os.path.join(args.src_masks, mask_name)
        dst_mask_path = os.path.join(args.dst_dir, split, "masks", mask_name)
        if os.path.exists(src_mask_path):
            shutil.copy2(src_mask_path, dst_mask_path)
        else:
            print(f"Mask not found for {fname}")

print("Dataset split complete!")


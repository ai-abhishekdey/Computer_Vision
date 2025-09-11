import argparse
import random
import shutil
from pathlib import Path
from sklearn.model_selection import train_test_split

def collect_image_mask_pairs(root_dir):
    image_mask_pairs = []
    tiles = sorted(Path(root_dir).glob("Tile *"))
    
    for tile in tiles:
        tile_name = tile.name.replace(" ", "_")  # e.g., "Tile_1"
        image_dir = tile / "images"
        mask_dir = tile / "masks"

        if not image_dir.exists() or not mask_dir.exists():
            continue

        for img_path in sorted(image_dir.glob("*.jpg")):
            mask_path = mask_dir / (img_path.stem + ".png")
            if mask_path.exists():
                # Store with tile name for debugging
                image_mask_pairs.append((img_path, mask_path, tile_name))
            else:
                print(f"Warning: No mask found for {img_path.name}")
    return image_mask_pairs


def split_and_copy(pairs, output_dir, split, seed, root_dir):
    train_ratio, val_ratio, test_ratio = split
    assert abs(sum(split) - 1.0) < 1e-6, "Split ratios must sum to 1"

    random.seed(seed)

    # Split dataset
    train_pairs, temp_pairs = train_test_split(
        pairs, test_size=(1-train_ratio), random_state=seed
    )
    val_pairs, test_pairs = train_test_split(
        temp_pairs, test_size=test_ratio/(test_ratio+val_ratio), random_state=seed
    )

    splits = {
        "train": train_pairs,
        "val": val_pairs,
        "test": test_pairs
    }

    for split_name, items in splits.items():
        img_out_dir = Path(output_dir) / split_name / "images"
        mask_out_dir = Path(output_dir) / split_name / "masks"
        img_out_dir.mkdir(parents=True, exist_ok=True)
        mask_out_dir.mkdir(parents=True, exist_ok=True)

        for img_path, mask_path, tile_name in items:
            new_img_name = f"{tile_name}_{img_path.name}"
            new_mask_name = f"{tile_name}_{mask_path.name}"

            shutil.copy(img_path, img_out_dir / new_img_name)
            shutil.copy(mask_path, mask_out_dir / new_mask_name)

    # Copy classes.json if exists
    classes_file = Path(root_dir) / "classes.json"
    if classes_file.exists():
        shutil.copy(classes_file, Path(output_dir) / "classes.json")
        print("Copied classes.json to output directory")
    else:
        print("classes.json not found in root directory")

    print("Dataset prepared at:", output_dir)
    print(f"Train: {len(train_pairs)}, Val: {len(val_pairs)}, Test: {len(test_pairs)}")


def main():
    parser = argparse.ArgumentParser(description="Prepare dataset with train/val/test split for semantic segmentation")
    parser.add_argument("--root_dir", type=str, required=True, help="Path to root dataset folder (e.g., 'archive/Semantic segmentation dataset')")
    parser.add_argument("--output_dir", type=str, default="arial_image_dataset", help="Output directory for processed dataset")
    parser.add_argument("--split", type=float, nargs=3, default=[0.7, 0.1, 0.2], help="Train/Val/Test split ratios (must sum to 1)")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for reproducibility")

    args = parser.parse_args()

    pairs = collect_image_mask_pairs(args.root_dir)
    if not pairs:
        print("No image-mask pairs found.")
        return

    split_and_copy(pairs, args.output_dir, args.split, args.seed, args.root_dir)


if __name__ == "__main__":
    main()


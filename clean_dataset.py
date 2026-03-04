import os
from collections import defaultdict

# ---------------- CONFIG ----------------
DATASET_PATH = r"datasets/rail"

# classes you want to REMOVE
REMOVE_CLASSES = {
    # example:
    # 5   # sharp_rails
}

DELETE_EMPTY_IMAGES = True
# ----------------------------------------


def process_split(split):
    label_dir = os.path.join(DATASET_PATH, split, "labels")
    image_dir = os.path.join(DATASET_PATH, split, "images")

    class_count = defaultdict(int)
    removed_labels = 0
    removed_images = 0

    for file in os.listdir(label_dir):
        if not file.endswith(".txt"):
            continue

        label_path = os.path.join(label_dir, file)

        with open(label_path, "r") as f:
            lines = f.readlines()

        new_lines = []

        for line in lines:
            cls = int(line.split()[0])

            if cls in REMOVE_CLASSES:
                removed_labels += 1
                continue

            class_count[cls] += 1
            new_lines.append(line)

        # overwrite cleaned labels
        with open(label_path, "w") as f:
            f.writelines(new_lines)

        # remove image if label becomes empty
        if DELETE_EMPTY_IMAGES and len(new_lines) == 0:
            os.remove(label_path)

            img_name = file.replace(".txt", ".jpg")
            img_path = os.path.join(image_dir, img_name)

            if os.path.exists(img_path):
                os.remove(img_path)
                removed_images += 1

    print(f"\n[{split.upper()}]")
    print("Class counts after cleaning:")
    for k, v in sorted(class_count.items()):
        print(f"Class {k}: {v}")

    print(f"Removed labels: {removed_labels}")
    print(f"Removed empty images: {removed_images}")


if __name__ == "__main__":
    process_split("train")
    process_split("valid")

    print("\n✅ Dataset cleaning completed.")
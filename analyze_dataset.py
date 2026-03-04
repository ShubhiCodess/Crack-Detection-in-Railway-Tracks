import os
from collections import defaultdict
import numpy as np

DATASET_PATH = r"datasets/rail"

CLASS_NAMES = [
    "clipping",
    "lightband",
    "perlage",
    "rails",
    "seams",
    "sharp_rails",
]

TINY_BOX_THRESHOLD = 0.015  # normalized size (~12px at 800 imgsz)


def analyze_split(split):
    label_dir = os.path.join(DATASET_PATH, split, "labels")

    class_counts = defaultdict(int)
    tiny_boxes = defaultdict(int)
    box_sizes = defaultdict(list)

    total_boxes = 0

    for file in os.listdir(label_dir):
        if not file.endswith(".txt"):
            continue

        with open(os.path.join(label_dir, file), "r") as f:
            lines = f.readlines()

        for line in lines:
            parts = line.strip().split()
            cls = int(parts[0])
            w = float(parts[3])
            h = float(parts[4])

            size = np.sqrt(w * h)

            class_counts[cls] += 1
            box_sizes[cls].append(size)
            total_boxes += 1

            if w < TINY_BOX_THRESHOLD or h < TINY_BOX_THRESHOLD:
                tiny_boxes[cls] += 1

    print(f"\n===== {split.upper()} ANALYSIS =====")

    for cls in sorted(class_counts.keys()):
        count = class_counts[cls]
        tiny = tiny_boxes[cls]
        avg_size = np.mean(box_sizes[cls])

        print(
            f"{CLASS_NAMES[cls]:12s} | "
            f"instances: {count:5d} | "
            f"tiny: {tiny:4d} ({tiny/count*100:.1f}%) | "
            f"avg size: {avg_size:.4f}"
        )

    print("\nTotal objects:", total_boxes)


if __name__ == "__main__":
    analyze_split("train")
    analyze_split("valid")
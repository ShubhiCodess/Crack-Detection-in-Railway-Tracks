import os

DATASET = r"datasets/rail"
CLIPPING_CLASS = 0
EXPAND_FACTOR = 2.5   # try 2.0–3.0


def expand(split):
    label_dir = os.path.join(DATASET, split, "labels")

    for file in os.listdir(label_dir):
        if not file.endswith(".txt"):
            continue

        path = os.path.join(label_dir, file)

        new_lines = []

        with open(path, "r") as f:
            lines = f.readlines()

        for line in lines:
            cls, x, y, w, h = map(float, line.split())

            if int(cls) == CLIPPING_CLASS:
                w *= EXPAND_FACTOR
                h *= EXPAND_FACTOR

                # clamp to image bounds
                w = min(w, 1.0)
                h = min(h, 1.0)

            new_lines.append(f"{int(cls)} {x} {y} {w} {h}\n")

        with open(path, "w") as f:
            f.writelines(new_lines)


if __name__ == "__main__":
    expand("train")
    expand("valid")
    print("✅ Clipping boxes expanded.")
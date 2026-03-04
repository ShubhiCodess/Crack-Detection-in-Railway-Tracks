import os, random, shutil

dataset = "datasets/rail"
train_img = f"{dataset}/train/images"
train_lbl = f"{dataset}/train/labels"
val_img   = f"{dataset}/valid/images"
val_lbl   = f"{dataset}/valid/labels"

files = os.listdir(train_img)
random.shuffle(files)

move_count = int(len(files) * 0.15)  # move 15% to validation

for f in files[:move_count]:
    shutil.move(f"{train_img}/{f}", f"{val_img}/{f}")
    label = f.replace(".jpg", ".txt")
    shutil.move(f"{train_lbl}/{label}", f"{val_lbl}/{label}")

print("Resplit complete.")
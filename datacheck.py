import os

# ---- CHANGE THIS PATH ----
dataset_path = r"datasets/rail"   # root dataset folder

train_images = os.path.join(dataset_path, "train", "images")
val_images   = os.path.join(dataset_path, "valid", "images")

def count_images(folder):
    image_ext = (".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff")
    return len([f for f in os.listdir(folder) if f.lower().endswith(image_ext)])

train_count = count_images(train_images)
val_count = count_images(val_images)

print(f"Train Images : {train_count}")
print(f"Validation Images : {val_count}")
print(f"Total Images : {train_count + val_count}")

train_labels = os.path.join(dataset_path, "train", "labels")
val_labels   = os.path.join(dataset_path, "valid", "labels")

print(f"Train Labels : {len(os.listdir(train_labels))}")
print(f"Validation Labels : {len(os.listdir(val_labels))}")
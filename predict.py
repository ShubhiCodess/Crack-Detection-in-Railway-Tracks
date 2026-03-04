from ultralytics import YOLO

# Load trained model
model = YOLO("E:\\Crack Detection\\rail_defect_v2\\runs\\detect\\experiments\\spdconv_ema_contextfix\\weights\\best.pt")

# Run prediction
results = model.predict(
    source="test_images",   # folder containing images
    save=True,              # saves output images
    conf=0.25               # confidence threshold
)

print("Prediction complete. Check runs folder.")

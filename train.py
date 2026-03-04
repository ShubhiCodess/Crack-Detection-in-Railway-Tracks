from ultralytics import YOLO

def main():

    print("\nTraining YOLOv8n from scratch...")

    model = YOLO("ultralytics/cfg/models/v8/yolov8n.yaml")

    model.train(
        data="datasets/rail/data.yaml",
        epochs=40,
        imgsz=800,
        batch=10,
        workers=6,
        device=0,
        pretrained=False,
        close_mosaic=15,
        project="experiments",
        name="good_data_run"
    )

if __name__ == "__main__":
    main()
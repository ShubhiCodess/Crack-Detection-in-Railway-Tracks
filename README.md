# Railway Track Crack Detection System

An end-to-end AI-powered system for automated railway track inspection using a custom-trained YOLO model and a mobile robotic platform.

-*Now being extended with AWS for scalable, real-time cloud-based monitoring.*

## Problem Statement

Manual railway track inspection is:
- Time-consuming
- Error-prone
- Not scalable

This project aims to automate defect detection using Yolo model and robotics to improve safety and efficiency.

## Features

- Real-time railway track monitoring  
- Crack detection using YOLO-based deep learning  
- Continuous image acquisition via ESP32-CAM  
- Wireless image transmission  
- Autonomous robotic movement  
- Modular hardware design  

## System Architecture

Current Pipeline:

Robot → ESP32-CAM → WiFi → Local System → YOLO Model → Detection Output


## Model Details

- Model: Custom YOLO-based architecture
- Dataset Size: ~7000+ images
- Classes: Crack / No Crack
- Focus: Detecting small structural defects
<img width="1536" height="922" alt="diagram" src="https://github.com/user-attachments/assets/4b679c81-d9b7-49b5-b5cf-2e6eee4e3082" />


## Model Performance Comparison
*Trained on a dataset of ~7000+ railway track images with multiple defect classes.*

| Class        | Precision (Baseline) | Recall (Baseline) | mAP@50 (Baseline) | mAP@50-95 (Baseline) | Precision (Proposed) | Recall (Proposed) | mAP@50 (Proposed) | mAP@50-95 (Proposed) |
|-------------|---------------------|------------------|------------------|----------------------|----------------------|-------------------|-------------------|-----------------------|
| Clipping     | 0.692 | 0.441 | 0.536 | 0.214 | 0.752 | 0.470 | 0.721 | 0.301 |
| Lightband    | 0.975 | 0.977 | 0.991 | 0.945 | 0.963 | 0.980 | 0.993 | 0.926 |
| Perlage      | 0.939 | 0.984 | 0.993 | 0.715 | 0.883 | 0.942 | 0.960 | 0.623 |
| Rails        | 0.946 | 0.980 | 0.988 | 0.887 | 0.903 | 0.963 | 0.982 | 0.855 |
| Seams        | 0.964 | 0.994 | 0.993 | 0.954 | 0.964 | 0.986 | 0.994 | 0.932 |
| Sharp_rails  | 0.881 | 1.000 | 0.972 | 0.770 | 0.889 | 0.927 | 0.954 | 0.702 |
### Key Observations

- The proposed model improves detection performance in **Clipping defects significantly** (mAP@50: 0.536 → 0.721)
- Maintains high performance across stable classes like **Seams and Lightband**
- Slight trade-offs in some categories (e.g., Perlage), indicating scope for further tuning
- Overall, the model is more robust for **real-world defect detection scenarios**

## Tech Stack

- Python, OpenCV
- YOLOv8 (custom modified)
- ESP32-CAM, ESP32
- Embedded C (Arduino IDE)
- AWS (in progress)
  
## Sample Results


| Sample Photo | Proposed Model |
|------------------|----------------|
| <img width="640" height="640" alt="xpress (1)" src="https://github.com/user-attachments/assets/007a1703-8dcf-46f0-b87e-817340017167" />| <img width="640" height="640" alt="tested (1)" src="https://github.com/user-attachments/assets/5a0232a6-e26b-462e-9d69-3120688ef3ef" /> |

Example railway defect detection results. The left image shows the original railway track sample, while the right image shows the predicted bounding boxes highlighting detected defects.

## ☁️ AWS Integration (In Progress)

- Upload inspection images to Amazon S3  
- Trigger AWS Lambda on image upload  
- Enable scalable, event-driven processing  
- Future: Real-time dashboard using API Gateway + frontend  
  



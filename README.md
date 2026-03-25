**Railway Track Crack Detection using YOLOv8**
📌 Overview

This project focuses on detecting cracks in railway tracks using a deep learning-based object detection model (YOLOv8) integrated with an ESP32-CAM for real-time image capture.
The system aims to improve railway safety by identifying structural defects early and enabling timely maintenance.

🎯 Objectives
Detect cracks in railway tracks with high accuracy
Enable real-time monitoring using embedded systems
Reduce dependency on manual inspection
Improve railway safety and reliability

🧠 Model Architecture
Base Model: YOLOv8
Enhancements:
SPDConv (Spatial-to-Depth Convolution) for better feature preservation
Improved small-object detection
Optimized for real-time performance

📂 Dataset
Training Images: 5854
Validation Images: 1297
Annotated using bounding boxes for crack detection
Includes variations in:
Lighting conditions
Track textures
Crack orientations

⚙️ Tech Stack
Programming Language: Python, C/C++
Frameworks: PyTorch, Ultralytics YOLOv8
Hardware: ESP32-CAM
Tools: Arduino IDE, OpenCV

🔌 Hardware Setup
ESP32-CAM module used for capturing images
Connected via CP2102 USB to TTL converter
Configured using Arduino IDE

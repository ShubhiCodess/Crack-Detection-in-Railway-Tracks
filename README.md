# **Railway Track Crack Detection System**

## **Overview**

This project presents an automated railway track crack detection system using computer vision and embedded systems. The system integrates a mobile robotic platform with a camera module and a deep learning model (YOLO-based) to continuously monitor railway tracks and detect structural defects in real time.

The goal is to reduce manual inspection effort, improve detection accuracy, and enable early fault identification to prevent accidents.

## Features

1.Real-time railway track monitoring

2.Crack detection using YOLO-based deep learning model

3.Continuous image acquisition via ESP32-CAM

4.Wireless transmission of images to a processing system

5.Autonomous movement of inspection robot

Modular hardware design for scalability


## Hardware Components:

ESP32-CAM (image acquisition + WiFi transmission)

ESP32 (motor control)

L298N Motor Driver

BO Motors with wheels

LM2596 Buck Converter (voltage regulation)

18650 Li-ion Battery

Robotic chassis

## Software Components:

Python (image processing pipeline)

YOLO (custom-trained model for crack detection)

OpenCV (image handling)

Embedded C (ESP32 programming via Arduino IDE)

## **Working Principle:**

1.The robot moves along the railway track using BO motors.

2.ESP32-CAM captures images continuously.

3.Images are transmitted over WiFi to a laptop/server.

4.A Python script monitors incoming images in real time.

5.The YOLO model processes each frame to detect cracks.

6.If a crack is detected, the system flags the image for further analysis.


## YOLO Model Details:

Custom-trained YOLO architecture for crack detection

Enhanced feature extraction for small defect identification

Backbone, Neck, and Detection Head optimized for railway imagery

Trained on dataset containing cracked and non-cracked track images

<img width="1536" height="922" alt="diagram" src="https://github.com/user-attachments/assets/4b679c81-d9b7-49b5-b5cf-2e6eee4e3082" />

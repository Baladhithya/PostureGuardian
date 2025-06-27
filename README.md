# Posture Guardian 🧍‍♂️📐 | A TinyML-Based Wearable for Posture Monitoring
A compact and intelligent wearable posture correction system built using TinyML and Arduino. This project provides real-time feedback using a lightweight ML model running directly on an Arduino Uno, with data from an MPU6050 accelerometer/gyroscope and feedback via an I2C LCD.

## 🔧 Features

- 💡 Real-time posture classification using accelerometer + gyroscope
- 🧠 On-device inference via TensorFlow Lite for Microcontrollers (TinyML)
- 📟 LCD feedback interface for user awareness
- 🔋 Battery-powered, wearable, and lightweight
- 💰 Cost-effective and privacy-preserving (no camera or cloud involved)

---

## 🧠 Powered by TinyML

**What is TinyML?**
TinyML brings Machine Learning to embedded devices with extremely low resource footprints. In this project, we used:
- Logistic Regression model trained on posture data
- TensorFlow Lite to quantize and convert to `.tflite`
- Converted to C array using `xxd` or Python script
- Deployed with <2KB RAM usage on Arduino Uno

---

## ⚙️ Hardware Components

| Component       | Description                                |
|----------------|--------------------------------------------|
| Arduino Uno     | Main MCU for inference                    |
| MPU6050         | 3-axis accelerometer and gyroscope        |
| I2C LCD Display | Displays posture classification feedback   |
| Jumper Wires    | Connections                               |
| Battery Pack    | Portable power supply                     |

---

## 📈 Model Summary

- **Accuracy**: 88%
- **Model Size**: ~30 KB Flash, 1.9 KB RAM
- **Inference Time**: <100ms
- **Classes**: Good Posture, Bad Posture

👥 Authors
Baladhithya T 

S. Krithik Rishi

Mentor: Dr. Yokesh Babu D, VIT University

📽️ [Watch on YouTube](https://youtu.be/8XapK43eMfQ?si=fEIxYqNx7RbCLTOX)

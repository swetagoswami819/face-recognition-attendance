# Face Recognition Attendance System

This project is a Face Recognition-based Attendance System that automatically marks attendance by detecting and recognizing faces using a webcam.

## 💡 What it Does

- Captures real-time video from webcam
- Detects and recognizes faces using OpenCV
- Automatically stores attendance data in a MySQL database

## 🛠 Technologies Used

- Python
- OpenCV
- MySQL
- Tkinter (if GUI used)

## 🔑 Features

- Real-time face detection
- Face recognition from trained data
- Automatic attendance marking
- Data stored with timestamp in MySQL
- Prevents duplicate attendance entries

## 📁 Project Structure

```
📦 FaceRecognitionAttendance
 ┣ 📂 data
 ┣ 📂 images
 ┣ 📜 attendance.py
 ┣ 📜 train_model.py
 ┣ 📜 recognize_face.py
 ┣ 📜 database_connection.py
 ┗ 📜 README.md
```

## 🚀 How to Run

1. Clone the repo
2. Install dependencies:
   ```
   pip install opencv-python mysql-connector-python
   ```
3. Run `train_model.py` to train face data
4. Run `recognize_face.py` to start attendance

## 📌 Note

- Make sure MySQL server is running
- Create a database and table before running the system

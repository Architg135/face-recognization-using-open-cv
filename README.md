# Real-Time Face Detection with OpenCV

This repository contains a Python script for real-time face detection using a webcam and OpenCV's Haar cascade classifier. The script captures video from the webcam, processes each frame to detect faces, and displays the frames with rectangles drawn around detected faces.

## Features

- **Real-Time Video Capture**: Captures video feed from the default webcam.
- **Face Detection**: Utilizes OpenCV's Haar cascade classifier to detect faces in each frame.
- **Grayscale Conversion**: Converts frames to grayscale for improved detection performance.
- **Visualization**: Draws rectangles around detected faces and displays the video feed in real-time.
- **Interactive**: Runs until the user presses the 'q' key to exit.

## Prerequisites

- Python 3.x
- OpenCV

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/real-time-face-detection.git
   cd real-time-face-detection
   ```

2. **Install the required dependencies**:
   ```bash
   pip install opencv-python
   ```

## Usage

1. **Run the script**:
   ```bash
   python face_detection.py
   ```

2. **Exit**: Press the 'q' key to stop the video capture and close the window.

## Code Overview

### Import Libraries

The script starts by importing necessary libraries:
```python
import pathlib
import cv2
```

### Haar Cascade Classifier Path

It constructs the correct path to the Haar cascade file for frontal face detection:
```python
cascade_path = pathlib.Path(cv2.data.haarcascades) / "haarcascade_frontalface_default.xml"
```

### Initialize Cascade Classifier

The script initializes the Haar cascade classifier and checks if it's loaded correctly:
```python
clf = cv2.CascadeClassifier(str(cascade_path))
if clf.empty():
    print("Failed to load cascade classifier")
    exit(1)
```

### Open Webcam

It attempts to open the default webcam (camera index 0) and checks if it's opened successfully:
```python
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Failed to open camera")
    exit(1)
```

### Video Capture Loop

The script enters an infinite loop to capture and process frames from the webcam:
```python
while True:
    ret, frame = camera.read()
    if not ret:
        print("Failed to capture image")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = clf.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 255, 0), 2)

    cv2.imshow("Faces", frame)
    if cv2.waitKey(1) == ord("q"):
        break
```

### Release Resources

Finally, it releases the webcam and destroys all OpenCV windows:
```python
camera.release()
cv2.destroyAllWindows()
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenCV for providing the tools and libraries for computer vision.
- The authors of the Haar cascade classifier for face detection.

---

Feel free to fork this repository, open issues, and submit pull requests to contribute to this project. If you have any questions or suggestions, please contact [yourname@example.com](mailto:yourname@example.com).

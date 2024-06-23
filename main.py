import pathlib
import cv2

# Correct path to Haar cascade file
cascade_path = pathlib.Path(cv2.data.haarcascades) / "haarcascade_frontalface_default.xml"
print(f"Using cascade file: {cascade_path}")

# Initialize the cascade classifier
clf = cv2.CascadeClassifier(str(cascade_path))
if clf.empty():
    print("Failed to load cascade classifier")
    exit(1)

camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Failed to open camera")
    exit(1)

while True:
    ret, frame = camera.read()
    if not ret:
        print("Failed to capture image")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = clf.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,  # Lowered from 18 to 5 for better initial detection
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    print(f"Detected {len(faces)} faces")

    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 255, 0), 2)

    cv2.imshow("Faces", frame)
    if cv2.waitKey(1) == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()

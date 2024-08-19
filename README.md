
# Face Recognition with DeepFace and OpenCV

This project demonstrates a simple face recognition system using `DeepFace` and OpenCV. The system captures video from a webcam, processes each frame to check for a match against a reference image, and displays the result on the video feed.

## Requirements

- Python 3.x
- OpenCV
- DeepFace

You can install the required packages using pip:

```bash
pip install opencv-python deepface
```

## Project Structure

```
Facial-Recognition-Software/
│
├── reference.jpg
├── reference2.jpg
├── main.py
├── facial_recognition.jpg
└── README.md
```

- `reference.jpg`: Image used for face comparison.
- `main.py`: The main script for the face recognition system.

## Usage

1. **Place Your Reference Image:**
   - Ensure that `reference.jpg` is present in the same directory as `main.py`. This image will be used for face matching.

2. **Run the Script:**

   Execute the script using Python:

   ```bash
   python main.py
   ```

3. **Interaction:**
   - The script opens a webcam feed.
   - It checks every 30 frames to see if the face in the frame matches the reference image.
   - If a match is found, the text "MATCH!" is displayed in green; otherwise, "NO MATCH!" is displayed in red.
   - Press `q` to quit the application.

## Code

```python
import threading
import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
face_match = False
reference_img = cv2.imread('reference.jpg')
lock = threading.Lock()

def check_face(frame):
    global face_match
    try:
        result = DeepFace.verify(frame, reference_img.copy())['verified']
        with lock:
            face_match = result
    except ValueError:
        with lock:
            face_match = False

while True:
    ret, frame = cap.read()

    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass
        counter += 1
        
        with lock:
            if face_match:
                cv2.putText(frame, 'MATCH!', (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
            else:
                cv2.putText(frame, 'NO MATCH!', (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.imshow('video', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

## Notes

- Make sure you have a working webcam and the `reference.jpg` image for the face comparison.
- Adjust the webcam resolution and frame rate settings as needed.
- This script is for educational purposes and may require adjustments for production use.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

This README provides clear instructions on setting up and running your face recognition system, including a description of the project, how to use it, and the full code.

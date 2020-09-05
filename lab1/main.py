import time
import os

import numpy as np
import cv2


VIDEO_FOLDER = "videos"
FILE_NAME = f"output_{int(time.time())}.avi"
FIGURES_PARAMETERS = [(10, 10), (100, 100), (0, 255, 0), 5]

if __name__ == "__main__":
    # Check if folder exists
    if not (os.path.exists(VIDEO_FOLDER) and os.path.isdir(VIDEO_FOLDER)):
        os.mkdir(VIDEO_FOLDER)

    # Create objects
    cap = cv2.VideoCapture(0)
    out = cv2.VideoWriter(
        os.path.join(VIDEO_FOLDER, FILE_NAME),
        cv2.VideoWriter_fourcc(*"MJPG"),
        30, (int(cap.get(3)), int(cap.get(4)))
    )

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            # Write to videofile and show on screen
            out.write(frame)

            # Convert to grayscale and draw shapes
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = np.repeat(gray[:, :, np.newaxis], 3, axis=2)
            gray = cv2.line(gray, *FIGURES_PARAMETERS)
            gray = cv2.rectangle(gray, *FIGURES_PARAMETERS)

            # Show both frames
            cv2.imshow("original", frame)
            cv2.imshow("modified", gray)

            # Leave if `q` was pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            break

    # Release all objects
    cap.release()
    out.release()
    cv2.destroyAllWindows()

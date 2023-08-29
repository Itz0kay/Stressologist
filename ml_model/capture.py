import cv2
import time
from tkinter import *

def close_image():
    cv2.destroyAllWindows()

def capture_image():
    # Add delay before opening the webcam
    time.sleep(2)

    # Open the webcam
    cap = cv2.VideoCapture(0)

    # Display the countdown before capturing the image
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)

    # Capture a frame
    ret, frame = cap.read()
    if not ret:
        print("Error capturing image")

    # Save the image
    cv2.imwrite("sami.jpg", frame)

    # Display the captured image
    cv2.imshow("Captured Image", frame)
    close_button = Button(root, text="Close", command=close_image)
    close_button.pack()
    cv2.waitKey(0)

    # Release the webcam
    cap.release()

root = Tk()
root.title("Capture Image")

# Create a button to capture the image
capture_button = Button(root, text="Capture Image", command=capture_image)
capture_button.pack()

root.mainloop()

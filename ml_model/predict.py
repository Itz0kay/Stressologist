import numpy as np
import cv2
from keras.models import load_model
# from model import emotion as emotions

emotions = ['angry', 'disgusted', 'fearful', 'happy', 'neutral', 'surprised', 'sad']


# Load the model
model = load_model("modelweight.h5")

# Load the image
image = cv2.imread("sami.jpg")

# Preprocess the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, (48, 48))
gray = gray.reshape(1, 48, 48, 1)
gray = gray / 255

image = np.expand_dims(gray, axis=0)


image = image.reshape(1, 48, 48, 1)


# Make a prediction
predictions = model.predict(image)
top_3 = np.argsort(predictions[0])[-3:]
top_3_emotions = [emotions[i] for i in top_3]
print("Emotion:",top_3_emotions)


# print(emotions)

# emotion = emotions[np.argmax(emotions)]
# print("Emotion:", emotion)


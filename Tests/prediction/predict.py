import numpy as np
import cv2
from keras.models import load_model 
import os
from django.conf import settings

emotions = ['angry', 'disgusted', 'fearful', 'happy', 'neutral', 'surprised', 'sad']

model_path = os.path.join(settings.BASE_DIR, 'Tests', 'prediction', 'modelweight.h5')
model = load_model(model_path)  

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (48, 48))
    reshaped = resized.reshape(1, 48, 48, 1)
    normalized = reshaped / 255.0
    return normalized

def predict_emotions(request):
    if 'image' not in request.FILES:
        return "No image found in the request"
    
    image = cv2.imdecode(np.frombuffer(request.FILES['image'].read(), np.uint8), cv2.IMREAD_UNCHANGED)
    
    processed_image = preprocess_image(image)
    
    predictions = model.predict(processed_image)
    top_3 = np.argsort(predictions[0])[-3:]
    top_3_emotions = [emotions[i] for i in top_3]
    
    return top_3_emotions

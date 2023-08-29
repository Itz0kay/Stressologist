import random

emotions = {
    'angry':random.randrange(25,30), 
    'disgusted':random.randrange(15,20),
    'fearful':random.randrange(20,28), 
    'happy':random.randrange(10,17), 
    'neutral':random.randrange(10,15), 
    'surprised':random.randrange(10,12), 
    'sad':random.randrange(25,32)
    }

def calculateStressPercent(predictions):
    result = 0
    for i in predictions:
        result += emotions[i]
    return result
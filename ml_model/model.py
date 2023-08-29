import numpy as np
import pandas as pd
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import SGD
from keras.utils import np_utils

# Load the FER2013 dataset
data = pd.read_csv("fer2013.csv")
# print(data)

# Split the dataset into training and test sets
x_train, y_train, x_test, y_test = [], [], [], []
for index, row in data.iterrows():
    emotion = row['emotion']
    pixels = list(map(int, row['pixels'].split()))
    pixels = np.array(pixels)
    pixels = pixels.reshape(48, 48)

    if row['Usage'] == "Training":
        x_train.append(pixels)
        y_train.append(emotion)
    else:
        x_test.append(pixels)
        y_test.append(emotion)

if __name__ == "__main__":
    # Convert the data to numpy arrays
    x_train = np.array(x_train)
    y_train = np.array(y_train)
    x_test = np.array(x_test)
    y_test = np.array(y_test)

# Reshape the data to 48x48x1
    x_train = x_train.reshape(x_train.shape[0], 48, 48, 1)
    x_test = x_test.reshape(x_test.shape[0], 48, 48, 1)

# Normalize the data
    x_train = x_train / 255
    x_test = x_test / 255

# One-hot encode the labels
    y_train = np_utils.to_categorical(y_train)
    y_test = np_utils.to_categorical(y_test)

# Create the model
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(48, 48, 1)))
    model.add(Conv2D(32, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(7, activation='softmax'))

    # Compile the model
    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Fit the model on the training data
    model.fit(x_train, y_train, batch_size=32, epochs=15)

# Evaluate the model on the test data
    score = model.evaluate(x_test, y_test, batch_size=32)
    print("Test loss: ", score[0])
    print("Test accuracy: ", score[1])

# Save the weights
    model.save("model.h5")
